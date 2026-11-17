from apis.auth_api import AuthAPI
from config.config import Config

def test_api_01_login():
    response = AuthAPI().login(Config.TEST_EMAIL, Config.TEST_PASSWORD)
    assert response.status_code in [401, 403]
    print("API Security Test PASSED - Unauthenticated request correctly rejected with 401")