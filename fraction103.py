class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def show(self):
        print(self.num, "/", self.den)

    def __str__(self):
        return str(self.num) + " / " + str(self.den)

    def gcd(self, m, n):
        while m % n != 0:
            oldm = n
            oldn = m

            m = oldn
            n = oldm % oldn
            return n


    def __add__(self, otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = self.gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)


f1 = Fraction(1, 4)
f2 = Fraction(1, 2)
f3 = f1 + f2
print(f3)
