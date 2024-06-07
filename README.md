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
#### Solve ReCaptcha V2
```

"""
    REQUIRED - sitekey: 6LfW6wATAAAAAHLqO2pb8bDBahxlMxNdo9g947u9 // Recaptcha v2 challenge site key
    REQUIRED - site: https://recaptcha-demo.appspot.com/ // Recaptcha v2 challenge page URL
    OPTIONAL - gdomain: false // If the domain is a Recaptcha, false is google by default
    OPTIONAL - invisible: false // If the Recaptcha is invisible, false by default
    OPTIONAL - payload: 3Zky78k550-A2.... // The s parameter in the anchor request
    OPTIONAL - proxytype: HTTP // Your proxy type (HTTP, SOCKS4, SOCKS5)
    OPTIONAL - proxyaddress: 127.0.0.1 // Your proxy address
    OPTIONAL - proxyport: 8080 // Your proxy port
    OPTIONAL - proxyuser: user // Your proxy login (if required)
    OPTIONAL - proxypass: pass // Your proxy password (if required)
"""

response = captcha_killer.recaptcha_v2("sitekey", "site")
if response['success']:
    print("Captcha solved: " + response["result"])
else:
    print("Error: " + str(response["errorId"]) + " - " + response["error"])
```

#### Solve ReCaptcha V2 Enterprise
```

"""
    REQUIRED - sitekey: 6LfW6wATAAAAAHLqO2pb8bDBahxlMxNdo9g947u9 // Recaptcha v2 challenge site key
    REQUIRED - site: https://recaptcha-demo.appspot.com/ // Recaptcha v2 challenge page URL
    OPTIONAL - gdomain: false // If the domain is a Recaptcha, false is google by default
    OPTIONAL - invisible: false // If the Recaptcha is invisible, false by default
    OPTIONAL - payload: 3Zky78k550-A2.... // The s parameter in the anchor request
    OPTIONAL - action: Default // The sa parameter in the anchor request
    OPTIONAL - proxytype: HTTP // Your proxy type (HTTP, SOCKS4, SOCKS5)
    OPTIONAL - proxyaddress: 127.0.0.1 // Your proxy address
    OPTIONAL - proxyport: 8080 // Your proxy port
    OPTIONAL - proxyuser: user // Your proxy login (if required)
    OPTIONAL - proxypass: pass // Your proxy password (if required)
"""

response = captcha_killer.recaptcha_v2_enterprise("sitekey", "site")
if response['success']:
    print("Captcha solved: " + response["result"])
else:
    print("Error: " + str(response["errorId"]) + " - " + response["error"])
```

#### Solve ReCaptcha V3 Low Score
```

"""
    REQUIRED - sitekey: 6LdKlZEpAAAAAAOQjzC2v_d36tWxCl6dWsozdSy9 // Recaptcha v3 challenge site key
    REQUIRED - site: https://recaptcha-demo.appspot.com/ // Recaptcha v3 challenge page URL
    REQUIRED - action: examples/v3scores // Recaptcha v3 site action, if not known, try "homepage", "submit", "verify", "register", or "login"
    OPTIONAL - gdomain: false // If the domain is a Recaptcha, false is google by default
"""

response = captcha_killer.recaptcha_v2_enterprise("sitekey", "site", "action")
if response['success']:
    print("Captcha solved: " + response["result"])
else:
    print("Error: " + str(response["errorId"]) + " - " + response["error"])
```

#### Solve Funcaptcha / Arkoselabs
```

"""
    REQUIRED - publickey: DF9C4D87-CB7B-4062-9FEB-BADB6ADA61E6 // Public key of the FunCaptcha challeng
    REQUIRED - site: https://demo.arkoselabs.com // URL of the website where the FunCaptcha challenge is located
    OPTIONAL - surl: https://client-api.arkoselabs.com // URL of the Arkose Labs API server
    OPTIONAL - datatype: blob // Data type of the data sent in the challenge
    OPTIONAL - data: ENsYWf9hLu6E5oSTcPby1t8iK4TCZgv... // Data sent in the challenge
"""

response = captcha_killer.recaptcha_v2_enterprise("publickey", "site")
if response['success']:
    print("Captcha solved: " + response["result"])
else:
    print("Error: " + str(response["errorId"]) + " - " + response["error"])
```

#### Solve MTCaptcha
```

"""
    REQUIRED - sitekey: MTPublic-DemoKey9M // MTCaptcha site key, always contains MTPublic
    REQUIRED - site: https://service.mtcaptcha.com // URL of the site that contains the MTCaptcha
    OPTIONAL - action: login // MTCaptcha action that is inside of the getchallenge.json request (act parameter)
"""

response = captcha_killer.mtcaptcha("MTPublic-DemoKey9M", "https://service.mtcaptcha.com")
if response['success']:
    print("Captcha solved: " + response["result"])
else:
    print("Error: " + str(response["errorId"]) + " - " + response["error"])
```
