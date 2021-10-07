# class
class Complex:
    def __init__(self, *inp):
        if len(inp) == 1:
            self.first = int(inp[0][:inp[0].find(' ')])
            self.second = int(inp[0][inp[0].find(' ') + 1:inp[0].find('i')])
        else:
            self.first = inp[0]
            self.second = inp[1]

    def __str__(self):
        if self.second >= 0:
            return str(self.first) + ' +' + str(self.second) + 'i'
        else:
            return str(self.first) + ' ' + str(self.second) + 'i'

    def __add__(self, new_complex):
        res_complex = Complex(self.first + new_complex.first, self.second + new_complex.second)
        return res_complex

    def __sub__(self, new_complex):
        res_complex = Complex(self.first - new_complex.first, self.second - new_complex.second)
        return res_complex

    def __mul__(self, new_complex):
        if type(new_complex) is int:
            res_complex = Complex(self.first * new_complex, self.second * new_complex)
        else:
            res_complex = Complex(self.first * new_complex.first - self.second * new_complex.second,\
                              self.first * new_complex.second + self.second * new_complex.first)
        return res_complex

    def __rmul__(self, new_complex):
        return self.__mul__(new_complex)
        
