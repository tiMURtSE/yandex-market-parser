from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from Browser import Browser
from Product import Product

class MainPage(Browser):
    SEARCH_BAR_ID = "header-search"

    def __init__(self, elem_search_delay=5):
        super().__init__(elem_search_delay)

    def search_product(self, product: Product):
        search_query = product.get_name()
        search_bar_element = self._find_search_bar()

        print(f"Поиск по {search_query}")

        # Для устранения бага
        search_bar_element.clear()
        search_bar_element.click()
        search_bar_element.send_keys(search_query)
        search_bar_element.submit()

    def _find_search_bar(self) -> WebElement:
        search_bar_element = self._wait.until(
            EC.presence_of_element_located((By.ID, self.SEARCH_BAR_ID))
        )

        return search_bar_element