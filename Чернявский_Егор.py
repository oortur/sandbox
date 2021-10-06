class Complex:
    def __init__(self, a, b=None):
        if b == None:
            a = a.replace(' ', '')
            b = a.replace('+', '-')
            k = b.rfind('-')
            c, d = a[:k], a[k:len(a)]
            if 'i' in c:
                self.realpart = int(d)
                self.complpart = int(c[:-1])
            else:
                self.realpart = int(c)
                self.complpart = int(d[:-1])
        else:
            self.realpart = a
            self.complpart = b

    def __str__(self):
        if self.complpart < 0:
            s = str(self.realpart) + '-' + str(abs(self.complpart)) + 'j'
        else:
            s = str(self.realpart) + '+' + str(self.complpart) + 'j'
        return s

    def __add__(self, other):
        a = self.realpart + other.realpart
        b = self.complpart + other.complpart
        return Complex(a, b)

    def __sub__(self, other):
        a = self.realpart - other.realpart
        b = self.complpart - other.complpart
        return Complex(a, b)

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            a = self.realpart * other
            b = self.complpart * other
        else:
            a = self.realpart * other.realpart - self.complpart * other.complpart
            b = self.realpart * other.complpart + self.complpart * other.realpart
        return Complex(a, b)

    def __rmul__(self, other):
        return self.__mul__(other)

