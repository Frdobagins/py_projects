'''def are_anagrams(str1, str2): 
    for i in str1: 
        if i not in str2:
            return False
        if str1.count(i) != str2.count(i):
            return False
    for j in str2:
        if j not in str1:
            return False      
    return True'''

def are_anagrams(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())


test1 = are_anagrams("listen", "silent") 
print(test1) # Output: True 
test2 = are_anagrams("hello", "world") 
print(test2) # Output: False