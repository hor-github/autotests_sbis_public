import pytest

import conftest
import pages.base_page
from pages.business_page import BusinessPage
from pages.sale_report_filter_page import SaleReportFilterPage
import time


class TestOperationFilter:


    def test_operation_filter_realization(self, browser):
        page_business = BusinessPage(browser, BusinessPage)
        page_sale_report_filter = SaleReportFilterPage(browser, SaleReportFilterPage)
        page_business.go_to_sale_report()
        page_sale_report_filter.select_operation_realization()
        page_sale_report_filter.should_be_realization_operation()
        page_sale_report_filter.generate_sale_report()
        page_sale_report_filter.should_be_realization_operation()
        page_sale_report_filter.should_be_qty_column()
        time.sleep(5)

    def test_operation_filter_retail_realization(self, browser):
        page_business = BusinessPage(browser, BusinessPage)
        page_sale_report_filter = SaleReportFilterPage(browser, SaleReportFilterPage)
        page_business.go_to_sale_report()
        page_sale_report_filter.select_operation_retail_realization()
        page_sale_report_filter.should_be_retail_realization_operation()
        page_sale_report_filter.generate_sale_report()
        page_sale_report_filter.should_be_retail_realization_operation()
        page_sale_report_filter.should_be_qty_column()
        page_sale_report_filter.should_be_qty_column()
        # time.sleep(5)
