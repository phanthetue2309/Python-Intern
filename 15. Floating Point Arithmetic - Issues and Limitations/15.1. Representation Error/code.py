from decimal import Decimal
from fractions import Fraction

print( Fraction.from_float(0.1))


print( (0.1).as_integer_ratio())


print( Decimal.from_float(0.1) )


print( format(Decimal.from_float(0.1), '.17'))