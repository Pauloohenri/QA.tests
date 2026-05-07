from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def adicionar_produto(self):
        btn = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn_inventory"))
        )
        btn.click()

    def adicionar_produtos(self, quantidade):
        botoes = self.wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "btn_inventory"))
        )

        for i in range(quantidade):
            botoes[i].click()

    def ir_para_carrinho(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "shopping_cart_link")
            )
        ).click()

        self.wait.until(
            EC.url_contains("cart")
        )