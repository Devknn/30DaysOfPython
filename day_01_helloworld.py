"""
💻 Exercises - Day 1
Exercise: Level 1
Check the python version you are using
Open the python interactive shell and do the following operations. The operands are 3 and 4.
addition(+)
subtraction(-)
multiplication(*)
modulus(%)
division(/)
exponential(**)
floor division operator(//)
Write strings on the python interactive shell. The strings are the following:
Your name
Your family name
Your country
I am enjoying 30 days of python
Check the data types of the following data:
10
9.8
3.14
4 - 4j
['Asabeneh', 'Python', 'Finland']
Your name
Your family name
Your country
Exercise: Level 2
Create a folder named day_1 inside 30DaysOfPython folder. Inside day_1 folder, create a python file helloworld.py and repeat questions 1, 2, 3 and 4. Remember to use print() when you are working on a python file. Navigate to the directory where you have saved your file, and run it.
Exercise: Level 3
Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
Find an Euclidian distance between (2, 3) and (10, 8)
"""


#Exercise: Level 2

#1

#python3 --version

#2
import math


n1,n2 = 3,4

addition = n1 + n2
subtraction = n1 - n2
multiplication = n1 * n2
division = n1 / n2
exponential = n1 ** n2
floor_division = n1 // n2

#3
name = "kenier".title()
family_name = ["oscar","jean","marleny","carlos"].append("sindy")
country = "Venezuela"
enjoy = "I am enjoying 30 days of python".split()

#4
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type([]))
print(type(name))
print(type(family_name))
print(type(country))

#Exercise: Level 3
#1
integer = 1
floats = 0.1
complexs = 5 + 5j
string = "python"
boolean = True
lists = []
tuples = ()
set = {}
dictionary = {"key":"value"}

#2

euclidean_distance = math.sqrt((2 - 10) ** 2 + (3 - 8) ** 2)
print(euclidean_distance)

