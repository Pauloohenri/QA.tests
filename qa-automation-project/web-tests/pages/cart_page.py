from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def iniciar_checkout(self):

        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "cart_list"))
        )

        checkout_btn = self.wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            checkout_btn
        )

        checkout_btn.click()

        self.wait.until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )