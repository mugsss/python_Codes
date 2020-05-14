# -*- coding: utf-8 -*-
"""
Created on Mon May 11 15:29:24 2020

@author: Mugdha
"""
"""
Write a python function, nearest_palindrome() which accepts a number and returns the nearest palindrome greater than the given number
"""

def nearest_palindrome(number):
    #start writitng your code here
    while True:
        sum1 = 0
        p = number
        while(p!=0):
            r= p % 10
            sum1 = sum1*10 + r
            p = p//10
        if(sum1 == number):
            print(sum1)
            break
        else:
            number = number + 1
            

number=12331
nearest_palindrome(number)

