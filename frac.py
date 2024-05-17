class Frac:
    
    def __init__(self, numer, denom):
        self.numer = numer // gcd(numer,denom)
        self.denom = denom // gcd(numer, denom)

    def __str__(self):
        return f"{self.numer}/{self.denom}"
    
    def add(self, y):
        return Frac(((self.numer*y.denom) + (self.denom*y.numer)),(self.denom*y.denom))

    def sub(self, y):
        return Frac(((self.numer*y.denom) - (self.denom*y.numer)),(self.denom*y.denom))

    def mul(self, y):
        return Frac((self.numer*y.numer),(self.denom*y.denom))

    def div(self, y):
        return Frac((self.numer*y.denom),(self.denom*y.numer))
    
    def __add__(self, y):
        return self.add(y)
        
    def __sub__(self, y):
        return self.sub(y)
    
    def __mul__(self, y):
        return self.mul(y)

    def __truediv__(self, y):
        return self.div(y)
    

def gcd(a,b):
    while b < 0 or b > 0:
        t = b
        b = a % b
        a = t 
    return abs(a)

'''
x = Frac(1,3)
y = Frac(1,3)
z = Frac(1,6)
d = Frac(1,6)
#print((x.add(y)).add(z.add(d)))
print((z.mul(d)).add(x.add(y)))


x = Frac(1, 3)
y = Frac(1, 3)
result = x + y #Försök att använda + på två Frac-objekt
print(result)
'''
sum = Frac(1,3) - Frac(1,3)
print(sum)