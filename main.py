from Workbook import Workbook
from Browser import Browser
from models.MainPage.MainPage import MainPage
from models.SearchResultPage.SearchResultPage import SearchResultPage

from consts import URL

class Main:
    def __init__(self):
        self._broswer = Browser()
        self._export_workbook = Workbook()
        self._main_page = MainPage()
        self._search_result_page = SearchResultPage()

    def run(self):
        self._broswer.get(URL)
        products = self._export_workbook.convert_to_products()
        # start_pos = int(input("Номер товара, с которого нужно начать прохождение парсинг:\n"))
        start_pos = 0

        for product in products[start_pos:]:
            self._main_page.search_product(product=product)
            product.page_links = self._search_result_page.get_product_page_links()
            
            




















if __name__ == "__main__":
    app = Main()
    app.run()