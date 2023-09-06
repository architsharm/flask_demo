import pytest

from model import app

@pytest.fixture
def client():
    return app.test_client()


def test_home(client):    
    resp = client.get('/ping')
    assert resp.status_code == 200
    assert resp.json == {"test":"hello1"}

def test_predict(client):    
    loan_application = {
    'Gender': "Male",
    'Married': "Unmarried",
    'ApplicantIncome': 50000,
    'Credit_History': "Cleared Debts",
    'LoanAmount': 500000
}
    resp = client.post('/predict',json=loan_application)
    assert resp.status_code == 200
    assert resp.text == "Rejected"