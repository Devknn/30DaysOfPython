"""
💻 Exercises - Day 2
Exercises: Level 1
Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
Write a python comment saying 'Day 2: 30 Days of python programming'
Declare a first name variable and assign a value to it
Declare a last name variable and assign a value to it
Declare a full name variable and assign a value to it
Declare a country variable and assign a value to it
Declare a city variable and assign a value to it
Declare an age variable and assign a value to it
Declare a year variable and assign a value to it
Declare a variable is_married and assign a value to it
Declare a variable is_true and assign a value to it
Declare a variable is_light_on and assign a value to it
Declare multiple variable on one line
Exercises: Level 2
Check the data type of all your variables using type() built-in function
Using the len() built-in function, find the length of your first name
Compare the length of your first name and your last name
Declare 5 as num_one and 4 as num_two
Add num_one and num_two and assign the value to a variable total
Subtract num_two from num_one and assign the value to a variable diff
Multiply num_two and num_one and assign the value to a variable product
Divide num_one by num_two and assign the value to a variable division
Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
Calculate num_one to the power of num_two and assign the value to a variable exp
Find floor division of num_one by num_two and assign the value to a variable floor_division
The radius of a circle is 30 meters.
Calculate the area of a circle and assign the value to a variable name of area_of_circle
Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
Take radius as user input and calculate the area.
Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords

"""
#Exercises: Level 1


#2

#Day 2: 30 Days of python programming

#3
import math


first_name = "kenier".title()

#4
last_name = "noriega navarro".title()

#5
full_name = first_name + last_name

#6
country = "venezuela".title()

#7
city = "maturín".title()

#8
age = 32

#9
year = 1993

#10 
is_married = False

#11
is_true = True

#12
is_light_on = True

#13
value_one, value_two = "hello","python"

#Exercises: Level 2

#1
type(first_name)
type(last_name)
type(full_name)
type(country)
type(city)
type(age)
type(year)
type(is_married)
type(is_true)
type(is_light_on)
type(value_one)
type(value_two)

#2
len(first_name)

##3
len(first_name) == len(last_name)

#4
num_one = 5
num_two = 4

#5
variable_total = num_one + num_two

#6
variable_diff = num_two - num_one

#7
variable_product = num_two * num_one

#8
variable_division = num_one / num_two

#9
variable_remainder = num_two % num_one

#10
variable_exp = num_one ** num_two

#11
floor_division = num_one // num_two

#12
radius = int(input("Enter the radius of a circle: "))
area_of_circle = math.pi * (radius ** 2)
circum_of_circle = 2 * math.pi * radius

#13
first_name = input("Enter your name: ").title()
last_name = input("Enter your last name: ").title()
country = input("Enter your country: ").title()
age = int(input("Enter your age: "))
user_info = f"My name is {first_name + ' ' + last_name}. I'm From {country} and I'm {age} old years"
print(user_info)

#14
help('keywords')

