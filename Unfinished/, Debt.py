#will be able to calculate one's student debt over time asking for payments akd decisions as to where it goes.

# to learn
    # 1 OOP (Classes to make the different loans and organize that)
    # 1 logic
    # 1 ask for input
    # 3 output graphs
    # 3 good interface 

class Loan:
    def __init__(self, i, debt):
        self.i = i
        self.debt = debt
        pass
    
ls = 0
li = 0
years = 5
currentYear = 0
# put inside a loop 
while currentYear < years:
        #each year is a loop
        #option to add new loans 
            #choose loan type
            #interest
            #amount
        #option to pay loand
    ls = input("Loan Size?" + "\n")
    li = input("Interest Rate?" + "\n" )

    loan1 = Loan(ls, li)
    print("Interest Rate" + "\n" + loan1.i)
    print("Total Debt" + "\n" + loan1.debt)
    currentYear += 1