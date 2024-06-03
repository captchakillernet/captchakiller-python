from captchakiller import CaptchaKiller

captcha_killer = CaptchaKiller()

"""
    Use custom configuration
    captcha_killer = CaptchaKiller("API_KEY")
"""

"""
    REQUIRED - sitekey: 6LdKlZEpAAAAAAOQjzC2v_d36tWxCl6dWsozdSy9 // Recaptcha v3 challenge site key
    REQUIRED - site: https://recaptcha-demo.appspot.com/ // Recaptcha v3 challenge page URL
    REQUIRED - action: examples/v3scores // Recaptcha v3 site action, if not known, try "homepage", "submit", "verify", "register", or "login"
    OPTIONAL - gdomain: false // If the domain is a Recaptcha, false is google by default
"""

response = captcha_killer.recaptcha_v3_low_score("6LdKlZEpAAAAAAOQjzC2v_d36tWxCl6dWsozdSy9", "https://recaptcha-demo.appspot.com/", "examples/v3scores")

if response['success']:
    print("Captcha solved: " + response["result"])
else:
    print("Error: " + str(response["errorId"]) + " - " + response["error"])