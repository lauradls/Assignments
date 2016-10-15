# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 21:45:28 2016

@author: laura
"""

my_list=range(1, 100)

lower = my_list[0]
upper = my_list[98]

guess= (lower+upper)/2


Greeting = "Hello! To test my abilities, think of a number from 1 to 100 and \
I will guess it. Everytime you see my guess, type LOWER, HIGHER or YES so \
I can have a few hints."

print(Greeting)

attempt = "Is your number %s?" % (guess)
print ("")
number = input(attempt)


while (number != 'YES'):
    if number == 'LOWER':
        upper = (guess-1)
        guess= int((lower+upper)/2)
    elif number == 'HIGHER':
        lower = (guess+1)
        guess= int((lower+upper)/2)
    else:
        print ("Is it LOWER or HIGHER?. If this is your number, type YES. \
REMEMBER TO TYPE YOUR ANSWER IN CAPITAL LETTERS")
    print  ("Is your number %s ?" % (guess))
    number = input()
    print ("")
 
print ("I guessed it! Your number is", guess, "!")

