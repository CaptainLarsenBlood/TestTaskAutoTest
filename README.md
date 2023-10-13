Тестовое задание:

Краткое описание файлов:

base_page.py - тут мы храним методы которые применяются по всему проекту.

locators.py - тут мы храним локаторы, в виде констант. Локаторы каждой отдельной страницы завёрнуты в класс, чтобы было удобно импортировать

login_page, money_page - тут мы храним методы по конкретной странице, завернутые в класс этой страницы (унаследованы от BasePage)


Запуск Selenium grid: java -jar selenium-server-4.14.1.jar standalone

Запуск теста: pytest: --alluredir=allure-report

Результатты в allure: allure serve allure-report           


