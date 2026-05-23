import sys; sys.path.insert(0, 'src')
import unittest
from quantum.algorithms import EnsembleRiskScorer, VQERiskOptimizer, QAOARiskOptimizer, QuantumMonteCarloRisk

class TestQuantumAlgorithms(unittest.TestCase):
    def test_vqe_risk_optimizer(self):
        vqe = VQERiskOptimizer(4)
        result = vqe.optimize([0.3, 0.7, 0.2, 0.5])
        self.assertIn('risk_score', result)
        self.assertGreaterEqual(result['risk_score'], 0.0)
        self.assertLessEqual(result['risk_score'], 1.0)

    def test_qaoa_risk_optimizer(self):
        qaoa = QAOARiskOptimizer(4)
        result = qaoa.optimize([0.1, 0.9, 0.4, 0.6])
        self.assertIn('risk_score', result)
        self.assertGreaterEqual(result['risk_score'], 0.0)

    def test_quantum_monte_carlo(self):
        qmc = QuantumMonteCarloRisk(4)
        result = qmc.simulate([0.2, 0.5, 0.8, 0.3], num_samples=100)
        self.assertIn('risk_score', result)
        self.assertIn('std_dev', result)
        self.assertIn('confidence_interval', result)

    def test_ensemble_scorer(self):
        ensemble = EnsembleRiskScorer(4)
        result = ensemble.score([0.3, 0.6, 0.2, 0.7])
        self.assertIn('risk_score', result)
        self.assertIn('individual', result)
        self.assertIn('weights', result)
        self.assertAlmostEqual(sum(result['weights'].values()), 1.0)

    def test_ensemble_scorer_different_qubits(self):
        ensemble = EnsembleRiskScorer(6)
        result = ensemble.score([0.1]*6)
        self.assertIn('risk_score', result)

    def test_vqe_edge_cases(self):
        vqe = VQERiskOptimizer(2)
        result = vqe.optimize([1.0, 1.0])
        self.assertLessEqual(result['risk_score'], 1.0)
        result2 = vqe.optimize([0.0, 0.0])
        self.assertGreaterEqual(result2['risk_score'], 0.0)

if __name__ == '__main__':
    unittest.main()
