class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        result = []
        for i in range(len(self.products)):
            if first_letter == self.products[i][0]:
                result.append(self.products[i])

        return result

    def __repr__(self):
        return f"Items in the {self.name} catalogue:\n" + '\n'.join(sorted([i for i in self.products]))


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)