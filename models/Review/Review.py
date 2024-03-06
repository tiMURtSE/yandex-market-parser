class Review:
    def __init__(self, product_id: int, review: dict):
        self._product_id = product_id
        self._customer_name = review["customer_name"]
        self._comment = review["comment"]
        self._rate = review["rate"]
        self._pros = review["pros"]
        self._cons = review["cons"]

    