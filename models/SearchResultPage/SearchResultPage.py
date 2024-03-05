from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

from Browser import Browser

class SearchResultPage(Browser):
    PRODUCT_WINDOW = "_1lpjN._1Oii8.cXkP_.gCOkS"
    SPELLCHECKER = "_3RoU0.D7c4V._3aPfw._25vcL._1x2l8"
    BUTTON_BY_RATING_CLASS = "_23p69"
    SHOW_MORE_BUTTON_SELECTOR = ".qaxd1._2jRxX button._2AMPZ._1N_0H._1ghok._390_8"
    PRODUCT_TITLE_SELECTOR = "h3 > .egKyN"
    
    SCROLL_TO_NEXT_PAGE_COUNT = 3

    def __init__(self, elem_search_delay=5):
        super().__init__(elem_search_delay)

    def get_product_page_links(self):
        product_page_links = []

        if not self._has_search_results():
            print("Товаров не было найдено")
            return product_page_links
        
        self._set_filter_by_rating()

        product_title_elements = self._browser.find_elements(By.CSS_SELECTOR, self.PRODUCT_TITLE_SELECTOR)
        print(f"Количество товаров: {len(product_title_elements)}")

        for element in product_title_elements:
            product_link = element.get_attribute("href")
            product_title = element.text

            print(f"Название товара: {product_title}")




    def _has_show_more_button(self):
        try:
            self._wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "_2AMPZ._1N_0H._1ghok._390_8"))
            )
        except NoSuchElementException:
            return False
        
        return True
    
    def _scroll_to_next_page(self):
        # show_more_button_element = self._browser.find_element(By.CSS_SELECTOR, self.SHOW_MORE_BUTTON_SELECTOR)
        show_more_button_element = self._browser.find_elements(By.CLASS_NAME, "_2AMPZ._1N_0H._1ghok._390_8")[0]

        print(f"Кнопка: {show_more_button_element}")
        show_more_button_element.click()
    
    def _set_filter_by_rating(self):
        filter_button_elements = self._browser.find_elements(
            By.CLASS_NAME, self.BUTTON_BY_RATING_CLASS
        )

        button_by_rating_element = filter_button_elements[2]
        button_by_rating_element.click()

    def _has_search_results(self):
        return self._has_product_window() and not self._has_spellchecker()

    def _has_product_window(self):
        try:
            self._wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, self.PRODUCT_WINDOW))
            )
        except:
            return False
        
        return True
    
    def _has_spellchecker(self):
        mysterious_element = self._browser.find_elements(By.CLASS_NAME, self.SPELLCHECKER)[0]

        if "ничего не нашлось" in mysterious_element.text.lower():
            return True
        else:
            return False