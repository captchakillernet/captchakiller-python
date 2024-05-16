from .utils import _send_request

class UserManager:
    def getbalance(self):
        url = self.USER_ENDPOINT + 'balance'
        headers = {
            'x-api-key': self.API_KEY
        }
        response = _send_request(self, url, {}, headers)
        if 'error' in response:
            response.update({"success": False})
            return response
        elif 'balance' in response:
            response.update({"success": True})
            return response
        else:
            response.update({"success": False})
            return {"errorId": "0", "error": "Unknown error"}

class CaptchaKiller:
    
    TIMEOUT = 30
    API_KEY = ''
    SOLVE_ENDPOINT = 'https://api.captchakiller.net/c/'
    USER_ENDPOINT = 'https://api.captchakiller.net/u/'
    PARTNER_ID = ''
    
    def __init__(self, api_key=None, partner_id=None, timeout=30):
        self.API_KEY = api_key if api_key is not None else self.API_KEY
        self.PARTNER_ID = partner_id if partner_id is not None else self.PARTNER_ID
        self.TIMEOUT = timeout
        
    def getbalance(self):
        return UserManager.getbalance(self)
        
    def recaptcha_v2(self, sitekey, site, gdomain=False, invisible=False, payload=None):
        url = self.SOLVE_ENDPOINT + 'solvev2'
    
        queryparams = {
            'sitekey': sitekey,
            'site': site,
            'gdomain': gdomain,
            'invisible': invisible,
            'payload': payload,
        }
    
        response = _send_request(self, url, queryparams, {})
        
        if 'error' in response:
            response.update({"success": False})
            return response
        elif 'result' in response:
            response.update({"success": True})
            return response
        else:
            response.update({"success": False})
            return {"errorId": "0", "error": "Unknown error"}
        
    def recaptcha_v2_enterprise(self, sitekey, site, gdomain=False, invisible=False, payload=None, action=None):
        url = self.SOLVE_ENDPOINT + 'solvev2e'
    
        queryparams = {
            'sitekey': sitekey,
            'site': site,
            'gdomain': gdomain,
            'invisible': invisible,
            'payload': payload,
            'action': action,
        }
    
        response = _send_request(self, url, queryparams, {})
        
        if 'error' in response:
            response.update({"success": False})
            return response
        elif 'result' in response:
            response.update({"success": True})
            return response
        else:
            response.update({"success": False})
            return {"errorId": "0", "error": "Unknown error"}
        
    def recaptcha_v3_low_score(self, sitekey, site, action, gdomain=False):
        url = self.SOLVE_ENDPOINT + 'solvev3ls'
        
        queryparams = {
            'sitekey': sitekey,
            'site': site,
            'action': action,
            'gdomain': gdomain,
        }
        
        response = _send_request(self, url, queryparams, {})
        
        if 'error' in response:
            response.update({"success": False})
            return response
        elif 'result' in response:
            response.update({"success": True})
            return response
        else:
            response.update({"success": False})
            return {"errorId": "0", "error": "Unknown error"}