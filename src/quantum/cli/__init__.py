import sys
from typing import List

def main(args: List[str] = None):
    if args is None:
        args = sys.argv[1:]
    print("Quantum Risk CLI v1.0.0")
    print("=" * 40)
    print("Commands: risk-score, keygen, verify, entropy")
    if not args or args[0] == "risk-score":
        from ..algorithms.ensemble_risk import EnsembleRiskScorer
        factors = [0.3, 0.7, 0.2, 0.5, 0.4, 0.1]
        scorer = EnsembleRiskScorer(4)
        result = scorer.score(factors)
        print(f"Risk Score: {result['risk_score']:.3f}")
        print(f"Algorithm: {result['algorithm']}")
        for name, r in result['individual'].items():
            print(f"  {name}: {r['risk_score']:.3f}")
    elif args[0] == "keygen":
        from security.pqc.kem import PQCKEMFactory
        kem = PQCKEMFactory.create_kem(args[1] if len(args) > 1 else "Kyber768")
        pk, sk = kem.generate_keypair()
        print(f"Generated {kem.algorithm_name} keypair")
        print(f"Public key: {len(pk)} bytes")
        print(f"Private key: {len(sk)} bytes")
    elif args[0] == "entropy":
        from ..circuits.risk_circuit import RiskScoringCircuit
        import os
        entropy = os.urandom(32)
        print(f"Entropy: {entropy.hex()}")

if __name__ == "__main__":
    main()
