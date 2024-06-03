from captchakiller import CaptchaKiller

captcha_killer = CaptchaKiller()

"""
    Use custom configuration
    captcha_killer = CaptchaKiller("API_KEY")
"""

"""
    REQUIRED - publickey: DF9C4D87-CB7B-4062-9FEB-BADB6ADA61E6 // Public key of the FunCaptcha challeng
    REQUIRED - site: https://demo.arkoselabs.com // URL of the website where the FunCaptcha challenge is located
    OPTIONAL - surl: https://client-api.arkoselabs.com // URL of the Arkose Labs API server
    OPTIONAL - datatype: blob // Data type of the data sent in the challenge
    OPTIONAL - data: ENsYWf9hLu6E5oSTcPby1t8iK4TCZgv... // Data sent in the challenge
"""

response = captcha_killer.funcaptcha("DF9C4D87-CB7B-4062-9FEB-BADB6ADA61E6", "https://demo.arkoselabs.com")

if response['success']:
    print("Captcha solved: " + response["result"])
else:
    print("Error: " + str(response["errorId"]) + " - " + response["error"])