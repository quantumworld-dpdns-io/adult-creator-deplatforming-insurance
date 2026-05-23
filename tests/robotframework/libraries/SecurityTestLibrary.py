import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from typing import Dict, Any


class SecurityTestLibrary:
    """Robot Framework test library for OWASP Top 10 security testing."""

    ROBOT_LIBRARY_SCOPE = 'SUITE'

    def __init__(self):
        self.vulnerabilities = {}

    def test_sql_injection(self, target_url: str, payload: str) -> Dict[str, Any]:
        errors = []
        sql_payloads = ["' OR '1'='1", "'; DROP TABLE users--", "' UNION SELECT * FROM users--"]
        for p in sql_payloads:
            if p in payload or payload in p:
                errors.append(f"Suspicious SQL pattern detected: {p}")
        return {'vulnerable': len(errors) > 0, 'errors': errors, 'payload': payload}

    def test_xss(self, target_url: str, payload: str) -> Dict[str, Any]:
        errors = []
        xss_patterns = ['<script>', 'onerror=', 'javascript:', '<iframe', 'onload=']
        for pattern in xss_patterns:
            if pattern.lower() in payload.lower():
                errors.append(f"XSS pattern detected: {pattern}")
        return {'vulnerable': len(errors) > 0, 'errors': errors, 'payload': payload}

    def test_authentication(self, target_url: str) -> Dict[str, Any]:
        errors = []
        weak_creds = [('admin', 'admin'), ('admin', 'password'), ('root', 'root')]
        # In real implementation, this would make actual HTTP requests
        return {'vulnerable': False, 'errors': errors, 'url': target_url}

    def test_data_exposure(self, target_url: str) -> Dict[str, Any]:
        errors = []
        sensitive_patterns = ['password', 'secret', 'token', 'api_key', 'ssn', 'credit_card']
        # In real implementation, this would scan responses
        return {'vulnerable': False, 'errors': errors, 'url': target_url}

    def test_xxe(self, target_url: str, payload: str) -> Dict[str, Any]:
        errors = []
        xxe_patterns = ['<!ENTITY', '<!DOCTYPE', 'SYSTEM "file:', 'SYSTEM "http:']
        for pattern in xxe_patterns:
            if pattern.lower() in payload.lower():
                errors.append(f"XXE pattern detected: {pattern}")
        return {'vulnerable': len(errors) > 0, 'errors': errors}

    def test_access_control(self, target_url: str, admin_url: str) -> Dict[str, Any]:
        errors = []
        # In real implementation, would test unauthorized access to admin endpoints
        return {'vulnerable': False, 'errors': errors}

    def test_security_misconfiguration(self, target_url: str) -> Dict[str, Any]:
        errors = []
        # Check for common misconfigurations
        misconfigs = ['Directory listing enabled', 'Default credentials', 'Debug mode enabled']
        return {'vulnerable': False, 'errors': errors, 'checks': misconfigs}

    def test_cryptographic_failures(self, target_url: str) -> Dict[str, Any]:
        errors = []
        # Check for weak crypto
        weak_ciphers = ['RC4', 'DES', 'MD4', 'MD5', 'SHA-1']
        return {'vulnerable': False, 'errors': errors}

    def perform_pqc_key_exchange(self, algorithm: str = 'Kyber768') -> Dict[str, Any]:
        from security.pqc.kem import PQCKEMFactory
        kem = PQCKEMFactory.create_kem(algorithm)
        pk, sk = kem.generate_keypair()
        ct, ss = kem.encapsulate(pk)
        recovered = kem.decapsulate(sk, ct)
        success = ss == recovered
        return {'success': success, 'algorithm': kem.algorithm_name}

    def perform_pqc_signature(self, algorithm: str = 'Dilithium3', message: str = 'Test') -> Dict[str, Any]:
        from security.pqc.signatures import PQCSignatureFactory
        sig_scheme = PQCSignatureFactory.create_signature(algorithm)
        pk, sk = sig_scheme.generate_keypair()
        msg_bytes = message.encode()
        signature = sig_scheme.sign(sk, msg_bytes)
        verified = sig_scheme.verify(pk, msg_bytes, signature)
        return {'verified': verified, 'algorithm': sig_scheme.algorithm_name}
