"""Security CLI module."""

import sys
from typing import List


def keygen_main(args: List[str] = None):
    if args is None:
        args = sys.argv[1:]
    from ..pqc.kem import PQCKEMFactory
    from ..pqc.signatures import PQCSignatureFactory

    algo = args[0] if args else "all"
    print("Post-Quantum Cryptography Key Generator")
    print("=" * 45)

    if algo in ("all", "kem"):
        for level in ["Kyber512", "Kyber768", "Kyber1024"]:
            kem = PQCKEMFactory.create_kem(level)
            pk, sk = kem.generate_keypair()
            print(f"{kem.algorithm_name}: PK={len(pk)}B, SK={len(sk)}B")

    if algo in ("all", "sig"):
        for level in ["Dilithium2", "Dilithium3", "Dilithium5"]:
            sig = PQCSignatureFactory.create_signature(level)
            pk, sk = sig.generate_keypair()
            print(f"{sig.algorithm_name}: PK={len(pk)}B, SK={len(sk)}B")


def main():
    keygen_main(sys.argv[1:])


if __name__ == "__main__":
    main()
