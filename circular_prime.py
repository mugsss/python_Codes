# -*- coding: utf-8 -*-
"""
Created on Thu May 28 17:12:50 2020

@author: Mugdha
"""

#PF-Assgn-57
#CODE 5

def check_prime(number):
    flag = 0
    for i in range(2,number//2 + 1):
        if(number%i == 0):
            flag=1
            break
    if(flag==1):
        return False
        #print("Not Prime")
    else:
        return True
        #print("Prime")
    #remove pass and write your logic here. if the number is prime return true, else return false




def rotations(num):
    x = str(num) #print(x)
    p = list(x) 
    #print(p)
    
    rotation_final = []
    hey =  ''.join(p)
    rotation_final.append(hey)
    
    for i in range(0,len(p)-1):
        rotation_list = []
        for i in range(0,len(p)-1):
            rotation_list.append(p[i+1])

     
        rotation_list.append(p[0])
        #print(rotation_list)
        p = rotation_list
        hey =  ''.join(rotation_list)
        rotation_final.append(hey)
    #hey =  ''.join(p)
    #print(hey)
    
    #list(map(int,rotation_final))
    return rotation_final
    #remove pass and write your logic here. It should return the list of different combinations of digits of the given number.
	#Rotation should be done in clockwise direction. For example, if the given number is 197, the list returned should be [197, 971, 719]

def get_circular_prime_count(limit):
    p = []
    check = []
    final_list =[]
    for i in range(2,100):
        x = check_prime(i)
        if(x):
            p.append(i)
    #print(p)
    for i in p:
        
        rotate_list = rotations(i)
        #print(rotate_list)
        check = []
        
        for i in rotate_list:
            num = int(i)
            x = check_prime(num)
            if(x):
                
                check.append(1)
            else:
                check.append(0)
            count = 0
            for i in check:
                if(i == 1):
                    count =count+1
            if(count == len(rotate_list)):
                for i in rotate_list:
                    final_list.append(i)
    final= list(set(final_list))
    length = len(final)
    return length
    

               
        
    
#remove pass and write your logic here.It should return the count of circular prime numbers below the given limit.

#Provide different values for limit and test your program
    
print(get_circular_prime_count(100))
