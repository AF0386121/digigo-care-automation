from apis.patient_api import PatientAPI
from utilities.helpers import load_test_data

def test_api_02_get_patients():
    response = PatientAPI().get_patients()
    assert response.status_code in [401,403,404]

def test_api_03_create_patient():
    data = load_test_data()
    response = PatientAPI().create_patient(data["valid_patient"])
    assert response.status_code in [401, 403,404]
    