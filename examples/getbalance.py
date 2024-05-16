from captchakiller import CaptchaKiller

captcha_killer = CaptchaKiller()

"""
    Use custom configuration
    captcha_killer = CaptchaKiller("API_KEY")
"""

response = captcha_killer.getbalance()

if response['success']:
    print("Balance: " + response["balance"])
else:
    print("Error: " + str(response["errorId"]) + " - " + response["error"])