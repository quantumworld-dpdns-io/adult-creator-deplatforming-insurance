*** Settings ***
Documentation     Keywords for quantum computing operations testing

Library           Collections
Library           String
Library           Process
Library           ../libraries/QuantumTestLibrary.py

*** Keywords ***
Initialize Quantum Risk Engine
    [Documentation]    Initialize the quantum risk scoring engine
    ${engine}=    Create Quantum Risk Engine    4
    Set Suite Variable    ${QUANTUM_ENGINE}    ${engine}
    [Return]    ${engine}

Calculate Quantum Risk Score
    [Arguments]    @{risk_factors}
    [Documentation]    Calculate risk score using quantum algorithms
    ${result}=    Calculate Risk Score    ${QUANTUM_ENGINE}    ${risk_factors}
    [Return]    ${result}

Verify Quantum Circuit Valid
    [Arguments]    ${circuit}
    [Documentation]    Verify quantum circuit structure
    Dictionary Should Contain Key    ${circuit}    num_qubits
    Dictionary Should Contain Key    ${circuit}    gates
    ${num_qubits}=    Get From Dictionary    ${circuit}    num_qubits
    Should Be True    ${num_qubits} > 0    Circuit must have at least 1 qubit

Run VQE Risk Assessment
    [Arguments]    @{risk_factors}
    [Documentation]    Run VQE-based risk assessment
    ${result}=    Run VQE Algorithm    ${QUANTUM_ENGINE}    ${risk_factors}
    [Return]    ${result}

Run QAOA Risk Assessment
    [Arguments]    @{risk_factors}
    [Documentation]    Run QAOA-based risk assessment
    ${result}=    Run QAOA Algorithm    ${QUANTUM_ENGINE}    ${risk_factors}
    [Return]    ${result}

Run Quantum Monte Carlo Simulation
    [Arguments]    @{risk_factors}
    [Documentation]    Run quantum Monte Carlo risk simulation
    ${result}=    Run Quantum Monte Carlo    ${QUANTUM_ENGINE}    ${risk_factors}
    [Return]    ${result}

Validate Post-Quantum Keys
    [Arguments]    ${public_key}    ${private_key}
    [Documentation]    Validate PQC keypair
    ${pk_len}=    Get Length    ${public_key}
    ${sk_len}=    Get Length    ${private_key}
    Should Be True    ${pk_len} > 0    Public key cannot be empty
    Should Be True    ${sk_len} > 0    Private key cannot be empty

Test Quantum Entropy
    [Documentation]    Test quantum entropy generation
    ${entropy}=    Generate Quantum Entropy    32
    ${entropy_len}=    Get Length    ${entropy}
    Should Be Equal As Integers    ${entropy_len}    32
    [Return]    ${entropy}
