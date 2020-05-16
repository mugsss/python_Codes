# -*- coding: utf-8 -*-
"""
Created on Sat May 16 13:40:59 2020

@author: Mugdha
"""

def sms_encoding(data):
    #start writing your code here
    vowels =  list("aeiouAEIOU")
    sms_encode = []
    p = data.split()
    for i in range(0,len(p)):
        
        if p[i] in ['a','e','i','o','u','A','E','I','O','U']:
            sms_encode.append(p[i])
        
        else:
            q=[]
            c_list =[]
            for letter in p[i]:
                q.append(letter)
                
            

            for letter in q:
                if(letter not in vowels):
                    c_list.append(letter)
                    #q.remove(letter)
                    
            
            x= "".join(c_list)
            sms_encode.append(x)
    x = ' '.join(sms_encode)
    return (x)

                
        
        
data="I love Python"
print(sms_encoding(data))