import sys; sys.path.insert(0, 'src')
import unittest
from quantum.utils.entropy import QuantumEntropyGenerator, generate_quantum_entropy

class TestQuantumEntropy(unittest.TestCase):
    def test_generate_entropy_default(self):
        entropy = generate_quantum_entropy()
        self.assertEqual(len(entropy), 32)

    def test_generate_entropy_custom_size(self):
        entropy = generate_quantum_entropy(64)
        self.assertEqual(len(entropy), 64)

    def test_entropy_generator_basic(self):
        gen = QuantumEntropyGenerator()
        entropy = gen.generate(16)
        self.assertEqual(len(entropy), 16)

    def test_entropy_generator_add_entropy(self):
        gen = QuantumEntropyGenerator()
        gen.add_entropy(b"additional entropy data")
        e1 = gen.generate(32)
        e2 = gen.generate(32)
        self.assertNotEqual(e1, e2)

    def test_quantum_random_bits(self):
        bits = QuantumEntropyGenerator.generate_quantum_random_bits(256)
        self.assertEqual(len(bits), 256)
        self.assertTrue(all(c in '01' for c in bits))

    def test_reseed(self):
        gen = QuantumEntropyGenerator()
        gen.add_entropy(b"test data")
        gen.reseed()
        entropy = gen.generate(32)
        self.assertEqual(len(entropy), 32)

if __name__ == '__main__':
    unittest.main()
