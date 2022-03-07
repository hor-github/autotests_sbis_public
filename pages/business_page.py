from locators import MainPageSbisLocators
from locators import BusinessPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class BusinessPage(BasePage):

    # переход на главную Бизнес
    def go_to_the_main_business(self):
        # ожидание кнопки Бизнес в аккордеоне
        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(MainPageSbisLocators.BUSINESS_BUTTON)).click()

        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(MainPageSbisLocators.Business_bb)).click()

    # Переход в отчет Продажи
    def go_to_sale_report(self):
        # ожидание кнопки Бизнес в аккордеоне
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(MainPageSbisLocators.BUSINESS_BUTTON)).click()
        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(MainPageSbisLocators.Business_bb)).click()

        # ожидание панели построения отчета Продажи
        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(BusinessPageLocators.SALE_REPORT)).click()
        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(BusinessPageLocators.TITLE_SALE_REPORT))

    # Открытие панели построения отчета Сравнение продаж
    def go_to_sales_comparison_report(self):
        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(BusinessPageLocators.SALES_COMPARISON_REPORT)).click()
        # явное ожидание панели построения отчета Сравнение продаж
        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(BusinessPageLocators.TITLE_COMPARISON))

    # Проверка открытия панели построения отчета Продажи
    def should_be_sale_report_form(self):
        assert self.is_element_present(*BusinessPageLocators.TITLE_SALE_REPORT), "Панель построения отчета не появилась"


