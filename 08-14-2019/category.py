class Category:
    def __init__(self, name, products):
        self.name = name
        self.products = products

    def __str__(self):
        if not self.products:
            return "No products available in " + self.name
        else:
            return f"{self.name} has products: {",".join(self.products)}"
