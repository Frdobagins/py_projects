""" Goal, Make a recurive function that changes a base 10 int to other bases"""

def baseChange(n, baseAim):
    convStr = "0123456789ABCDEF"
    if n < baseAim:
        return convStr[n]
    #the base case, it starts to leave once it gets here
    else:
        return baseChange(n//baseAim, baseAim) + convStr[n%baseAim]
    #Create the output with a chain of returns, you dive down and then come back out
    #accumulator, but without the accumulator
'''
      I need to be better at these  ^^^ they are hard to wrap my head around
'''

def baseChangeWhile(n, baseAim):
    convStr = "0123456789ABCDEF"
    output = ""
    while n >= baseAim:
        output = convStr[n%baseAim] + output
        n = n//baseAim
    output = convStr[n] + output
    return output

#print(baseChangeWhile(66, 2))
#print(baseChange(66, 2))


""" sum through recursion """
def sumloop(lst):
    total = 0
    for i in lst:
        total += i
    return total

def sumRec(lst):
    if lst != []:
        return lst.pop() + sumRec(lst)
    return 0
'''^^ That is short as frick ^^'''

alist = [12, 43, 100, 6542, 23, 542, 23, 456443]
#print(sumloop(alist))
#print(sumRec(alist))

""" alphabetize a string through recursion"""
####  I need to learn how to sort things before I do this ####
def alphaloop(Str):
    Strlist = []
    srt1 = []
    srt2 = []
    for i in Str:
        Strlist += i
    for i in Strlist:
        if i < "n":
            srt1 += i
        else: 
            srt2 += i
        
    print(srt1)
    print(srt2)
    return Strlist



dealph = "rtyujkmnbvcxdfrtyujkmnbvcfgtyhujmnbvc"
#print(alphaloop(dealph))


"""
Other Prjoect Ideas???
"""


"""Calculating change"""


"""Factiorals"""
def factorial(n):
    if n <= 1: 
        return 1
    return n*factorial(n-1)

print(factorial(4))

"""tower of hanoi"""

