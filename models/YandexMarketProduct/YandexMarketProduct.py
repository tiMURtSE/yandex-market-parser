from openpyxl.cell.cell import Cell

from models.YandexGPTReview.YandexGPTReview import YandexGPTReview
from Product import Product

class YandexMarketProduct(Product):
    def __init__(self, row: tuple[Cell]):
        super().__init__(row)
        self._yandexGPT_review = YandexGPTReview(product_id=self.id)

    @property
    def yandexGPT_review(self):
        return self._yandexGPT_review