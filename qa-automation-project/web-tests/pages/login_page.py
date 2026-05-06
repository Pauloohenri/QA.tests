from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def login(self, usuario, senha):
        campo_user = self.wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        campo_user.send_keys(usuario)

        self.driver.find_element(By.ID, "password").send_keys(senha)
        self.driver.find_element(By.ID, "login-button").click()