from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from selenium.webdriver.common.by import By


def test_adicionar_produto_ao_carrinho(driver):
    login = LoginPage(driver)
    produtos = ProductsPage(driver)

    login.login("standard_user", "secret_sauce")
    produtos.adicionar_produto()
    produtos.ir_para_carrinho()

    itens = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(itens) > 0


def test_remover_produto_do_carrinho(driver):
    login = LoginPage(driver)
    produtos = ProductsPage(driver)

    login.login("standard_user", "secret_sauce")
    produtos.adicionar_produto()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.CLASS_NAME, "cart_button").click()

    itens = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(itens) == 0