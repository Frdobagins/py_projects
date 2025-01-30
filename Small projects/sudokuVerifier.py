import math as m

""" Reverse a string with a recursive function

def rec_rev(str):
    if str == "":
        return ""
    else:
        return rec_rev(str[1:]) + str[0]

string = "hello"
print(rec_rev(string))
print(string[::-2]) 
"""


""" reverse a string with a loop
def loop(s):
    n = ""
    for i in range(len(s)):
        if i % 2 != 0:
            continue
        n += s[i]
    return n

print(loop("abcdefghi"))

def rec(s):
    if len(s) == 0:
        return ""
    n = s[0] + rec(s[2:])
    return n
print(rec("abcdefghi" ))
"""


""" outputs a string of numbers in a specfic manner to a file
def count_writer(file, n):
    count = 0
    nstring = ""
    while count < n:
        count += 1
        nstring += str(count)
        if count % 10 != 0:
            nstring += "*"
        else:
            nstring += "\n"

    with open('file', 'w') as fil:
        fil.write(nstring)

count_writer('file.txt', 13)
"""


''' sort a list of numbers in an odd way (the smallest in the center)
num = input("number list?")
numlist = num.split(" ")
numlist.sort()
print(numlist)
newlst = []
while len(numlist) > 0:
    if len(newlst) % 2 != 0:
        print(True)
        newlst.insert(0, numlist.pop(0))
        print(newlst)
    else:
        print(False)
        newlst.append(numlist.pop(0))
        print(newlst)
print(newlst)
'''

"""sudoku verifier""" # can be as big or small as you want


def sudokuVerifier(lol): #lol = list of lists
    if len(lol) != len(lol[0]): #make sure its square
        print("Your puzzle is not square")
        return 

    checkAgainst = [i for i in range(1, len(lol[0])+1 )]

    #create rotated version list
    rotated = [[num[i] for num in lol] for i in range(len(lol[0]))] #list comprehension^2

    #create boxes; I want to see if I can make this with list comprehensions
    boxRows = int(m.sqrt(len(lol)))
    boxColumns = int(m.sqrt(len(lol[0])))
    ''' I dislike the lack of multiline comments in python
    boxes = []
    #I will make it with for loops first, the box number collection is a bit hard to picture


    """After I wrote this I realized that it would be much clearer to have not use i, j, and k as iterators"""
    for i in range(0, boxRows): # three (assuming 9x9) large vertical sections
        for j in range(0, boxColumns): # three (assuming 9x9) large horizontal sections
            miniBox = []
            for k in range(0, boxRows): # the rows in smaller box
                miniBox.extend(lol[k+i*boxRows][j*boxColumns : (j+1)*boxColumns])
            boxes.append(miniBox)
            print(f'i = {i}')
            print(f'j = {j}')
            print(f'k = {k}')
            print(miniBox)
    print("Boxes:")
    print(boxes)
    """is it even possibly to condense that mess into a list comprehension? I'm sure it is"""
    boxes2 = [
        [
            [
                lol[row+boxrow * boxRows][boxcolumn * boxColumns : (boxcolumn + 1) * boxColumns] 
                for row in range(0, boxRows)
            ]for boxcolumn in range(0, boxColumns)
        ] for boxrow in range(0, boxRows)
            ]
    print("Boxes?: ")
    print(boxes2)      
    """That technically works, but there are a huge amount of brackets cause its a list of lists of lists"""  
    '''
    
    """better idea, use the if feature at the end""" #I got sidetracked, realized I could used double for statements without the brackets, wooo
    br = boxRows # also, using that if feature would be terrible for optimization, I'd be iterating througha bunch of things without using them 
    bc = boxColumns #not that that matters, this is python after all. If I wanted optmization, I'd use c++
    boxes3 = [[lol[sr + r*br][sc + c * bc] for sr in range(0, br) for sc in range(0, bc)] for c in range(0, bc) for r in range(0, br)]

    # I did it!!
    # that was horrible, I learned a lot abour list comprehensions tho
    #print("boxes??:")
    #print(boxes3)


    #check rows
    for i in lol:
        if sorted(i) != checkAgainst:
            return False
        
    #check columns
    for i in rotated:
        if sorted(i) != checkAgainst:
            return False
        
    #check boxes
    for i in boxes3:
        if sorted(i) != checkAgainst:
            return False
    
    #print(rotated)
    return True



ssb = [ [5, 3, 4, 6, 7, 8, 9, 1, 2], 
        [6, 7, 2, 1, 9, 5, 3, 4, 8], 
        [1, 9, 8, 3, 4, 2, 5, 6, 7], 
        [8, 5, 9, 7, 6, 1, 4, 2, 3], 
        [4, 2, 6, 8, 5, 3, 7, 9, 1], 
        [7, 1, 3, 9, 2, 4, 8, 5, 6], 
        [9, 6, 1, 5, 3, 7, 2, 8, 4], 
        [2, 8, 7, 4, 1, 9, 6, 3, 5], 
        [3, 4, 5, 2, 8, 6, 1, 7, 9] ]
print(ssb)
print(sudokuVerifier(ssb))


solved_sudoku_4x4 = [
    [1, 2, 3, 4],
    [3, 4, 1, 2],
    [2, 3, 4, 1],
    [4, 1, 2, 3]
]

print(solved_sudoku_4x4)
print(sudokuVerifier(solved_sudoku_4x4))

