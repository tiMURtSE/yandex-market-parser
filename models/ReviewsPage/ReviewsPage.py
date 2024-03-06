from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from Browser import Browser
from models.YandexMarketProduct.YandexMarketProduct import YandexMarketProduct
from models.Review.Review import Review

class ReviewsPage(Browser):
    NEXT_PAGE_BUTTON_CLASS = "_2prNU._3OFYT"

    def __init__(self, elem_search_delay=5):
        super().__init__(elem_search_delay)

    def get_reviews(self, product: YandexMarketProduct):
        reviews = []

        while True:
            reviews_from_single_page = self._browser.execute_script(self._get_script(id=product.id, article=product.article))
            reviews.extend([Review(product_id=product.id, review=review) for review in reviews_from_single_page])

            next_page_button_element = self._get_next_page_button()
            if next_page_button_element:
                next_page_button_link = next_page_button_element.get_attribute("href")
                self._browser.get(next_page_button_link)
            else:
                break

        return reviews

    def _get_next_page_button(self):
        try:
            next_page_button = self._wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, self.NEXT_PAGE_BUTTON_CLASS))
            )

            return next_page_button
        except:
            return False

    def _get_script(self, id="", article=""):
        script = f"""
            reviews = []

            elems = document.querySelectorAll("._3K8Ed")

            for (const elem of Array.from(elems)) {{
                obj = {{ 
                    "id": "{id}",
                    "product_id": "",
                    "customer_id": "",
                    "customer_name": "",
                    "is_fake_customer": "",
                    "comment": "", 
                    "pros": "", 
                    "cons": "",
                    "review_status": "",
                    "moderator_id": "",
                    "rate": "" ,
                    "moderator_comment": "",
                    "order_id": "",
                    "type": "",
                    "z:article": "{article}",
                }}
            
                obj["customer_name"] = elem.querySelector("._1UL8e._1mJcZ").textContent
                obj["pros"] = elem.querySelectorAll("dl[data-auto='review-pro'] > dd")[0]?.textContent
                obj["cons"] = elem.querySelectorAll("dl[data-auto='review-contra'] > dd")[0]?.textContent
                obj["comment"] = elem.querySelectorAll("dl[data-auto='review-comment'] > dd")[0]?.textContent
                obj["rate"] = elem.querySelectorAll("._3Q7P8 path._3DSnN._2BvsM").length

                reviews.push(obj)
            }}

            console.log(reviews)
            return reviews
        """

        return script

