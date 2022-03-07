from pages.base_page import BasePage
from locators import SaleReportPanelLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SaleReportFilterPage(BasePage):
    # Открытие фильтра Операции
    def open_operation_filter(self):
        operation_filter_button = self.browser.find_element(*SaleReportPanelLocators.OPERATION_FILTER_BUTTON).click()

    # Выбор операции Реализация
    def select_operation_realization(self):
        # Открытие фильтра Операции
        # self.browser.find_element(*SaleReportPanelLocators.OPERATION_FILTER_BUTTON).click()
        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(SaleReportPanelLocators.OPERATION_FILTER_BUTTON)).click()
        # Выбор операции = Реализация
        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(SaleReportPanelLocators.REALIZATION)).click()

        # Выбор операции Реализация розницы
    def select_operation_retail_realization(self):
        # Открытие фильтра Операции
        # self.browser.find_element(*SaleReportPanelLocators.OPERATION_FILTER_BUTTON).click()
        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(SaleReportPanelLocators.OPERATION_FILTER_BUTTON)).click()
        # Выбор операции = Реализация розницы
        WebDriverWait(self.browser, 5).until(
               EC.presence_of_element_located(SaleReportPanelLocators.RETAIL_REALIZATION)).click()

    # Проверка наличия выбранно операции Реализация на панели построения отчета
    def should_be_realization_operation(self):
        assert self.is_element_present(*SaleReportPanelLocators.REALIZATION_IN_PANEL)

    # Проверка наличия выбранно операции Реализация розницы на панели построения отчета
    def should_be_retail_realization_operation(self):
        assert self.is_element_present(*SaleReportPanelLocators.RETAIL_REALIZATION_IN_PANEL)

    # Построение отчета
    def generate_sale_report(self):
        self.browser.find_element(*SaleReportPanelLocators.BUTTON_GENERATE).click()

    # Ожидание колонки Кол-во
    def should_be_qty_column(self):
        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(SaleReportPanelLocators.COLUMN_QTY))
