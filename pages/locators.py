from selenium.webdriver.common.by import By


class LoginPageLocators:
    CUSTOMER_LOGIN = (By.CSS_SELECTOR, '[ng-click="customer()"]')
    MANAGER_LOGIN = (By.CSS_SELECTOR, '[ng-click="manager()"]')
    USER_SELECT = (By.ID, 'userSelect')
    LOGIN = (By.CSS_SELECTOR, '[type="submit"]')


class MoneyPageLocators:
    TRANSACTIONS = (By.CSS_SELECTOR, '[ng-click="transactions()"]')
    DEPOSIT = (By.CSS_SELECTOR, '[ng-click="deposit()"]')
    WITHDRAWL = (By.CSS_SELECTOR, '[ng-click="withdrawl()"]')
    AMOUNT_INP = (By.CSS_SELECTOR, '[ng-model="amount"]')
    SUBMIT = (By.CSS_SELECTOR, '[type="submit"]')
    INFO_ACCOUNT = (By.XPATH, "//*[contains(@class, 'ng-binding')][2]")