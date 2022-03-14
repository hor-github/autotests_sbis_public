import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="function")
def browser(request):
    browser = webdriver.Chrome()
    print("\n! ! ! start browser ! ! !")
    link = 'https://fix-online.sbis.ru/auth/'
    page_login = LoginPage(browser, link)
    page_login.open()
    page_login.authorization(login='Прохожий', password='Прохожий1234')

    yield browser
    print("\n! ! ! quit browser ! ! !")
    browser.quit()



