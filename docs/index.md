# Adult Creator Deplatforming Insurance

> Quantum-powered insurance risk scoring with on-chain proof of reserves.

## Features

- **Quantum Risk Scoring**: Variational Quantum Eigensolver (VQE), Quantum Approximate Optimization Algorithm (QAOA), and Quantum Monte Carlo methods for risk assessment
- **Post-Quantum Cryptography**: Kyber KEM for key exchange, Dilithium for digital signatures
- **OWASP Top 10 Security**: Automated security testing with Robot Framework
- **CI/CD Pipeline**: Automated builds, tests, releases, and package publishing

## Installation

```bash
pip install adult-creator-deplatforming-insurance
```

Or with quantum dependencies:

```bash
pip install "adult-creator-deplatforming-insurance[quantum]"
```

## Quick Start

```python
from quantum.circuits.risk_circuit import RiskScoringCircuit
from quantum.qiskit.risk_algorithms import QuantumRiskAlgorithms

# Create risk scoring circuit
risk_circuit = RiskScoringCircuit(num_qubits=4)
factors = [0.3, 0.7, 0.2, 0.5]
circuit = risk_circuit.create_risk_feature_circuit(factors)

# Run quantum risk algorithms
engine = QuantumRiskAlgorithms()
result = engine.ensemble_quantum_risk_scoring(factors)
print(f"Risk score: {result['risk_score']:.3f}")
```

## Project Structure

```
.
├── src/
│   ├── quantum/         # Quantum computing modules
│   │   ├── cuda_q/      # NVIDIA CUDA-Q integration
│   │   ├── qiskit/      # Qiskit quantum algorithms
│   │   ├── algorithms/  # Quantum algorithm implementations
│   │   ├── circuits/    # Quantum circuit definitions
│   │   └── utils/       # Quantum utility functions
│   └── security/        # Security modules
│       ├── pqc/         # Post-quantum cryptography
│       ├── keys/        # Key management
│       └── utils/       # Security utilities
├── tests/
│   ├── robotframework/  # Robot Framework test suites
│   │   ├── libraries/   # Custom test libraries
│   │   ├── resources/   # Shared keywords
│   │   └── testcases/   # Test case files
│   └── ...
├── .github/workflows/   # CI/CD pipeline definitions
├── docs/               # Documentation
└── scripts/            # Utility scripts
```

## Security

This project implements post-quantum cryptographic primitives for future-proof security:

- **Kyber KEM**: Lattice-based key encapsulation mechanism
- **Dilithium**: Lattice-based digital signatures
- **OWASP Top 10**: Regular automated security testing

## License

MIT
