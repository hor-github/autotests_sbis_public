from selenium.webdriver.common.by import By


class LoginPageLocators:
    AUTH_LOGIN = By.CSS_SELECTOR, ".auth-Form__content input[name=login]"
    AUTH_PASSWORD = By.CSS_SELECTOR, ".auth-Form__content input[name=password]"
    AUTH_BUTTON = By.CSS_SELECTOR, ".auth-Form__submit"


class MainPageSbisLocators:
    BUSINESS_BUTTON = By.CSS_SELECTOR, '.NavigationPanels-Accordion__item_level-1[name="item-business"]'
    Business_bb = By.CSS_SELECTOR, ".NavigationPanels-SubMenu__head .NavigationPanels-Accordion__prevent-default:nth-child(3)"


class BusinessPageLocators:

    SALE_REPORT = By.CSS_SELECTOR, '.controls-Grid div[attr-data-qa="key-SalesReport"] .controls-Grid__row-cell_rowSpacingBottom_default'
    TITLE_SALE_REPORT = By.CSS_SELECTOR, 'span[title = Продажи]'

    SALES_COMPARISON_REPORT = By.CSS_SELECTOR, '.controls-Grid div[attr-data-qa="key-SalesComparisonReport"] .controls-Grid__row-cell_rowSpacingBottom_default'
    # Заголовок панели построения отчета Сравнение продаж
    TITLE_COMPARISON = By.CSS_SELECTOR, '.report-Opener__template span[title]:nth-child(1)'


class SaleReportPanelLocators:
    OPERATION_FILTER_BUTTON = By.CSS_SELECTOR, 'div[name = popupTarget] .controls-FilterDropdown__content_text'
    REALIZATION = By.CSS_SELECTOR, 'div[title=Реализация] .controls-Menu__content-wrapper'
    REALIZATION_IN_PANEL = By.CSS_SELECTOR, 'div[title=Реализация]'
    BUTTON_GENERATE = By.CSS_SELECTOR, '.controls-DialogTemplate__top-area span[data-qa=FilterPanel__filterButton]'
    COLUMN_QTY = By.CSS_SELECTOR, '.controls-StickyHeader>div[title=Кол-во]'
    RETAIL_REALIZATION = By.CSS_SELECTOR, 'div[title="Реализация розницы"] .controls-Menu__content-wrapper'
    RETAIL_REALIZATION_IN_PANEL = By.CSS_SELECTOR, 'div[title="Реализация розницы"]'

