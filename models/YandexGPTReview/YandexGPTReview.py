class YandexGPTReview:
    def __init__(self, product_id: int):
        self._product_id = product_id
        self._pros = []
        self._cons = []

    @property
    def pros(self):
        return self._pros
    
    @pros.setter
    def pros(self, value):
        self._pros = value

    @property
    def cons(self):
        return self._cons
    
    @cons.setter
    def cons(self, value):
        self._cons = value

    def set_review(self, review: dict):
        pros = review["pros"]
        cons = review["cons"]

        self._pros = pros
        self._cons = cons