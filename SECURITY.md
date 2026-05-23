# Security Policy for Adult Creator Deplatforming Insurance

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

We take security seriously. If you discover a security vulnerability, please:

1. **Do NOT** open a public issue
2. Email security@quantumworld.io
3. Include a detailed description and reproduction steps
4. Allow 48 hours for initial response

## Security Features

- **Post-Quantum Cryptography**: Kyber KEM and Dilithium signatures for quantum-resistant security
- **OWASP Top 10**: Automated security testing in CI/CD pipeline
- **CodeQL Analysis**: Continuous code security scanning
- **Dependency Scanning**: Regular vulnerability scanning of dependencies
- **Pre-commit Hooks**: Security checks before code is committed

## Security Testing

```bash
# Run OWASP security tests
robot tests/robotframework/testcases/owasp_top10.robot

# Run security scan
bandit -r src/

# Check dependencies
safety check -r requirements-quantum.txt
```

<!-- commit-051: add SECURITY.md with vulnerability reporting -->
