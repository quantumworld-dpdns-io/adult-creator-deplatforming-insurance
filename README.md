# Adult Creator Deplatforming Insurance

> Quantum-powered insurance risk scoring with on-chain proof of reserves and post-quantum cryptography.

[![Test Suite](https://github.com/quantumworld-dpdns-io/adult-creator-deplatforming-insurance/actions/workflows/test.yml/badge.svg)](https://github.com/quantumworld-dpdns-io/adult-creator-deplatforming-insurance/actions/workflows/test.yml)
[![Release](https://github.com/quantumworld-dpdns-io/adult-creator-deplatforming-insurance/actions/workflows/release.yml/badge.svg)](https://github.com/quantumworld-dpdns-io/adult-creator-deplatforming-insurance/actions/workflows/release.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](pyproject.toml)
[![Quantum](https://img.shields.io/badge/quantum-computing-purple.svg)](src/quantum/)
[![PQC](https://img.shields.io/badge/PQC-Kyber%2FDilithium-orange.svg)](src/security/pqc/)

## Overview

This project provides a comprehensive risk scoring platform for adult creator deplatforming insurance, leveraging:

- **Quantum Computing**: VQE, QAOA, and Quantum Monte Carlo for advanced risk assessment
- **Post-Quantum Cryptography**: Kyber KEM and Dilithium signatures for future-proof security
- **OWASP Top 10**: Automated security validation with Robot Framework
- **CI/CD**: Full pipeline with automated builds, tests, releases, and packaging

## Features

### Quantum Risk Scoring
- **VQE**: Variational Quantum Eigensolver for finding minimum risk configurations
- **QAOA**: Quantum Approximate Optimization Algorithm for risk factor optimization
- **Quantum Monte Carlo**: Quantum-enhanced Monte Carlo simulation for risk modeling
- **Ensemble**: Combines multiple quantum algorithms for robust risk scoring

### Post-Quantum Cryptography
- **Kyber KEM**: Lattice-based key encapsulation for quantum-resistant key exchange
- **Dilithium Signatures**: Lattice-based digital signatures for document authentication
- **Key Management**: Full lifecycle management with rotation and storage

### Security Testing
- **Robot Framework**: Automated test execution with custom libraries
- **OWASP Top 10**: Comprehensive security vulnerability testing
- **CodeQL**: Continuous code security analysis
- **Dependency Scanning**: Regular vulnerability checks

### CI/CD Pipeline
- **Automated Builds**: Multi-Python version testing (3.10, 3.11, 3.12)
- **Security Scanning**: Bandit, Safety, and CodeQL integration
- **Release Management**: Semantic versioning with changelog generation
- **Package Publishing**: PyPI and GitHub Container Registry
- **Docker**: Multi-stage container builds with health checks

## Quick Start

```bash
pip install adult-creator-deplatforming-insurance

# Or with full quantum support
pip install "adult-creator-deplatforming-insurance[quantum]"
```

### Basic Usage

```python
from quantum.algorithms.ensemble_risk import EnsembleRiskScorer

# Initialize quantum risk engine
scorer = EnsembleRiskScorer(num_qubits=4)

# Calculate risk score for an adult creator
risk_factors = [0.3, 0.7, 0.2, 0.5, 0.4, 0.1]
result = scorer.score(risk_factors)
print(f"Risk Score: {result['risk_score']:.3f}")
```

### Post-Quantum Cryptography

```python
from security.pqc.kem import PQCKEMFactory
from security.pqc.signatures import PQCSignatureFactory

# Quantum-resistant key exchange
kem = PQCKEMFactory.create_kem("Kyber768")
public_key, private_key = kem.generate_keypair()
ciphertext, shared_secret = kem.encapsulate(public_key)
recovered = kem.decapsulate(private_key, ciphertext)

# Quantum-resistant digital signatures
sig = PQCSignatureFactory.create_signature("Dilithium3")
pk, sk = sig.generate_keypair()
signature = sig.sign(sk, b"Insurance policy document")
assert sig.verify(pk, b"Insurance policy document", signature)
```

## Project Structure

```
.
├── src/
│   ├── __init__.py
│   ├── main.py                    # Application entry point
│   ├── quantum/                   # Quantum computing modules
│   │   ├── __init__.py
│   │   ├── circuits/              # Quantum circuit definitions
│   │   │   ├── risk_circuit.py    # Risk scoring circuits
│   │   ├── algorithms/            # Quantum algorithms
│   │   │   ├── vqe_risk.py        # VQE optimizer
│   │   │   ├── qaoa_risk.py       # QAOA optimizer
│   │   │   ├── monte_carlo_risk.py# Quantum Monte Carlo
│   │   │   └── ensemble_risk.py   # Ensemble risk scorer
│   │   ├── qiskit/                # Qiskit integration
│   │   │   └── risk_algorithms.py # Qiskit algorithms
│   │   ├── cuda_q/                # CUDA-Q integration
│   │   │   └── backend.py         # GPU backend
│   │   ├── cli/                   # CLI interface
│   │   └── utils/                 # Quantum utilities
│   │       └── entropy.py         # Entropy generation
│   └── security/                  # Security modules
│       ├── pqc/                   # Post-quantum cryptography
│       │   ├── kem.py             # Kyber KEM
│       │   └── signatures.py      # Dilithium signatures
│       ├── keys/                  # Key management
│       └── cli/                   # CLI interface
├── tests/                         # Test suites
│   ├── unit/                      # Unit tests (46+ tests)
│   ├── integration/               # Integration tests
│   └── robotframework/            # Robot Framework tests
│       ├── libraries/             # Custom test libraries
│       ├── resources/             # Shared keywords
│       └── testcases/             # OWASP Top 10 test cases
├── .github/workflows/             # CI/CD pipelines
│   ├── test.yml                   # Test workflow
│   ├── release.yml                # Release workflow
│   └── package.yml                # Package build workflow
├── docs/                          # Documentation
├── Dockerfile                     # Container build
├── pyproject.toml                 # Package configuration
└── scripts/                       # Utility scripts
    ├── auto_commit.sh             # Auto-commit agent
    └── run_tests.py               # Test runner
```

## Testing

```bash
# Run all tests
python scripts/run_tests.py --all

# Run unit tests only
pytest tests/unit/ -v

# Run OWASP security tests
robot tests/robotframework/testcases/owasp_top10.robot

# Run integration tests
pytest tests/integration/ -v
```

### Test Results

```
✓ All 46 tests passing (41 unit + 5 integration)
✓ Robot Framework OWASP Top 10 test suite
✓ Quantum module import checks
✓ PQC key exchange and signature verification
```

## CI/CD Pipelines

### Test Workflow
- Multi-version Python testing (3.10, 3.11, 3.12)
- Quantum module import verification
- OWASP Top 10 security testing with Robot Framework
- Code quality checks (flake8, black, isort, mypy)
- Dependency security scanning

### Release Workflow
- Automated changelog generation
- Multi-architecture package building
- GPG signature signing
- CodeQL security scanning
- GitHub Release creation
- PyPI publishing
- Docker image build and push

### Package Workflow
- Python wheel and source distribution building
- Docker container image building
- Documentation generation with MkDocs
- Package installation testing

## Security

This project implements comprehensive security measures:

1. **Post-Quantum Cryptography**
   - Kyber KEM for quantum-resistant key exchange (NIST Level 1-5)
   - Dilithium for quantum-resistant digital signatures
   - Automatic key rotation and management

2. **OWASP Top 10 Coverage**
   - A01: Broken Access Control
   - A02: Cryptographic Failures
   - A03: Injection (SQL, XSS, Command)
   - A04: Insecure Design
   - A05: Security Misconfiguration
   - A06: Vulnerable Components
   - A07: Authentication Failures
   - A08: Integrity Failures
   - A09: Logging Failures
   - A10: Server-Side Request Forgery

3. **Continuous Security**
   - Pre-commit hooks with security checks
   - Automated dependency scanning
   - CodeQL analysis in CI/CD
   - Regular security updates via Dependabot

## Quantum Computing Integration

### Frameworks

| Framework | Purpose | Status |
|-----------|---------|--------|
| **NVIDIA CUDA-Q** | GPU-accelerated quantum circuit simulation | Ready |
| **IBM Qiskit** | Quantum circuit construction and execution | Ready |
| **Custom Algorithms** | VQE, QAOA, Quantum Monte Carlo | Tested |

### Algorithms

| Algorithm | Application | Complexity |
|-----------|------------|------------|
| VQE | Minimum risk configuration | O(2^n) |
| QAOA | Risk factor optimization | O(p*n) |
| Quantum Monte Carlo | Risk simulation | O(√N) |
| Ensemble | Combined risk scoring | O(1) |

## License

MIT License - see [LICENSE](LICENSE) for details.

## Citation

If you use this software in your research, please cite:

```bibtex
@software{quantumworld2026adult,
  title = {Adult Creator Deplatforming Insurance},
  author = {{quantumworld-dpdns-io}},
  year = {2026},
  url = {https://github.com/quantumworld-dpdns-io/adult-creator-deplatforming-insurance}
}
```

<!-- commit-004: add initial README with project overview -->
