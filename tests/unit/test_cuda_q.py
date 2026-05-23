import sys; sys.path.insert(0, 'src')
import unittest
from quantum.cuda_q.backend import CUDABackend

class TestCUDABackend(unittest.TestCase):
    def setUp(self):
        self.backend = CUDABackend(target="simulator")

    def test_initialization(self):
        result = self.backend.initialize()
        self.assertTrue(result)
        self.assertTrue(self.backend.initialized)

    def test_execute_circuit(self):
        self.backend.initialize()
        circuit = {'num_qubits': 2, 'gates': []}
        result = self.backend.execute_circuit(circuit, shots=100)
        self.assertIn('counts', result)
        self.assertIn('shots', result)
        self.assertEqual(result['shots'], 100)

    def test_device_info(self):
        info = self.backend.get_device_info()
        self.assertIn('name', info)
        self.assertIn('max_qubits', info)
        self.assertGreater(info['max_qubits'], 0)

    def test_execute_large_circuit(self):
        self.backend.initialize()
        circuit = {'num_qubits': 8, 'gates': []}
        result = self.backend.execute_circuit(circuit, shots=50)
        self.assertEqual(result['shots'], 50)

    def test_shutdown(self):
        self.backend.initialize()
        self.backend.shutdown()
        self.assertFalse(self.backend.initialized)

if __name__ == '__main__':
    unittest.main()
