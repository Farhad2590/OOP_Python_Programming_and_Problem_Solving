class shop:
    cart = []

    def __init__(self, buyer):
        self.buyer = buyer
    def add_to_cart(self, item):
        self.cart.append(item)

shopper_1 = shop('Ma - Moni general store')
shopper_1.add_to_cart('t shirt')
print(shopper_1.cart)

shopper_2 = shop('Moni general store')
shopper_2.add_to_cart('Shoes')
print(shopper_2.cart)