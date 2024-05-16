from captchakiller import CaptchaKiller

captcha_killer = CaptchaKiller()

"""
    Use custom configuration
    captcha_killer = CaptchaKiller("API_KEY")
"""

response = captcha_killer.recaptcha_v2_enterprise("6LfW6wATAAAAAHLqO2pb8bDBahxlMxNdo9g947u9", "https://recaptcha-demo.appspot.com/")

if response['success']:
    print("Captcha solved: " + response["result"])
else:
    print("Error: " + str(response["errorId"]) + " - " + response["error"])