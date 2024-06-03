from captchakiller import CaptchaKiller

captcha_killer = CaptchaKiller()

"""
    Use custom configuration
    captcha_killer = CaptchaKiller("API_KEY")
"""

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

response = captcha_killer.recaptcha_v2("6LfW6wATAAAAAHLqO2pb8bDBahxlMxNdo9g947u9", "https://recaptcha-demo.appspot.com/")

if response['success']:
    print("Captcha solved: " + response["result"])
else:
    print("Error: " + str(response["errorId"]) + " - " + response["error"])