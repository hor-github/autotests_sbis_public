from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators import LoginPageLocators


class LoginPage(BasePage):
    # проверка нахождения инпута логина на странице
    def should_be_login_input(self):
        assert self.is_element_present(*LoginPageLocators.AUTH_LOGIN), "Форма ввода логина не представлена на странице"

    # Ввод данных в инпуты и клик по кнопке для авторизации
    def authorization(self, login, password):
        self.browser.find_element(*LoginPageLocators.AUTH_LOGIN).send_keys(login)

        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(LoginPageLocators.AUTH_PASSWORD)).send_keys(password)

        self.browser.find_element(*LoginPageLocators.AUTH_BUTTON).click()


