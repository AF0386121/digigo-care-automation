import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    BASE_URL = os.getenv("BASE_URL")
    API_BASE_URL = os.getenv("API_BASE_URL")
    TEST_PHONE = os.getenv("TEST_PHONE")
    TEST_NAME = os.getenv("TEST_NAME")
    TEST_EMAIL = os.getenv("TEST_EMAIL")
    TEST_PASSWORD = os.getenv("TEST_PASSWORD")
    ADMIN_PIN = os.getenv("ADMIN_PIN")
    CLINIC_NAME = os.getenv("CLINIC_NAME")