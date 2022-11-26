class Shopper:
    def __init__(self, name):
        self.name = name
        self.cart = []
    
    def add_to_cart (self, item, price, quantity):
        self.cart.append({'P.Name': item,'P.Price' : price, 'P.Quantity' : quantity })
        # self.item = item
        # self.price = price
        # self.quantity = quantity

    def checkout(self,amount):
        price = 0
        for item in self.cart:
            print (item)
            price = price + item['P.Price'] * item ['P.Quantity']
        if amount < price:
            return f'Please Give Me More {price - amount} taka'
        elif amount > price:
            return f'Here is your item and Thank You For Purchasing. Here is your retun {amount - price} taka'
        else:
            return 'Here is your item and Than you for Purchasing'
        # print (price)

shopping = Shopper('MA_Moni')
shopping.add_to_cart('Shirt',400,3)
shopping.add_to_cart('Jins_pant',700,2)
shopping.add_to_cart('Shoes',1200,1)

reply = shopping.checkout(5000)
print(reply)