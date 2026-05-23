*** Settings ***
Documentation     Root test suite for adult-creator-deplatforming-insurance
...               Robot Framework test suite for quantum computing integration
...               and OWASP Top 10 security validation.

Library           Collections
Library           String
Library           OperatingSystem
Resource          resources/common_keywords.robot
Resource          resources/quantum_keywords.robot
Resource          resources/security_keywords.robot

# commit-024: create tests/robotframework/ test directory

# commit-087: run robot framework tests in CI
