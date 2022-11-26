class Calculator:
    def add(self, num1,num2):
        sum = num1 + num2
        return sum

    def multi(self, num1,num2):
        mul = num1 * num2
        return mul

    def divi(self, num1,num2):
        divi = num1 / num2
        return divi

    def sub(self, num1,num2):
        sub = num1 - num2
        return sub


make_cal = Calculator()

sum = make_cal.add(10,20)
sub = make_cal.sub(30,10)
mul = make_cal.multi(5,4)
div = int(make_cal.divi(100,10))

print(f'sum:{sum},div:{div},mul:{mul},sub:{sub}')