# -*- coding: utf-8 -*-
"""
Created on Sun May 31 11:07:34 2020

@author: Mugdha
"""
#CODE 6
#PF-Assgn-59
def check_perfect_number(number):
    #start writing your code here
    sum = 0
    list_divisors = []
    for i in range(1,number//2 +1):
        if(number % i ==0):
            list_divisors.append(i)
    #print(list_divisors)
    for div in list_divisors:
        sum = sum + div
    if(sum==number):
        return True
    else:
        return False

def check_perfectno_from_list(no_list):
    #start writing your code here
    list1 = []
    for i in no_list:
        if(i==0):
            pass
        else:
            x = check_perfect_number(i)
            if(x):
                list1.append(i)
    
    return list1


perfectno_list=check_perfectno_from_list([0,18,6,4,2,1,28])
print(perfectno_list)
