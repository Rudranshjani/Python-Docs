class Number:
    def __init__(self, start): # On Number(start)
        self.data = start
    def __sub__(self, other):
        return (self.data - other)

X = Number(5) # Number.__init__(X, 5)
Y = X + 2        # Number.__sub__(X, 2)
print(Y)
