from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def adicionar_produto(self):

        btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "btn_inventory")
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            btn
        )

    def adicionar_produtos(self, quantidade):

        botoes = self.wait.until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "btn_inventory")
            )
        )

        for i in range(quantidade):

            self.driver.execute_script(
                "arguments[0].click();",
                botoes[i]
            )

    def ir_para_carrinho(self):

        carrinho = self.wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "shopping_cart_link")
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            carrinho
        )

        self.wait.until(
            EC.url_contains("cart")
        )