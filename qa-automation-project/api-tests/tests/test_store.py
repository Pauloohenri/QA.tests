import requests

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