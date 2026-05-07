import requests
BASE_URL = "https://petstore.swagger.io/v2"
from utils.data_factory import criar_usuario

def test_deve_criar_buscar_e_deletar_usuario(base_url):
    usuario = criar_usuario()

    # Criar usuário
    res = requests.post(f"{base_url}/user", json=usuario)
    assert res.status_code == 200

    # Buscar usuário
    res = requests.get(f"{base_url}/user/{usuario['username']}")
    assert res.status_code == 200
    assert res.json()['username'] == usuario['username']

    # Deletar usuário
    res = requests.delete(f"{base_url}/user/{usuario['username']}")
    assert res.status_code == 200

def test_login_usuario():

    username = "pauloqa"

    payload = {
        "id": 1,
        "username": username,
        "firstName": "Paulo",
        "lastName": "Teste",
        "email": "paulo@email.com",
        "password": "123456",
        "phone": "99999999",
        "userStatus": 1
    }

    requests.post(
        f"{BASE_URL}/user",
        json=payload
    )

    response = requests.get(
        f"{BASE_URL}/user/login?username={username}&password=123456"
    )

    assert response.status_code == 200


def test_deletar_usuario():

    username = "usuario_delete"

    payload = {
        "id": 1,
        "username": username,
        "firstName": "Teste",
        "lastName": "QA",
        "email": "teste@email.com",
        "password": "123456",
        "phone": "99999999",
        "userStatus": 1
    }

    requests.post(
        f"{BASE_URL}/user",
        json=payload
    )

    response = requests.delete(
        f"{BASE_URL}/user/{username}"
    )

    assert response.status_code == 200

def test_criar_usuario_sem_username():

    payload = {
        "id": 1,
        "username": "",
        "firstName": "Teste",
        "lastName": "QA",
        "email": "teste@email.com",
        "password": "123456",
        "phone": "99999999",
        "userStatus": 1
    }

    response = requests.post(
        f"{BASE_URL}/user",
        json=payload
    )

    assert response.status_code in [200, 400]