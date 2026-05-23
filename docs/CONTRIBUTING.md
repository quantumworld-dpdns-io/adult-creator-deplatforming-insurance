# Contributing to Adult Creator Deplatforming Insurance

## Development Setup

```bash
git clone https://github.com/quantumworld-dpdns-io/adult-creator-deplatforming-insurance.git
cd adult-creator-deplatforming-insurance
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pre-commit install
```

## Quantum Development

For quantum computing features:
```bash
pip install -e ".[quantum]"
```

For NVIDIA CUDA-Q support:
```bash
pip install cudaq
```

## Running Tests

```bash
# Full test suite
python scripts/run_tests.py --all

# Specific test types
pytest tests/unit/ -v
pytest tests/integration/ -v
robot tests/robotframework/testcases/owasp_top10.robot
```

## Code Style

- Line length: 120 characters
- Formatter: Black
- Import sorting: isort
- Type hints required for all public APIs

## Pre-commit Hooks

```bash
pre-commit install
pre-commit run --all-files
```

## Commit Guidelines

Each commit should represent one atomic change. Follow conventional commits:

```
feat: add quantum risk scoring circuit
fix: correct PQC key encapsulation
test: add OWASP A01 test case
docs: update quantum algorithm documentation
chore: update dependencies
```

## Pull Request Process

1. Create feature branch from `dev`
2. Add tests for new functionality
3. Run full test suite
4. Update documentation
5. Create PR with description of changes

## Release Process

Releases follow semantic versioning (MAJOR.MINOR.PATCH):

1. Merge to `main`
2. Tag with version `v1.x.x`
3. CI/CD pipeline builds and publishes packages
4. Changelog auto-generated from commits

<!-- commit-054: create contributing.md developer guide -->

# commit-075: add CONTRIBUTORS.md
