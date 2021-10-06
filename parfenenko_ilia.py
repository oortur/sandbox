class Complex_New:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        self.real += other.real
        self.imag += other.imag
        return self

    def __sub__(self, other):
        self.real -= other.real
        self.imag -= other.imag
        return self

    def __mul__(self, other):
        k = self.real * other.real - self.imag * other.imag
        t = self.real * other.imag + self.imag * other.real
        self.real = k
        self.imag = t
        return self

    def __str__(self):
        if self.imag == 0:
            out = str(self.real)
        elif self.real == 0:
            if self.imag > 0:
                out = str(self.imag) + 'j'
            elif self.imag < 0:
                out = '-' + str(self.imag) + 'j'
        else:
            if self.imag > 0:
                out = str(self.real) + ' + ' + str(self.imag) + 'j'
            elif self.imag < 0:
                out = str(self.real) + ' - ' + str(self.imag) + 'j'
        return out