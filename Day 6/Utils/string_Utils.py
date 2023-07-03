# Create a package called "utils" that contains the following modules:
# string_utils.py: Implement utility functions for string manipulation, such as reversing a string, counting the occurrence of a character, etc.
# file_utils.py: Implement utility functions for file handling, such as reading and writing files, listing directory contents, etc.
# math_utils.py: Implement utility functions for mathematical operations, such as finding the factorial of a number, checking if a number is prime, etc.
def reverse(s):
    s = list(s)
    s = s[::-1]
    s = ''.join(s)
    return s


def occurrence(s):
    # s = 'sunny'
    n = input('enter the chr u want occurance of:')
    if(n not in s):
        return 'char not present in given string'
    count = 0
    for i in range(0,len(s)):
        # print(s[i])
        if(s[i] == n):
            count+=1
        
    return n,count