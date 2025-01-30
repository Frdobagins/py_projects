""" ## the below has a floating point math error (2.325 is being rounded to 2.32)

origPrice = float(input('Enter the original price: $'))
discount = float(input('Enter discount percentage: '))
newPrice = float((1 - discount/100)*origPrice)
calculation = f'${origPrice:.2f} discounted by {discount}% is ${newPrice:.2f}.'
print(calculation)
"""


""" ## Fix #1 -- better for the assignment, still bad though. It would give an incorrect answer when 2.5 and 7.5 are inputted
     |-> rounding the "1-discount/100" to two digits

origPrice = float(input('Enter the original price: $'))
discount = float(input('Enter discount percentage: '))
newPrice = float((round(1 - discount/100, 2))*origPrice)
calculation = f'${origPrice:.2f} discounted by {discount}% is ${newPrice:.2f}.'
print(calculation)
"""

""" Fix #2 -- works in vscode, but you can't use the decimal module in activecode
#working code, best answer seems to be to import the decimal module and making the floats into the more exact decimal type
      #LIES, it doesn't work in activecode
from decimal import *
origPrice = Decimal(input('Enter the original price: $'))
discount = Decimal(input('Enter discount percentage: '))
a = discount/100
newPrice = float((1 - discount/100)*origPrice)
calculation = f'${origPrice:.2f} discounted by {discount}% is ${newPrice:.2f}.'
print(calculation)
"""

#works in activecode, should be good enough, rounds it to 15 decimal points, nobody will be getting 5.00102939132993838413% off of something, I hope
origPrice = float(input('Enter the original price: $'))
discount = float(input('Enter discount percentage: '))
newPrice = float((round(1 - discount/100, 15))*origPrice)
calculation = f'${origPrice:.2f} discounted by {discount}% is ${newPrice:.2f}.'
print(calculation)
