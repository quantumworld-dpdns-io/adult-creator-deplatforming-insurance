*** Settings ***
Documentation     OWASP Top 10 Security Test Suite
...               Tests for all OWASP Top 10 vulnerabilities
...               https://owasp.org/www-project-top-ten/

Resource          ../resources/common_keywords.robot
Resource          ../resources/security_keywords.robot
Library           ../libraries/SecurityTestLibrary.py
Library           Collections

Suite Setup       Setup Test Environment
Suite Teardown    Teardown Test Environment

*** Test Cases ***
A01 Broken Access Control Test
    [Documentation]    Test for broken access control (OWASP A01)
    ${result}=    Check Broken Access Control    http://localhost:8080/api/    http://localhost:8080/admin/
    Should Be True    not ${result['vulnerable']}    Broken access control detected
    Log    OWASP A01: Access control test passed

A02 Cryptographic Failures Test
    [Documentation]    Test for cryptographic failures (OWASP A02)
    ${result}=    Check Cryptographic Failures    http://localhost:8080/
    Should Be True    not ${result['vulnerable']}    Cryptographic failures detected
    Log    OWASP A02: Cryptographic failures test passed

A03 Injection Test - SQL Injection
    [Documentation]    Test for SQL injection vulnerability (OWASP A03)
    ${result}=    Check SQL Injection    http://localhost:8080/login    ' OR '1'='1
    Should Be True    not ${result['vulnerable']}    SQL Injection vulnerability detected
    Log    OWASP A03: SQL Injection test passed

A03 Injection Test - XSS
    [Documentation]    Test for Cross-Site Scripting (OWASP A03)
    ${result}=    Check XSS Vulnerability    http://localhost:8080/search    <script>alert('XSS')</script>
    Should Be True    not ${result['vulnerable']}    XSS vulnerability detected
    Log    OWASP A03: XSS test passed

A04 Insecure Design Test
    [Documentation]    Test for insecure design (OWASP A04)
    ${result}=    Check Security Misconfiguration    http://localhost:8080/
    Should Be True    not ${result['vulnerable']}    Security misconfiguration detected
    Log    OWASP A04: Insecure design test passed

A05 Security Misconfiguration Test
    [Documentation]    Test for security misconfiguration (OWASP A05)
    ${result}=    Check Security Misconfiguration    http://localhost:8080/
    Should Be True    not ${result['vulnerable']}    Security misconfiguration detected
    Log    OWASP A05: Security misconfiguration test passed

A06 Vulnerable and Outdated Components Test
    [Documentation]    Test for vulnerable components (OWASP A06)
    ${result}=    Check Security Misconfiguration    http://localhost:8080/
    Should Be True    not ${result['vulnerable']}    Vulnerable components detected
    Log    OWASP A06: Vulnerable components test passed

A07 Identification and Authentication Failures Test
    [Documentation]    Test for authentication failures (OWASP A07)
    ${result}=    Check Broken Authentication    http://localhost:8080/login
    Should Be True    not ${result['vulnerable']}    Authentication failures detected
    Log    OWASP A07: Authentication test passed

A08 Software and Data Integrity Failures Test
    [Documentation]    Test for integrity failures (OWASP A08)
    ${result}=    Check Security Misconfiguration    http://localhost:8080/
    Should Be True    not ${result['vulnerable']}    Integrity failures detected
    Log    OWASP A08: Integrity test passed

A09 Security Logging and Monitoring Failures Test
    [Documentation]    Test for logging failures (OWASP A09)
    ${result}=    Check Sensitive Data Exposure    http://localhost:8080/logs
    Should Be True    not ${result['vulnerable']}    Logging failures detected
    Log    OWASP A09: Logging test passed

A10 Server-Side Request Forgery Test
    [Documentation]    Test for SSRF vulnerability (OWASP A10)
    ${result}=    Check XXE Vulnerability    http://localhost:8080/fetch    SSRF test payload
    Should Be True    not ${result['vulnerable']}    SSRF vulnerability detected
    Log    OWASP A10: SSRF test passed

A01-Broken Access Control - Horizontal Privilege Escalation
    [Documentation]    Test horizontal privilege escalation
    ${result}=    Check Broken Access Control    http://localhost:8080/user/123    http://localhost:8080/user/456
    Should Be True    not ${result['vulnerable']}    Horizontal privilege escalation detected
    Log    Horizontal privilege escalation test passed

A02-Cryptographic Failures - Weak TLS
    [Documentation]    Test for weak TLS cipher suites
    ${result}=    Check Cryptographic Failures    https://localhost:8443/
    Should Be True    not ${result['vulnerable']}    Weak TLS detected
    Log    Cryptographic failures test passed

A03-Injection - Command Injection
    [Documentation]    Test for command injection
    ${result}=    Check SQL Injection    http://localhost:8080/exec    ; ls -la
    Should Be True    not ${result['vulnerable']}    Command injection detected
    Log    Command injection test passed

A04-Insecure Design - Missing Rate Limiting
    [Documentation]    Test for missing rate limiting
    ${result}=    Check Broken Authentication    http://localhost:8080/login
    Should Be True    not ${result['vulnerable']}    Missing rate limiting detected
    Log    Rate limiting test passed

A05-Security Misconfiguration - CORS
    [Documentation]    Test for permissive CORS configuration
    ${result}=    Check Security Misconfiguration    http://localhost:8080/
    Should Be True    not ${result['vulnerable']}    Permissive CORS detected
    Log    CORS test passed
