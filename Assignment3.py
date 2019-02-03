# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 11:16:37 2019

#loops - use break (terminates the loop), continue (returns control to the beginning of loop) and pass (null in the code blocks) functions to control the iterations

@author: Mamedov
"""

'''#in class assignments
stars = eval(input('Enter a number of stars. The program ends if it is a zero:'))
if stars<0:
    raise Exception('The number of stars should not be a negative number')
elif stars==0:
    pass
else:
    for row in range (stars):
        if row%2==0:
            pass
        print ('*'*(stars-row)) '''      
        
#3.1 
def getPentagonalNumber(n):
    for i in range (1,n+1):
        print (int(i*(3*i-1)/2)," ", end =""),
        if i%10==0:
            print()
            
getPentagonalNumber(100)

#3.2
#Return the reversal of an integer, e.g. reverse(456) returns # 654 
def reverse(n):
    st = str(n)
    if st is None or len(st) == 0:
        raise Exception ('The string is empty.')
    st = list(st)
    s=0
    f=len(st)-1
    temp=''
    while f>s:
        temp=st[f]
        st[f] = st[s]
        st[s] = temp
        f-=1
        s+=1
    st=''.join(st)
    st = int (st)
    return st

print (reverse(654))

# Return true if number is a palindrome 
def isPalindrome(number):
    rev = reverse (number)
    if rev==number:
        return True
    else:
        return False
    
print (isPalindrome (666))
    