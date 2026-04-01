##1. Largest among Three Numbers: Write a Python program that takes three numbers as input 
##and prints out the largest among them.

A= int(input("A= "))
B= int(input("B= "))
C= int(input("C= "))
if A>B and A>C:
    print ("A is the largest among them")
elif B>A and B>C:
    print ("B is the largest among them")
else:
    print ("C is the largest among them")