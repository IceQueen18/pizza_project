from src.v2.pizza import Pizza

class Pepperoni(Pizza):
    def __init__(self, pizza):
        self.base = pizza
    def is_veggetarian(self):
        return not self.base.is_veggetarian()
    def is_dairy_free(self):
        return True
    def calculate_price(self):
        return(0.0 + self.base.calculate_price())