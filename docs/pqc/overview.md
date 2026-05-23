# Post-Quantum Cryptography

## Overview

Post-quantum cryptography (PQC) encompasses cryptographic algorithms resistant to attacks by quantum computers. This project integrates two NIST-selected PQC algorithms.

## Kyber KEM

Kyber is a lattice-based key encapsulation mechanism (KEM) for secure key exchange.

```python
from security.pqc.kem import PQCKEMFactory

kem = PQCKEMFactory.create_kem("Kyber768")
public_key, private_key = kem.generate_keypair()
ciphertext, shared_secret = kem.encapsulate(public_key)
recovered_secret = kem.decapsulate(private_key, ciphertext)
assert shared_secret == recovered_secret
```

## Dilithium Signatures

Dilithium is a lattice-based digital signature scheme.

```python
from security.pqc.signatures import PQCSignatureFactory

sig = PQCSignatureFactory.create_signature("Dilithium3")
public_key, private_key = sig.generate_keypair()
signature = sig.sign(private_key, b"message")
verified = sig.verify(public_key, b"message", signature)
assert verified
```

## Security Levels

| Algorithm | NIST Level | Public Key | Private Key | Security |
|-----------|------------|------------|-------------|----------|
| Kyber512  | 1          | 800 B      | 1632 B      | AES-128  |
| Kyber768  | 3          | 1184 B     | 2400 B      | AES-192  |
| Kyber1024 | 5          | 1568 B     | 3168 B      | AES-256  |
| Dilithium2 | 2         | 1312 B     | 2528 B      | SHA-256  |
| Dilithium3 | 3         | 1952 B     | 4000 B      | SHA-384  |
| Dilithium5 | 5         | 2592 B     | 4864 B      | SHA-512  |
