import time

from Workbook import Workbook
from Browser import Browser
from models.MainPage.MainPage import MainPage
from models.SearchResultPage.SearchResultPage import SearchResultPage
from models.ProductPage.ProductPage import ProductPage
from models.ReviewsPage.ReviewsPage import ReviewsPage
from models.ResultWorkbook.ResultWorkbook import ResultWorkbook

from consts import URL

class Main:
    def __init__(self):
        self._browser = Browser()
        self._export_workbook = Workbook()
        self._main_page = MainPage()
        self._search_result_page = SearchResultPage()
        self._product_page = ProductPage()
        self._reviews_page = ReviewsPage()
        self._result_workbook = ResultWorkbook()

    def run(self):
        self._browser.get(URL)
        time.sleep(15)
        products = self._export_workbook.convert_to_products()
        # start_pos = int(input("Номер товара, с которого нужно начать прохождение парсинг:\n"))
        start_pos = 14

        for product in products[start_pos:]:
            self._main_page.search_product(product=product)
            product.page_links = self._search_result_page.get_product_page_links(product=product)
            
            for link in product.page_links:
                self._browser.get(link)
                reviews_link = self._product_page.get_review_page_link()

                if reviews_link:
                    yandexGPT_review = self._product_page.get_yandexGPT_review()

                    if yandexGPT_review:
                        product.yandexGPT_review.set_review(review=yandexGPT_review)

                    self._browser.get(reviews_link)
                    reviews = self._reviews_page.get_reviews(product=product)

                    product.reviews.extend(reviews)

                else:
                    break

            if product.reviews:
                print(f"Количество отзывов: {len(product.reviews)}")
                self._result_workbook.write_result(product=product)

if __name__ == "__main__":
    app = Main()
    app.run()