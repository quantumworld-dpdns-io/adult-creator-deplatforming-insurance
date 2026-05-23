"""Quantum-resistant key management module."""

import os
import json
import base64
from typing import Dict, Tuple, Optional, Any
from datetime import datetime, timedelta
import logging

from ..pqc.kem import PQCKEMFactory, PQCKEM
from ..pqc.signatures import PQCSignatureFactory, PQCSignature

logger = logging.getLogger(__name__)

class QuantumKeyManager:
    def __init__(self, kem_algorithm: str = "Kyber768", sig_algorithm: str = "Dilithium3"):
        self.kem: PQCKEM = PQCKEMFactory.create_kem(kem_algorithm)
        self.sig: PQCSignature = PQCSignatureFactory.create_signature(sig_algorithm)
        self.keys: Dict[str, Dict[str, Any]] = {}
        logger.info(f"Initialized QuantumKeyManager with {kem_algorithm}, {sig_algorithm}")

    def generate_keypair(self, key_id: str, purpose: str = "general") -> Dict[str, Any]:
        kem_pk, kem_sk = self.kem.generate_keypair()
        sig_pk, sig_sk = self.sig.generate_keypair()
        key_entry = {
            "key_id": key_id,
            "purpose": purpose,
            "created": datetime.utcnow().isoformat(),
            "expires": (datetime.utcnow() + timedelta(days=365)).isoformat(),
            "kem_algorithm": self.kem.algorithm_name,
            "kem_public_key": base64.b64encode(kem_pk).decode(),
            "kem_private_key": base64.b64encode(kem_sk).decode(),
            "sig_algorithm": self.sig.algorithm_name,
            "sig_public_key": base64.b64encode(sig_pk).decode(),
            "sig_private_key": base64.b64encode(sig_sk).decode(),
        }
        self.keys[key_id] = key_entry
        logger.info(f"Generated keypair: {key_id} for {purpose}")
        return {
            "key_id": key_id,
            "kem_public_key": kem_pk,
            "sig_public_key": sig_pk,
            "kem_algorithm": self.kem.algorithm_name,
            "sig_algorithm": self.sig.algorithm_name,
        }

    def sign_document(self, key_id: str, document: bytes) -> bytes:
        if key_id not in self.keys:
            raise ValueError(f"Key not found: {key_id}")
        sk = base64.b64decode(self.keys[key_id]["sig_private_key"])
        return self.sig.sign(sk, document)

    def verify_document(self, key_id: str, document: bytes, signature: bytes) -> bool:
        if key_id not in self.keys:
            raise ValueError(f"Key not found: {key_id}")
        pk = base64.b64decode(self.keys[key_id]["sig_public_key"])
        return self.sig.verify(pk, document, signature)

    def encrypt_shared_secret(self, key_id: str) -> Tuple[bytes, bytes]:
        if key_id not in self.keys:
            raise ValueError(f"Key not found: {key_id}")
        pk = base64.b64decode(self.keys[key_id]["kem_public_key"])
        return self.kem.encapsulate(pk)

    def decrypt_shared_secret(self, key_id: str, ciphertext: bytes) -> bytes:
        if key_id not in self.keys:
            raise ValueError(f"Key not found: {key_id}")
        sk = base64.b64decode(self.keys[key_id]["kem_private_key"])
        return self.kem.decapsulate(sk, ciphertext)

    def rotate_keys(self, key_id: str) -> Dict[str, Any]:
        if key_id in self.keys:
            del self.keys[key_id]
        return self.generate_keypair(key_id, purpose="rotated")

    def export_public_keys(self, key_id: str) -> Dict[str, str]:
        if key_id not in self.keys:
            raise ValueError(f"Key not found: {key_id}")
        return {
            "key_id": key_id,
            "kem_algorithm": self.keys[key_id]["kem_algorithm"],
            "kem_public_key": self.keys[key_id]["kem_public_key"],
            "sig_algorithm": self.keys[key_id]["sig_algorithm"],
            "sig_public_key": self.keys[key_id]["sig_public_key"],
        }

    def save_key_store(self, path: str):
        with open(path, 'w') as f:
            json.dump(self.keys, f, indent=2)
        logger.info(f"Key store saved to {path}")

    def load_key_store(self, path: str):
        with open(path) as f:
            self.keys = json.load(f)
        logger.info(f"Key store loaded from {path}")

    def list_keys(self) -> list:
        return [{"key_id": k, "purpose": v["purpose"], "created": v["created"]}
                for k, v in self.keys.items()]
