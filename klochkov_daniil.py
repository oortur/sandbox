class Complex:
    def __init__(self, *a):
        if len(a) == 2:
            self.r = a[0]
            self.i = a[1]
        else:
            x = a[0].split()
            self.r = float(x[0])
            self.i = float(x[1].rstrip('j'))

    def __add__(self, x):
        return Complex(self.r + x.r, self.i + x.i)

    def __mul__(self, x):
        if type(x) == Complex:
            return Complex(self.r * x.r - self.i * x.i, self.r * x.i + self.i * x.r)
        else:
            return Complex(self.r * x, self.i * r)

    def __sub__(self, x):
        return Complex(self.r - x.r, self.i - x.i)

    def __str__(self):
        return str(self.r) + ' ' + str(self.i) + 'j'
