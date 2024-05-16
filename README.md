# captchakiller-python

## Installation
`pip install captchakiller-python`

## Usage
### Import the CaptchaKiller class
`from captchakiller import CaptchaKiller`

### Set your credentials
`captcha_killer = CaptchaKiller("API_KEY") # Optionally add partner id and/or timeout`

### Use the captcha_killer object
#### Get balance
```
response = captcha_killer.getbalance()
if response['success']:
    print("Balance: " + response["balance"])
else:
    print("Error: " + str(response["errorId"]) + " - " + response["error"])
```
#### Solve captcha
```
response = captcha_killer.recaptcha_v2("v2key", "site")
if response['success']:
    print("Captcha solved: " + response["result"])
else:
    print("Error: " + str(response["errorId"]) + " - " + response["error"])
```