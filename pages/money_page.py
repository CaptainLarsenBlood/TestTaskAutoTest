from pages.base_page import BasePage
from pages.locators import  MoneyPageLocators
from selenium.webdriver.common.by import By
from function import assert_equal_time


class MoneyPage(BasePage):

    def select_operation(self, type_oper='trans'):
        match type_oper:
            case 'trans':
                self.browser.find_element(*MoneyPageLocators.TRANSACTIONS).click()
                assert_equal_time(lambda: self.browser.find_element(By.CSS_SELECTOR, ".table").is_displayed(), True, 2)
                self.browser.refresh()

            case 'deposit':
                self.browser.find_element(*MoneyPageLocators.DEPOSIT).click()
                assert_equal_time(lambda: self.browser.find_element(MoneyPageLocators.SUBMIT).text, "Deposit", 2)
            case 'with':
                self.browser.find_element(*MoneyPageLocators.WITHDRAWL).click()
                assert_equal_time(lambda: self.browser.find_element(MoneyPageLocators.SUBMIT).text, "Deposit", 2)

    def input_money_and_submit(self, amount=None):

        self.browser.find_element(*MoneyPageLocators.AMOUNT_INP).send_keys(amount)
        self.browser.find_element(*MoneyPageLocators.SUBMIT).click()

    def check_balance(self, balance=0):

        assert balance == int(self.browser.find_element(*MoneyPageLocators.INFO_ACCOUNT).text),\
            f"Баланс должен быть {balance}!"

    def get_line_transaction(self, line: str):
        return self.browser.find_element(By.CSS_SELECTOR, f'[id=anchor{line}').text
