class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price


    def __str__(self):
        return f"{self.brand} {self.model} costs {self.price}"

    def afficher(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)


l = Laptop("Apple", "MacBook Air", 12000)
print(l)
l.afficher()

