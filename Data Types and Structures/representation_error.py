#Problem 1
a = 1-0.9
print(a)

1-0.9 == 0.1

#Problem 2
import decimal

x = decimal.Decimal(3.14); y = decimal.Decimal(2.74)

print(x * y)

decimal.getcontext().prec = 4

print(x * y)

#Problem 3
import fractions

fractions.Fraction(3,4) #Creates the fraction 3/4

fractions.Fraction(0.5) #Creates a fraction from a float

fractions.Fraction(".25") #Creates a fraction from a string