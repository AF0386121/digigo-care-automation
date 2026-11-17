import requests
from endpoints.endpoints import Endpoints

class AuthAPI:
    def login(self, email, password):
        # DigiGo Login is OTP based, so we test a public GET API that exists
        return requests.get(Endpoints.LOGIN)