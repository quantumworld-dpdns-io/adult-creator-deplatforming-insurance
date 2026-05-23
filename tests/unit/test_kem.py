import sys; sys.path.insert(0, 'src')
import unittest
from security.pqc.kem import PQCKEMFactory, MockKyberKEM

class TestPQCKEM(unittest.TestCase):
    def test_kyber512_creation(self):
        kem = PQCKEMFactory.create_kem("Kyber512")
        self.assertIn("Kyber", kem.algorithm_name)
        self.assertGreater(kem.public_key_length, 0)

    def test_kyber768_keypair(self):
        kem = PQCKEMFactory.create_kem("Kyber768")
        pk, sk = kem.generate_keypair()
        self.assertEqual(len(pk), kem.public_key_length)
        self.assertEqual(len(sk), kem.private_key_length)

    def test_kyber1024_encapsulate_decapsulate(self):
        kem = PQCKEMFactory.create_kem("Kyber1024")
        pk, sk = kem.generate_keypair()
        ct, ss1 = kem.encapsulate(pk)
        ss2 = kem.decapsulate(sk, ct)
        self.assertEqual(ss1, ss2)

    def test_invalid_algorithm(self):
        with self.assertRaises(ValueError):
            PQCKEMFactory.create_kem("InvalidAlgo")
