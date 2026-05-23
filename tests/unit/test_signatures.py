import sys; sys.path.insert(0, 'src')
import unittest
from security.pqc.signatures import PQCSignatureFactory, MockDilithiumSignature

class TestPQCSignatures(unittest.TestCase):
    def test_dilithium2_keypair(self):
        sig = PQCSignatureFactory.create_signature("Dilithium2")
        pk, sk = sig.generate_keypair()
        self.assertEqual(len(pk), sig.public_key_length)
        self.assertEqual(len(sk), sig.private_key_length)

    def test_dilithium3_sign_verify(self):
        sig = PQCSignatureFactory.create_signature("Dilithium3")
        pk, sk = sig.generate_keypair()
        msg = b"Test insurance document"
        signature = sig.sign(sk, msg)
        self.assertTrue(sig.verify(pk, msg, signature))

    def test_tampered_message(self):
        sig = PQCSignatureFactory.create_signature("Dilithium3")
        pk, sk = sig.generate_keypair()
        msg = b"Original message"
        signature = sig.sign(sk, msg)
        tampered = b"Tampered message"
        result = sig.verify(pk, tampered, signature)
        self.assertFalse(result)
