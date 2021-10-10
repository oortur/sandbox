class Complex:

    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

    def __str__(self):
        return str(self.re) + ' ' + str(self.im) + 'i'

    def __add__(self, other):
        nr = self.re + other.re
        ni = self.im + other.im
        return Complex(nr, ni)

    def __mul__(self, other):
        nr = self.re * other.re - self.im * other.im
        ni = self.re * other.im + self.im * other.re
        return Complex(nr, ni)
