from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def click_add_to_bucsket(self):
        add_busket_button = self.browser.find_element(*ProductPageLocators.ADD_BUCSKET_BUTTON)
        add_busket_button.click()

