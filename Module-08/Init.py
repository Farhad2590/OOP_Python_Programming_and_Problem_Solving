class Phone:

    manufactarer = 'china'

    def __init__(self,brand,price,colour):
        self.brand = brand
        self.price = price
        self.colour = colour
        

    def send_sms(self, number, text):
        sms = f'sending sms : {text}. To: {number}'
        return sms
my_phone = Phone( 'Oppo', 13000, 'blue')
print(my_phone.brand,my_phone.manufactarer)

her_phone = Phone( 'xiomi', 20000, 'purple')
print(her_phone.brand,her_phone.manufactarer)

dad_phone = Phone( 'iphone', 1000000, 'White')
print(dad_phone.brand,dad_phone.manufactarer)