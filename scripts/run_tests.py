"""Comprehensive test runner for adult-creator-deplatforming-insurance."""

import sys
import os
import subprocess
import argparse
from datetime import datetime

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

def run_unit_tests(verbose: bool = True):
    print("\n" + "="*60)
    print("RUNNING UNIT TESTS")
    print("="*60)
    cmd = [sys.executable, "-m", "pytest", "tests/unit/", "-v", "--tb=short"]
    if verbose:
        cmd.append("--tb=long")
    result = subprocess.run(cmd, capture_output=False)
    return result.returncode == 0

def run_integration_tests():
    print("\n" + "="*60)
    print("RUNNING INTEGRATION TESTS")
    print("="*60)
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "tests/integration/", "-v", "--tb=short"],
        capture_output=False
    )
    return result.returncode == 0

def run_robot_tests():
    print("\n" + "="*60)
    print("RUNNING ROBOT FRAMEWORK TESTS")
    print("="*60)
    result = subprocess.run(
        ["robot", "--outputdir", "robot-reports", "tests/robotframework/"],
        capture_output=False
    )
    return result.returncode == 0

def run_quantum_module_check():
    print("\n" + "="*60)
    print("RUNNING QUANTUM MODULE CHECK")
    print("="*60)
    try:
        from quantum.circuits.risk_circuit import RiskScoringCircuit
        from quantum.algorithms.ensemble_risk import EnsembleRiskScorer
        from security.pqc.kem import PQCKEMFactory
        from security.pqc.signatures import PQCSignatureFactory
        
        print("✓ Quantum modules loaded successfully")
        circuit = RiskScoringCircuit(4)
        print(f"✓ RiskScoringCircuit: {circuit.num_qubits} qubits")
        scorer = EnsembleRiskScorer(4)
        result = scorer.score([0.3, 0.5, 0.7, 0.2])
        print(f"✓ Ensemble risk score: {result['risk_score']:.3f}")
        kem = PQCKEMFactory.create_kem("Kyber768")
        pk, sk = kem.generate_keypair()
        print(f"✓ PQC KEM keypair: PK={len(pk)}B, SK={len(sk)}B")
        return True
    except Exception as e:
        print(f"✗ Quantum module check failed: {e}")
        return False

def run_owasp_checks():
    print("\n" + "="*60)
    print("RUNNING OWASP SECURITY CHECKS")
    print("="*60)
    try:
        from security.pqc.kem import PQCKEMFactory
        from security.pqc.signatures import PQCSignatureFactory
        
        for level in ["Kyber512", "Kyber768", "Kyber1024"]:
            kem = PQCKEMFactory.create_kem(level)
            pk, sk = kem.generate_keypair()
            ct, ss1 = kem.encapsulate(pk)
            ss2 = kem.decapsulate(sk, ct)
            assert ss1 == ss2, f"KEM failed at {level}"
            print(f"✓ {level} KEM: OK")
        
        for level in ["Dilithium2", "Dilithium3", "Dilithium5"]:
            sig = PQCSignatureFactory.create_signature(level)
            pk, sk = sig.generate_keypair()
            msg = b"Test message for OWASP verification"
            signature = sig.sign(sk, msg)
            assert sig.verify(pk, msg, signature), f"Signature failed at {level}"
            print(f"✓ {level} Signatures: OK")
        
        print("✓ All OWASP security checks passed")
        return True
    except Exception as e:
        print(f"✗ OWASP check failed: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Comprehensive test runner")
    parser.add_argument("--unit", action="store_true", help="Run unit tests")
    parser.add_argument("--integration", action="store_true", help="Run integration tests")
    parser.add_argument("--robot", action="store_true", help="Run Robot Framework tests")
    parser.add_argument("--quantum", action="store_true", help="Run quantum module check")
    parser.add_argument("--owasp", action="store_true", help="Run OWASP security checks")
    parser.add_argument("--all", action="store_true", help="Run all tests")
    parser.add_argument("--ci", action="store_true", help="CI mode (exit on first failure)")
    args = parser.parse_args()
    
    if not any([args.unit, args.integration, args.robot, args.quantum, args.owasp, args.all]):
        args.all = True
    
    start_time = datetime.now()
    results = {}
    
    if args.all or args.unit:
        results['unit'] = run_unit_tests()
    if args.all or args.integration:
        results['integration'] = run_integration_tests()
    if args.all or args.quantum:
        results['quantum'] = run_quantum_module_check()
    if args.all or args.owasp:
        results['owasp'] = run_owasp_checks()
    if args.all or args.robot:
        results['robot'] = run_robot_tests()
    
    elapsed = (datetime.now() - start_time).total_seconds()
    
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    all_passed = True
    for name, passed in results.items():
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"  {name.upper():15s}: {status}")
        if not passed:
            all_passed = False
    print(f"\nElapsed time: {elapsed:.2f}s")
    print(f"Overall: {'ALL TESTS PASSED' if all_passed else 'SOME TESTS FAILED'}")
    
    if args.ci and not all_passed:
        sys.exit(1)

if __name__ == "__main__":
    main()
