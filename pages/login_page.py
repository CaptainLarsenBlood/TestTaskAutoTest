from pages.base_page import BasePage
from pages.locators import  LoginPageLocators
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    def select_user(self, text: str):
        select = Select(self.browser.find_element(By.ID, 'userSelect'))
        select.select_by_visible_text(text)

    def check_load_page(self):
        customer = self.browser.find_element(*LoginPageLocators.CUSTOMER_LOGIN)
        bank_manager = self.browser.find_element(*LoginPageLocators.MANAGER_LOGIN)
        customer.is_displayed()
        bank_manager.is_displayed()

    def select_login_type(self, custom=True):
        if custom:
            self.browser.find_element(*LoginPageLocators.CUSTOMER_LOGIN).click()
        else:
            self.browser.find_element(*LoginPageLocators.MANAGER_LOGIN).click()

    def login(self):
        self.browser.find_element(*LoginPageLocators.LOGIN).click()

