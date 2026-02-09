'''
Product store
Design & create an online store for Products (name, price).
Track total products being created.
Create a static method to calculate discount on each product based on a % parameter.
'''


class product:
    count = 0
    def __init__(self,name,price):
        self.name = name
        self.price = price
        product.count += 1

    def get_info(self): #instance method
        print(f"price of {self.name} is Rs.{self.price}")

    @classmethod
    def get_count(cls):
        print(f"total product in store = {cls.count}")

    @staticmethod
    def calc_discount(price,discount):
        final_price = price - (discount * price / 100)
        print(f"discount price = {final_price}")


p1 = product("phone", 10_000)
p2 = product("laptop", 50_000)
p3 = product("pen", 10)

p1.get_info()
product.get_count()

p1.calc_discount(p1.price, 10)
    