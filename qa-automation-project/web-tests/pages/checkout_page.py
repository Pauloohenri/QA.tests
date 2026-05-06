from selenium.webdriver.common.by import By

class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    def preencher_dados(self):
        self.driver.find_element(By.ID, "first-name").send_keys("Paulo")
        self.driver.find_element(By.ID, "last-name").send_keys("Teste")
        self.driver.find_element(By.ID, "postal-code").send_keys("12345")
        self.driver.find_element(By.ID, "continue").click()

    def finalizar(self):
        self.driver.find_element(By.ID, "finish").click()

    def mensagem_sucesso(self):
        return self.driver.find_element(By.CLASS_NAME, "complete-header").text