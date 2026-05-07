import requests
BASE_URL = "https://petstore.swagger.io/v2"

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

def test_deve_atualizar_pet():
    pet_id = 99999

    payload = {
        "id": pet_id,
        "name": "rex",
        "status": "available"
    }

    requests.post(f"{BASE_URL}/pet", json=payload)

    payload["name"] = "thor"

    response = requests.put(
        f"{BASE_URL}/pet",
        json=payload
    )

    assert response.status_code == 200
    assert response.json()["name"] == "thor"


def test_busca_pet_inexistente():

    response = requests.get(
        f"{BASE_URL}/pet/999999999"
    )

    assert response.status_code != 500

def test_deletar_pet():

    pet_id = 77777

    payload = {
        "id": pet_id,
        "name": "rex",
        "status": "available"
    }

    requests.post(
        f"{BASE_URL}/pet",
        json=payload
    )

    response = requests.delete(
        f"{BASE_URL}/pet/{pet_id}"
    )

    assert response.status_code == 200