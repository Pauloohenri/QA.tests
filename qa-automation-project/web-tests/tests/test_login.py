from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

def test_login_invalido(driver):
    login = LoginPage(driver)
    login.login("usuario_errado", "senha_errada")

    erro = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    assert "Username and password do not match" in erro.text


def test_usuario_bloqueado(driver):
    login = LoginPage(driver)
    login.login("locked_out_user", "secret_sauce")

    erro = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    assert "locked out" in erro.text