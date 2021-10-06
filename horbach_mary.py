class Complex:
    def __init__(self, *args):
        if len(args) == 1:
            if isinstance(args[0], str):
                if args[0].find("-") != -1:
                    x, y = args[0].split("-")
                    self.re = int(x)
                    self.im = - int(y[0])
                else:
                    x, y = args[0].split("+")
                    self.re = int(x)
                    self.im = int(y[0])
            else:
                x = int(args[0])
                self.re = x
                self.im = 0
        else:
            self.re = args[0]
            self.im = args[1]

    def __add__(self, other):
        return Complex((self.re + other.re), (self.im + other.im))

    def __sub__(self, other):
        return Complex((self.re - other.re), (self.im - other.im))

    def __mul__(self, other):
        if not isinstance(other, Complex):
            other = Complex(other)
        a = self.re
        b = self.im
        c = other.re
        d = other.im
        return Complex(a * c - b * d, a * d + b * c)

    def __str__(self):
        x = str(self.re)
        y = str(abs(self.im))
        if self.im > 0:
            return x + "+" + y + "i"
        else:
            return x + "-" + y + "i"