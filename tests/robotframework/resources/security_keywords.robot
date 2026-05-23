*** Settings ***
Documentation     Keywords for OWASP Top 10 security testing

Library           Collections
Library           String
Library           RequestsLibrary
Library           ../libraries/SecurityTestLibrary.py

*** Keywords ***
Check SQL Injection
    [Arguments]    ${target_url}    ${payload}
    [Documentation]    Test for SQL injection vulnerability
    ${result}=    Test SQL Injection    ${target_url}    ${payload}
    Should Not Be True    ${result['vulnerable']}    SQL Injection vulnerability found!
    [Return]    ${result}

Check XSS Vulnerability
    [Arguments]    ${target_url}    ${payload}
    [Documentation]    Test for Cross-Site Scripting vulnerability
    ${result}=    Test XSS    ${target_url}    ${payload}
    Should Not Be True    ${result['vulnerable']}    XSS vulnerability found!
    [Return]    ${result}

Check Broken Authentication
    [Arguments]    ${target_url}
    [Documentation]    Test for broken authentication mechanisms
    ${result}=    Test Authentication    ${target_url}
    Should Not Be True    ${result['vulnerable']}    Broken authentication found!
    [Return]    ${result}

Check Sensitive Data Exposure
    [Arguments]    ${target_url}
    [Documentation]    Test for sensitive data exposure
    ${result}=    Test Data Exposure    ${target_url}
    Should Not Be True    ${result['vulnerable']}    Sensitive data exposure found!
    [Return]    ${result}

Check XML External Entities
    [Arguments]    ${target_url}    ${payload}
    [Documentation]    Test for XXE vulnerability
    ${result}=    Test XXE    ${target_url}    ${payload}
    Should Not Be True    ${result['vulnerable']}    XXE vulnerability found!
    [Return]    ${result}

Check Broken Access Control
    [Arguments]    ${target_url}    ${admin_url}
    [Documentation]    Test for broken access control
    ${result}=    Test Access Control    ${target_url}    ${admin_url}
    Should Not Be True    ${result['vulnerable']}    Broken access control found!
    [Return]    ${result}

Check Security Misconfiguration
    [Arguments]    ${target_url}
    [Documentation]    Test for security misconfigurations
    ${result}=    Test Security Misconfiguration    ${target_url}
    Should Not Be True    ${result['vulnerable']}    Security misconfiguration found!
    [Return]    ${result}

Check Cryptographic Failures
    [Arguments]    ${target_url}
    [Documentation]    Test for cryptographic failures
    ${result}=    Test Cryptographic Failures    ${target_url}
    Should Not Be True    ${result['vulnerable']}    Cryptographic failures found!
    [Return]    ${result}

Test PQC Key Exchange
    [Arguments]    ${algorithm}=Kyber768
    [Documentation]    Test post-quantum key exchange
    ${result}=    Perform PQC Key Exchange    ${algorithm}
    Should Be True    ${result['success']}    PQC key exchange failed
    [Return]    ${result}

Test PQC Signatures
    [Arguments]    ${algorithm}=Dilithium3    ${message}=Test message
    [Documentation]    Test post-quantum digital signatures
    ${result}=    Perform PQC Signature    ${algorithm}    ${message}
    Should Be True    ${result['verified']}    PQC signature verification failed
    [Return]    ${result}
