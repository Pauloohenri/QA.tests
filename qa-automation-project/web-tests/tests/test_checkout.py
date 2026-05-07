import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    mensagem = checkout.mensagem_sucesso()
    assert "Thank you" in mensagem


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

    WebDriverWait(driver, 10).until(EC.url_contains("checkout-step-one"))    

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "continue"))).click()

    erro = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']")))

    assert "First Name is required" in erro.text

def test_finalizar_compra_com_varios_produtos(driver):

    login = LoginPage(driver)
    produtos = ProductsPage(driver)
    carrinho = CartPage(driver)
    checkout = CheckoutPage(driver)

    login.login("standard_user", "secret_sauce")

    botoes = driver.find_elements(By.CSS_SELECTOR, ".btn_inventory")

    botoes[0].click()
    botoes[1].click()
    botoes[2].click()

    produtos.ir_para_carrinho()

    carrinho.iniciar_checkout()

    checkout.preencher_dados()
    checkout.finalizar()

    mensagem = checkout.mensagem_sucesso()

    assert "Thank you" in mensagem

def test_cancelar_checkout(driver):

    login = LoginPage(driver)
    produtos = ProductsPage(driver)
    carrinho = CartPage(driver)
    checkout = CheckoutPage(driver)

    login.login("standard_user", "secret_sauce")

    produtos.adicionar_produto()
    produtos.ir_para_carrinho()

    carrinho.iniciar_checkout()

    driver.find_element(By.ID, "cancel").click()

    assert "cart.html" in driver.current_url

def test_logout_apos_compra(driver):

    login = LoginPage(driver)
    produtos = ProductsPage(driver)
    carrinho = CartPage(driver)
    checkout = CheckoutPage(driver)

    login.login("standard_user", "secret_sauce")

    produtos.adicionar_produto()
    produtos.ir_para_carrinho()

    carrinho.iniciar_checkout()

    checkout.preencher_dados()
    checkout.finalizar()

    driver.find_element(By.ID, "react-burger-menu-btn").click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    ).click()

    assert "saucedemo.com" in driver.current_url

def test_fluxo_completo_de_compra(driver):

    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    login = LoginPage(driver)
    produtos = ProductsPage(driver)
    carrinho = CartPage(driver)
    checkout = CheckoutPage(driver)

    # Login
    login.login("standard_user", "secret_sauce")

    # Adiciona múltiplos produtos
    botoes = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".btn_inventory")
        )
    )

    botoes[0].click()
    botoes[1].click()

    # Valida quantidade no carrinho
    badge = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "shopping_cart_badge")
        )
    )

    assert badge.text == "2"

    # Vai para carrinho
    produtos.ir_para_carrinho()

    # Valida produtos no carrinho
    produtos_carrinho = driver.find_elements(
        By.CLASS_NAME,
        "inventory_item_name"
    )

    assert len(produtos_carrinho) == 2

    # Inicia checkout
    carrinho.iniciar_checkout()

    # Preenche dados
    checkout.preencher_dados()

    # Valida tela de resumo
    resumo = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "summary_info")
        )
    )

    assert resumo.is_displayed()

    # Finaliza compra
    checkout.finalizar()

    # Valida mensagem final
    mensagem = checkout.mensagem_sucesso()

    assert "Thank you" in mensagem

    # Valida URL final
    assert "checkout-complete" in driver.current_url