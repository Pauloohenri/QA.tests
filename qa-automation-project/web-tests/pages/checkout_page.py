from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def preencher_dados(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("Paulo")
        self.wait.until(EC.visibility_of_element_located((By.ID, "last-name"))).send_keys("Teste")
        self.wait.until(EC.visibility_of_element_located((By.ID, "postal-code"))).send_keys("12345")
        self.wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()

    def finalizar(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()

    def mensagem_sucesso(self):
        return self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))).text