class Phone:
    Brand = "Xiomi"
    Color = "Sky Blue"
    Price = 18500

    def call(self):
        print('ring ring ring')

    def send_sms(self, number, text):
        sms = f'sending sms : {text}. To: {number}'
        return sms

my_phone = Phone()
my_phone.call()
sms = my_phone.send_sms('01829313336','I missed to miss you')
print(sms)
