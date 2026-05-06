import sys
import os

# corrige caminho dos imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


from dotenv import load_dotenv

load_dotenv()

def test_deve_finalizar_compra(driver):
    usuario = os.getenv("LOGIN_USER")
    senha = os.getenv("LOGIN_PASSWORD")

    login = LoginPage(driver)
    produtos = ProductsPage(driver)
    carrinho = CartPage(driver)
    checkout = CheckoutPage(driver)

    login.login(usuario, senha)
    produtos.adicionar_produto()
    produtos.ir_para_carrinho()
    carrinho.iniciar_checkout()
    checkout.preencher_dados()
    checkout.finalizar()

    assert "Thank you" in checkout.mensagem_sucesso()


def test_checkout_sem_dados(driver):
    from pages.login_page import LoginPage
    from pages.products_page import ProductsPage
    from pages.cart_page import CartPage

    login = LoginPage(driver)
    produtos = ProductsPage(driver)
    carrinho = CartPage(driver)

    login.login("standard_user", "secret_sauce")
    produtos.adicionar_produto()
    produtos.ir_para_carrinho()
    carrinho.iniciar_checkout()

    driver.find_element(By.ID, "continue").click()

    erro = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    assert "First Name is required" in erro.text