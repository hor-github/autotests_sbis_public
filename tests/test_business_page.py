from pages.business_page import BusinessPage


def test_open_sale_report(browser):
    page_business = BusinessPage(browser, BusinessPage)
    page_business.go_to_the_main_business()
    page_business.go_to_sale_report()
    page_business.should_be_sale_report_form()


def test_open_sales_comparison_report(browser):
    page_business = BusinessPage(browser, BusinessPage)
    page_business.go_to_the_main_business()
    page_business.go_to_sales_comparison_report()

