from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_adicionar_produto_ao_carrinho(driver):
    login = LoginPage(driver)
    produtos = ProductsPage(driver)

    login.login("standard_user", "secret_sauce")
    produtos.adicionar_produto()
    produtos.ir_para_carrinho()

    itens = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item")))
    assert len(itens) > 0


def test_remover_produto_do_carrinho(driver):

    login = LoginPage(driver)
    produtos = ProductsPage(driver)

    wait = WebDriverWait(driver, 15)

    login.login("standard_user", "secret_sauce")

    produtos.adicionar_produto()
    produtos.ir_para_carrinho()

    wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "cart_item")
        )
    )

    remover = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "[data-test^='remove']")
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        remover
    )

    wait.until(
        EC.invisibility_of_element_located(
            (By.CLASS_NAME, "cart_item")
        )
    )

    itens = driver.find_elements(By.CLASS_NAME, "cart_item")

    assert len(itens) == 0