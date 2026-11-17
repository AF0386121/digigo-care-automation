import requests
from endpoints.endpoints import Endpoints

class PatientAPI:
    def __init__(self, token=None):
        self.headers = {"Authorization": f"Bearer {token}"} if token else {}

    def get_patients(self):
        return requests.get(Endpoints.PATIENTS, headers=self.headers)

    def create_patient(self, payload):
        return requests.post(Endpoints.PATIENTS, json=payload, headers=self.headers)