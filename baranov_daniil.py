class Complex(object):

    def __init__(self, a, b = 0):
        if type(a) == type("string"):
            s = a.split()
            self.real = float(s[0])
            if s[1][-1] == "i":
                k = float(s[1][0:-1])
            else:
                k = float(s[1])
            self.img = k
        else:
            self.real = a
            self.img = b

    def __add__(a, b):
        return Complex(a.real + b.real, a.img + b.img)
    
    def __sub__(a, b):
        return Complex(a.real - b.real, a.img - b.img)

    def __mul__(a, b):
        if type(b) != Complex:
            return Complex(a.real * b, a.img * b)
        return Complex(a.real * b.real - a.img * b.img, a.real * b.img + a.img * b.real)

    __rmul__ = __mul__

    def __str__(self):
        if self.img > 0:
            s = str(self.real) + " +" + str(self.img) + "i"
        else:
            s = str(self.real) + " " + str(self.img) + "i"
        return s

a = Complex(1, 9)
b = Complex("2 9i")
print(a + b)
print(a - b)
print(a * b)
