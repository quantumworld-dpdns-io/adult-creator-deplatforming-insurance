import sys; sys.path.insert(0, 'src')
import unittest
from quantum.circuits.risk_circuit import RiskScoringCircuit
from quantum.algorithms.ensemble_risk import EnsembleRiskScorer
from security.pqc.kem import PQCKEMFactory
from security.pqc.signatures import PQCSignatureFactory
from security.keys.key_manager import QuantumKeyManager

class TestQuantumIntegration(unittest.TestCase):
    def test_full_risk_scoring_pipeline(self):
        circuit = RiskScoringCircuit(num_qubits=4)
        factors = [0.3, 0.7, 0.2, 0.5]
        circ_spec = circuit.create_risk_feature_circuit(factors)
        self.assertIn('num_qubits', circ_spec)
        scorer = EnsembleRiskScorer(4)
        result = scorer.score(factors)
        self.assertGreaterEqual(result['risk_score'], 0.0)
        self.assertLessEqual(result['risk_score'], 1.0)

    def test_quantum_with_pqc(self):
        kem = PQCKEMFactory.create_kem("Kyber768")
        pk, sk = kem.generate_keypair()
        ct, ss1 = kem.encapsulate(pk)
        ss2 = kem.decapsulate(sk, ct)
        self.assertEqual(ss1, ss2)
        sig = PQCSignatureFactory.create_signature("Dilithium3")
        sig_pk, sig_sk = sig.generate_keypair()
        msg = b"Quantum risk assessment result"
        signature = sig.sign(sig_sk, msg)
        self.assertTrue(sig.verify(sig_pk, msg, signature))

    def test_key_manager_with_quantum(self):
        km = QuantumKeyManager()
        key_info = km.generate_keypair("quantum-key-1")
        self.assertIn("kem_public_key", key_info)
        ct, ss1 = km.encrypt_shared_secret("quantum-key-1")
        ss2 = km.decrypt_shared_secret("quantum-key-1", ct)
        self.assertEqual(ss1, ss2)
        doc = b"Quantum-encrypted insurance document"
        sig = km.sign_document("quantum-key-1", doc)
        self.assertTrue(km.verify_document("quantum-key-1", doc, sig))

    def test_vqe_and_sign(self):
        from quantum.algorithms import VQERiskOptimizer
        vqe = VQERiskOptimizer(4)
        risk_result = vqe.optimize([0.5, 0.5, 0.5, 0.5])
        score = risk_result['risk_score']
        km = QuantumKeyManager()
        km.generate_keypair("vqe-key")
        doc = f"Risk score: {score}".encode()
        sig = km.sign_document("vqe-key", doc)
        self.assertTrue(km.verify_document("vqe-key", doc, sig))

    def test_qmc_confidence_interval(self):
        from quantum.algorithms import QuantumMonteCarloRisk
        qmc = QuantumMonteCarloRisk(4)
        result = qmc.simulate([0.2, 0.5, 0.8, 0.1], num_samples=1000)
        ci = result['confidence_interval']
        self.assertEqual(len(ci), 2)
        self.assertLessEqual(ci[0], ci[1])
        self.assertGreaterEqual(ci[0], 0.0)
        self.assertLessEqual(ci[1], 1.0)

if __name__ == '__main__':
    unittest.main()
