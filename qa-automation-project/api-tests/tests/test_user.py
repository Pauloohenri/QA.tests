import requests
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