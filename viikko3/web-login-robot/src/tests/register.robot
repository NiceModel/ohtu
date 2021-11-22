*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  jonne
    Set Password  jonne123
    Set Password Confirmation  jonne123
    Submit Registration
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  jo
    Set Password  jonne123
    Set Password Confirmation  jonne123
    Submit Registration
    Register Should Fail With Message  Username must be at least 3 characters long 

Register With Valid Username And Too Short Password
    Set Username  jonne
    Set Password  jonne1
    Set Password Confirmation  jonne1
    Submit Registration
    Register Should Fail With Message  Password must be at least 8 characters long

Register With Nonmatching Password And Password Confirmation
    Set Username  jonne
    Set Password  jonne123
    Set Password Confirmation  jonne999
    Submit Registration
    Register Should Fail With Message  Password and password confirmation must match

Login After Successful Registration
    Set Username  jonne
    Set Password  jonne123
    Set Password Confirmation  jonne123
    Submit Registration
    Go To Login Page
    Set Username  jonne
    Set Password  jonne123
    Submit Credentials
    Login Should Succeed
    

Login After Failed Registration
    Set Username  jo
    Set Password  jonne123
    Set Password Confirmation  jonne123
    Submit Registration
    Go To Login Page
    Set Username  jo
    Set Password  jonne123
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Registration
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}