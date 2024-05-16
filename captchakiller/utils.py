import requests
import json
import time


def _send_request(self, url, queryparams, headers=None):
    try:
        headers['x-partner-id'] = self.PARTNER_ID
        headers['x-api-key'] = self.API_KEY
        response = requests.get(url, params=queryparams, headers=headers, timeout=self.TIMEOUT)
        return response.json()
    except Exception as e:
        return {"error": e}
    