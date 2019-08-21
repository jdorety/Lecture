from product import Product


class Equipment(Product):
    def __init__(self, name, price, material, weight):
        super().__init__(name, price)
        self.material = material
        self.weight = weight

    def __str__(self):
        parent_str = super().__str__()
        return f"{parent_str} and it weighs {self.weight}"
