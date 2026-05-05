import requests

def test_deve_criar_pet(base_url):
    pet = {
        "id": 12345,
        "name": "DogTeste",
        "status": "available"
    }

    res = requests.post(f"{base_url}/pet", json=pet)
    assert res.status_code == 200


def test_deve_buscar_pet(base_url):
    res = requests.get(f"{base_url}/pet/1")
    assert res.status_code in [200, 404]