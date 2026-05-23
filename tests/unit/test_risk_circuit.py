import sys; sys.path.insert(0, 'src')
import unittest
from quantum.circuits.risk_circuit import RiskScoringCircuit, create_simple_risk_circuit
import numpy as np

class TestRiskScoringCircuit(unittest.TestCase):
    def setUp(self):
        self.circuit = RiskScoringCircuit(num_qubits=4)

    def test_initialization(self):
        self.assertEqual(self.circuit.num_qubits, 4)

    def test_risk_feature_circuit(self):
        factors = [0.2, 0.5, 0.8]
        result = self.circuit.create_risk_feature_circuit(factors)
        self.assertIn('num_qubits', result)
        self.assertIn('initial_state', result)
        self.assertIn('gates', result)
        self.assertEqual(result['num_qubits'], 4)

    def test_risk_feature_circuit_too_many_factors(self):
        factors = [0.1] * 20
        with self.assertRaises(ValueError):
            self.circuit.create_risk_feature_circuit(factors)

    def test_variational_layer(self):
        gates = self.circuit.create_variational_layer(depth=2)
        self.assertTrue(len(gates) > 0)

    def test_variational_layer_specific_depth(self):
        gates_depth3 = self.circuit.create_variational_layer(depth=3)
        gates_depth1 = self.circuit.create_variational_layer(depth=1)
        self.assertGreater(len(gates_depth3), len(gates_depth1))

    def test_risk_score_calculation(self):
        result = {'counts': {'0000': 100, '1111': 100, '0101': 50, '1010': 50}}
        score = self.circuit.calculate_risk_score(result)
        self.assertGreaterEqual(score, 0.0)
        self.assertLessEqual(score, 1.0)

    def test_risk_score_extreme(self):
        result = {'counts': {'1111': 300}}
        score = self.circuit.calculate_risk_score(result)
        self.assertGreater(score, 0.5)

    def test_create_simple_risk_circuit_convenience(self):
        factors = [0.3, 0.6, 0.9]
        circuit = create_simple_risk_circuit(factors)
        self.assertIn('name', circuit)
        self.assertIn('num_qubits', circuit)
        self.assertIn('gates', circuit)
        self.assertEqual(circuit['name'], 'risk_scoring_circuit')

    def test_empty_factors(self):
        factors = []
        result = self.circuit.create_risk_feature_circuit(factors)
        self.assertEqual(len(result['initial_state']), 16)

    def test_risk_score_zero_counts(self):
        result = {'counts': {}}
        score = self.circuit.calculate_risk_score(result)
        self.assertEqual(score, 0.5)

if __name__ == '__main__':
    unittest.main()
