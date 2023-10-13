import time
import allure
from pages.login_page import LoginPage
from pages.money_page import MoneyPage
import logging as log
import datetime
import csv


def get_fibonacii(N):
    if N <= 3:
        return 1
    else:
        return get_fibonacii(N-1) + get_fibonacii(N-2)

class TestMain:

    date = datetime.datetime.now()

    @allure.title("Check money with Potter")
    def test_guest_can_go_to_login_page(self, browser):
        self.login_page = LoginPage(browser=browser,
                                   url="https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")

        with allure.step('Переходим на главную страницу'):
            self.login_page.open()
            self.login_page.check_load_page()

        with allure.step("Заходим под Поттером"):
            self.login_page.select_login_type()
            self.login_page.select_user("Harry Potter")
            self.login_page.login()

        with allure.step("Считаем Фибоначи -> заносим эту сумму на счет и списываем"):
            N = get_fibonacii(self.date.month+1)
            self.money_page = MoneyPage(browser)
            self.money_page.select_operation('deposit')
            self.money_page.input_money_and_submit(N)
            self.money_page.select_operation('with')
            self.money_page.input_money_and_submit(N)

        with allure.step("Проверяем баланс и транзакции"):
            self.money_page.check_balance()
            self.money_page.select_operation('trans')
            line_1 = self.money_page.get_line_transaction(0)
            assert "Credit" in line_1
            line_2 = self.money_page.get_line_transaction(1)
            assert "Debit" in line_2

        with allure.step("Записываем данные в csv"):
            with open("money.csv", mode="w", encoding='utf-8') as file:
                str_1 = f"{self.date.day} {line_1.split(',')[0][:3]} {self.date.year} {line_1[13:21]}"
                file_writer = csv.writer(file, delimiter=",", lineterminator="\r")
                file_writer.writerow(["<Дата-времямя Транзакции>", "Сумма", "Тип"])
                type_oper = lambda x: "Debit" if "Debit" in x else "Credit"
                file_writer.writerow([str_1, line_1[25:27], type_oper(line_1)])
                str_2 = f"{self.date.day} {line_2.split(',')[0][:3]} {self.date.year} {line_2[13:21]}"
                file_writer.writerow([str_2, line_2[25:27], type_oper(line_2)])
                allure.attach.file("money.csv", "table_result")
