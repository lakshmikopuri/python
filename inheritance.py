#inheriance
class Product:
    def __init__(self, name, price, deal_price, ratings):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.ratings = ratings
        self.you_save = price - deal_price
    def display_product_details(self):
        print("Product: {}".format(self.name))
        print("Price: {}".format(self.price))
        print("Deal Price: {}".format(self.deal_price))
        print("You Saved: {}".format(self.you_save))
        print("Ratings: {}".format(self.ratings))

class ElectronicItem(Product):
    def __init__(self, name, price, deal_price, ratings):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.ratings = ratings
        self.you_save = price - deal_price
    def display_product_details(self):
        print("Product: {}".format(self.name))
        print("Price: {}".format(self.price))
        print("Deal Price: {}".format(self.deal_price))
        print("You Saved: {}".format(self.you_save))
        print("Ratings: {}".format(self.ratings))
    def set_warentry(self,warentry_in_months):
        self.warentry_in_months=warentry_in_months
    def get_warentry(self):
        return self.warentry_in_months
class GroceryItem(Product):
    def __init__(self, name, price, deal_price, ratings):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.ratings = ratings
        self.you_save = price - deal_price
    def display_product_details(self):
        print("Product: {}".format(self.name))
        print("Price: {}".format(self.price))
        print("Deal Price: {}".format(self.deal_price))
        print("You Saved: {}".format(self.you_save))
        print("Ratings: {}".format(self.ratings))
    def set_expairt_date(self,expiry_date):
        self.expiry_date=expiry_date
    def get_expirydate(self):
        return self.expiry_date
e = ElectronicItem("camers", 25, 20, 3)
e.display_product_details()
e.set_warentry(24)
print(e.get_warentry())
g = GroceryItem("milk", 25, 20, 3)
g.display_product_details()
g.set_expairt_date(3)
print(g.set_expairt_date())