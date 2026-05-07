from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def preencher_dados(self):

        self.wait.until(
            EC.url_contains("checkout-step-one")
        )

        first_name = self.wait.until(
            EC.visibility_of_element_located((By.ID, "first-name"))
        )
        first_name.clear()
        first_name.send_keys("Paulo")

        last_name = self.wait.until(
            EC.visibility_of_element_located((By.ID, "last-name"))
        )
        last_name.clear()
        last_name.send_keys("Teste")

        postal = self.wait.until(
            EC.visibility_of_element_located((By.ID, "postal-code"))
        )
        postal.clear()
        postal.send_keys("12345")

        continue_btn = self.wait.until(
            EC.element_to_be_clickable((By.ID, "continue"))
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            continue_btn
        )

        continue_btn.click()

    def finalizar(self):

        finish_btn = self.wait.until(
            EC.element_to_be_clickable((By.ID, "finish"))
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            finish_btn
        )

        finish_btn.click()

    def mensagem_sucesso(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "complete-header")
            )
        ).text