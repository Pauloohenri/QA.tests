from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from selenium.webdriver.common.by import By


def test_adicionar_varios_produtos(driver):
    login = LoginPage(driver)
    produtos = ProductsPage(driver)

    login.login("standard_user", "secret_sauce")

    produtos.adicionar_produtos(2)

    produtos.ir_para_carrinho()

    itens = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(itens) == 2