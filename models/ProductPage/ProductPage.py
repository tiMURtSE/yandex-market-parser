from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from Browser import Browser

class ProductPage(Browser):
    REVIEWS_CLASS = "_3A1_K"
    REVIEW_RATING_CLASS = "_2S7Nj _36m2h"
    YANDEXGPT_BLOCK_CLASS = "_2I1yE"
    PROS_SELECTOR = "#plus-circle-filled ~ span"
    CONS_SELECTOR = "#minus-circle-filled ~ span"

    def __init__(self, elem_search_delay=5):
        super().__init__(elem_search_delay)

    def get_yandexGPT_review(self):
        if self._has_yandexGPT_review():
            print("Отзыв от YandexGPT: есть")
        else:
            print("Отзыв от YandexGPT: нет")
            return
        
        pros = self._find_yandexGPT_review_pros()
        cons = self._find_yandexGPT_review_cons()

        return {
            "pros": pros,
            "cons": cons,
        }
    
    def get_review_page_link(self):
        if not self._has_reviews():
            print("Отзывов нет")
            return
        
        reviews_link_element = self._browser.find_element(By.CLASS_NAME, self.REVIEW_RATING_CLASS)
        reviews_page_link = reviews_link_element.get_attribute("href")

        return reviews_page_link

    def _has_reviews(self):
        try:
            self._wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, self.REVIEW_RATING_CLASS))
            )
        except:
            return False
        
        return True

    def _has_yandexGPT_review(self):
        try:
            self._wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, self.YANDEXGPT_BLOCK_CLASS))
            )
        except:
            return False
        
        return True
    
    def _find_yandexGPT_review_pros(self):
        pros_elements = self._browser.find_elements(By.CSS_SELECTOR, self.PROS_SELECTOR)
        pros = [element.text for element in pros_elements]

        return pros

    def _find_yandexGPT_review_cons(self):
        cons_elements = self._browser.find_elements(By.CSS_SELECTOR, self.CONS_SELECTOR)
        cons = [element.text for element in cons_elements]

        return cons
