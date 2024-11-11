*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kal
    Set Password  salasan4
    Set Password Confirmation    salasan4
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username    it
    Set Password    salasana3
    Set Password Confirmation    salasana3
    Submit Credentials
    Register Should Fail With Message    Username is too short

Register With Valid Username And Too Short Password
    Set Username    kallekalle
    Set Password    1234567
    Set Password Confirmation    1234567
    Submit Credentials
    Register Should Fail With Message    Password is too short

Register With Valid Username And Invalid Password
    Set Username    kallekalle
    Set Password    salasana
    Set Password Confirmation    salasana
    Submit Credentials
    Register Should Fail With Message    Password must contain at least 1 number

Register With Nonmatching Password And Password Confirmation
    Set Username    kallekalle
    Set Password    salasana
    Set Password Confirmation    ei
    Submit Credentials
    Register Should Fail With Message    Passwords do not match!

Register With Username That Is Already In Use
    Set Username    kalle
    Set Password    salasana3
    Set Password Confirmation    salasana3
    Submit Credentials
    Register Should Fail With Message    User with username kalle already exists

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password    password_confirmation    ${password_confirmation}