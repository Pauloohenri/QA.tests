from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def iniciar_checkout(self):
        checkout_btn = self.wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            checkout_btn
        )

        self.driver.execute_script(
            "arguments[0].click();",
            checkout_btn
        )

        self.wait.until(
            EC.url_contains("checkout-step-one")
        )