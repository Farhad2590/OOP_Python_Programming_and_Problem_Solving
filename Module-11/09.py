from tkinter import N


class Instance:
    def __int__(self, x,n):
        self.x = x
        self.n = n 

    def sum(self):
        sum = self.x + self.n
        return(sum)

    def Pow(self):
        power = pow(self.x, self.n)
        return(power)

x = int(input())
n = int(input())

call = Instance(x, n)

print(call.sum())
print(call.Pow)