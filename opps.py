#oops
class Mobile:
    def __init__(self, model, camera):
        self.model = model
        self.camera= camera
    def make_cal(self,number):
        print("calling..{}".format(number))

mobile_obj = Mobile("iPhone 12 Pro","12 MP")
mobile_obj.make_cal(976388225)
mobile_obj = Mobile("iPhone 13 Pro","64 MP")
mobile_obj.make_cal(75906708)
#class mob:
    def __inint__(self,model,storage):
        self.model=model
        self.storage=storage
obj=mob("galaxy m51","128gb")
print(obj.model)
#updating model
class Mobile:
    def __init__(self, model, camera):
        self.model = model
        self.camera= camera
    def make_cal(self,number):
        print("calling..{}".format(number))
    def get_model(self):
        print(self.model)
    def update_mode(self,model):
        self.model=model
obj_1=Mobile("Galaxy m51","64 mp")
obj_1.update_mode("galaxy j17")
print(obj_1.model)
#creating a cart and add nd delete the product
lass Cart:
    def __init__(self):
        self.items = {}
        self.price_details = {"book": 500, "laptop": 30000}

    def add_item(self, item_name, quantity):
        self.items[item_name] = quantity

    def remove_item(self, item_name):
        del self.items[item_name]

    def update_quantity(self, item_name, quantity):
        self.items[item_name] = quantity

    def get_cart_items(self):
        cart_items = list(self.items.keys())
        return cart_items

    def get_total_price(self):
        total_price = 0
        for item, quantity in self.items.items():
            total_price += quantity * self.price_details[item]
        return total_price


cart_obj = Cart()
cart_obj.add_item("book", 3)
cart_obj.add_item("laptop", 1)
print(cart_obj.get_total_price())
cart_obj.remove_item("laptop")
print(cart_obj.get_cart_items())
cart_obj.update_quantity("book", 2)
print(cart_obj.get_total_price())