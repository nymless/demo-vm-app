from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hi there!"}


def test_predict():
    response = client.post(
        "/predict/",
        json={"url": "https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg"})
    text = response.text
    assert response.status_code == 200
    assert isinstance(text, str)
