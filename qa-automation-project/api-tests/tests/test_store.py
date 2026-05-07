import requests
BASE_URL = "https://petstore.swagger.io/v2"

def test_deve_criar_pedido(base_url):
    order = {
        "id": 1,
        "petId": 1,
        "quantity": 1,
        "status": "placed",
        "complete": True
    }

    res = requests.post(f"{base_url}/store/order", json=order)
    assert res.status_code == 200

def test_buscar_inventario():

    response = requests.get(
        f"{BASE_URL}/store/inventory"
    )

    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_buscar_pedido_inexistente():

    response = requests.get(
        f"{BASE_URL}/store/order/999999"
    )

    assert response.status_code == 404