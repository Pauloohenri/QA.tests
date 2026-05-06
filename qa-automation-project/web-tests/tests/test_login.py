from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_invalido(driver):
    login = LoginPage(driver)
    login.login("usuario_errado", "senha_errada")

    erro = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
    )

    assert "Username and password do not match" in erro.text

def test_usuario_bloqueado(driver):
    login = LoginPage(driver)
    login.login("locked_out_user", "secret_sauce")

    erro = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
    )

    assert "locked" in erro.text