from config.config import Config

class Endpoints:
    LOGIN = f"{Config.API_BASE_URL}/announcements/active"
    PATIENTS = f"{Config.API_BASE_URL}/patients"
    APPOINTMENTS = f"{Config.API_BASE_URL}/appointments"
    DOCTORS = f"{Config.API_BASE_URL}/doctors"