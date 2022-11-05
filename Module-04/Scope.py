# Global Variable
balance = 580
def total_cost(price, quantity):
    global balance
    cost = price * quantity
    balance = balance - cost
    # print(remaining)
    return cost

print(f'Blance outside before: {balance}')

pay = total_cost(10,3)
print(f'Please pay:{pay}')

print(f'Blance outside after: {balance}')