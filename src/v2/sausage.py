from src.v2.pizza import Pizza

class Sausage(Pizza):
    def __init__(self, pizza):
        self.base = pizza
    def is_veggetarian(self):
        return not self.base.is_veggetarian()
    def calculate_price(self):
        return(1.5 + self.base.calculate_price())