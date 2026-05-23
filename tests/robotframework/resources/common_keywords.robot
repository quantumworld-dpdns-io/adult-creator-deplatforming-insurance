*** Settings ***
Documentation     Common keywords for Robot Framework test suites

Library           Collections
Library           String
Library           OperatingSystem
Library           Process

*** Keywords ***
Setup Test Environment
    [Documentation]    Initialize test environment with required variables
    ${project_root}=    Get Environment Variable    PROJECT_ROOT    ${CURDIR}/../..
    Set Suite Variable    ${PROJECT_ROOT}    ${project_root}
    Set Suite Variable    ${QUANTUM_MODULE}    ${PROJECT_ROOT}/src/quantum
    Set Suite Variable    ${SECURITY_MODULE}    ${PROJECT_ROOT}/src/security
    Log    Test environment set up successfully

Teardown Test Environment
    [Documentation]    Clean up after test execution
    Log    Test environment torn down successfully

Assert Risk Score In Range
    [Arguments]    ${score}    ${min}=0.0    ${max}=1.0
    [Documentation]    Assert that risk score is within valid range
    ${score_float}=    Convert To Number    ${score}
    Should Be True    ${score_float} >= ${min}    Score ${score_float} is below min ${min}
    Should Be True    ${score_float} <= ${max}    Score ${score_float} is above max ${max}

Assert Quantum State Valid
    [Arguments]    ${state_vector}
    [Documentation]    Assert that a quantum state vector is valid
    ${length}=    Get Length    ${state_vector}
    Should Be True    ${length} > 0    State vector cannot be empty
    # Check normalization (sum of squared magnitudes = 1)
    ${norm}=    Evaluate    sum(abs(x)**2 for x in ${state_vector})
    Should Be True    abs(${norm} - 1.0) < 0.001    State vector not normalized: ${norm}

Create Random Risk Factors
    [Arguments]    ${count}=4
    [Documentation]    Generate random risk factor values for testing
    ${factors}=    Evaluate    [random.random() for _ in range(${count})]    random
    [Return]    ${factors}

Verify File Contains
    [Arguments]    ${file_path}    ${expected_text}
    [Documentation]    Verify that a file contains expected text
    ${content}=    Get File    ${file_path}
    Should Contain    ${content}    ${expected_text}
