"""Pytest configuration and shared fixtures."""

import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


@pytest.fixture
def risk_factors():
    return [0.3, 0.7, 0.2, 0.5, 0.4, 0.1]


@pytest.fixture
def high_risk_factors():
    return [0.9, 0.85, 0.95, 0.8]


@pytest.fixture
def low_risk_factors():
    return [0.1, 0.15, 0.05, 0.2]


@pytest.fixture
def sample_document():
    return b"Insurance policy document for adult creator risk assessment v2026"


@pytest.fixture
def quantum_engine():
    from quantum.algorithms.ensemble_risk import EnsembleRiskScorer
    return EnsembleRiskScorer(num_qubits=4)


@pytest.fixture
def key_manager():
    from security.keys.key_manager import QuantumKeyManager
    km = QuantumKeyManager()
    km.generate_keypair("test-key", "testing")
    return km


@pytest.fixture
def vqe_optimizer():
    from quantum.algorithms import VQERiskOptimizer
    return VQERiskOptimizer(4)


@pytest.fixture
def qaoa_optimizer():
    from quantum.algorithms import QAOARiskOptimizer
    return QAOARiskOptimizer(4)


@pytest.fixture
def qmc_simulator():
    from quantum.algorithms import QuantumMonteCarloRisk
    return QuantumMonteCarloRisk(4)
