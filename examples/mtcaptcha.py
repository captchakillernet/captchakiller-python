from captchakiller import CaptchaKiller

captcha_killer = CaptchaKiller()

"""
    Use custom configuration
    captcha_killer = CaptchaKiller("API_KEY")
"""

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