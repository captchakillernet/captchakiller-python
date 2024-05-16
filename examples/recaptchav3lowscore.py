from captchakiller import CaptchaKiller

captcha_killer = CaptchaKiller()

"""
    Use custom configuration
    captcha_killer = CaptchaKiller("API_KEY")
"""

response = captcha_killer.recaptcha_v3_low_score("6LdKlZEpAAAAAAOQjzC2v_d36tWxCl6dWsozdSy9", "https://recaptcha-demo.appspot.com/", "examples/v3scores")

if response['success']:
    print("Captcha solved: " + response["result"])
else:
    print("Error: " + str(response["errorId"]) + " - " + response["error"])