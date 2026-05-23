import sys; sys.path.insert(0, 'src')
import unittest
import tempfile
import os
from security.keys.key_manager import QuantumKeyManager

class TestQuantumKeyManager(unittest.TestCase):
    def setUp(self):
        self.km = QuantumKeyManager()

    def test_generate_keypair(self):
        result = self.km.generate_keypair("test-key-1", "insurance")
        self.assertEqual(result["key_id"], "test-key-1")
        self.assertIn("kem_public_key", result)

    def test_sign_and_verify(self):
        self.km.generate_keypair("test-key-2")
        doc = b"Insurance policy document 2026"
        sig = self.km.sign_document("test-key-2", doc)
        self.assertTrue(self.km.verify_document("test-key-2", doc, sig))

    def test_encrypt_decrypt(self):
        self.km.generate_keypair("test-key-3")
        ct, ss1 = self.km.encrypt_shared_secret("test-key-3")
        ss2 = self.km.decrypt_shared_secret("test-key-3", ct)
        self.assertEqual(ss1, ss2)

    def test_rotate_keys(self):
        self.km.generate_keypair("test-key-4")
        new_key = self.km.rotate_keys("test-key-4")
        self.assertEqual(new_key["key_id"], "test-key-4")
        self.assertIn("rotated", self.km.keys["test-key-4"]["purpose"])

    def test_list_keys(self):
        self.km.generate_keypair("key-a")
        self.km.generate_keypair("key-b")
        keys = self.km.list_keys()
        self.assertEqual(len(keys), 2)

    def test_export_public_keys(self):
        self.km.generate_keypair("key-export")
        pub = self.km.export_public_keys("key-export")
        self.assertIn("kem_public_key", pub)
        self.assertIn("sig_public_key", pub)

    def test_save_load(self):
        self.km.generate_keypair("persist-key")
        with tempfile.NamedTemporaryFile(suffix='.json', delete=False) as f:
            path = f.name
        try:
            self.km.save_key_store(path)
            km2 = QuantumKeyManager()
            km2.load_key_store(path)
            self.assertIn("persist-key", km2.keys)
        finally:
            os.unlink(path)

if __name__ == '__main__':
    unittest.main()
