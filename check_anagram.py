
#CODE 3

"""
Created on Thu May 28 02:37:27 2020

@author: Mugdha
"""

def check_anagram(data1,data2):
    #start writing your code here
    x = len(data1)
    y = len(data2)
    if(x!=y):
        return False
    else: 
        for i in data1:
            if i not in data2:
                return False
        i = 0
        while(i!=len(data1)):
            if(data1[i] != data2[i]):
                i = i+1
        if(i==len(data1)):
            return True
        else:
            return False
    
    
print(check_anagram("reductions","discounter"))