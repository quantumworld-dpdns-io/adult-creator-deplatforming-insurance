from .circuits.risk_circuit import RiskScoringCircuit, create_simple_risk_circuit
from .algorithms.ensemble_risk import EnsembleRiskScorer
from .utils.entropy import QuantumEntropyGenerator

try:
    from .qiskit.risk_algorithms import QuantumRiskAlgorithms
except ImportError:
    class QuantumRiskAlgorithms:
        def __init__(self, *args, **kwargs):
            raise ImportError("Qiskit is not installed. Run: pip install qiskit")

try:
    from .cuda_q.backend import CUDABackend
except ImportError:
    class CUDABackend:
        def __init__(self, *args, **kwargs):
            raise ImportError("CUDA-Q is not installed.")

__all__ = [
    'RiskScoringCircuit', 'create_simple_risk_circuit',
    'EnsembleRiskScorer', 'QuantumRiskAlgorithms',
    'CUDABackend', 'QuantumEntropyGenerator',
]
