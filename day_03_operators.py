"""
💻 Exercises - Day 3
Declare your age as integer variable
Declare your height as a float variable
Declare a variable that store a complex number
Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
    Enter base: 20
    Enter height: 10
    The area of the triangle is 100
Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
Enter side a: 5
Enter side b: 4
Enter side c: 3
The perimeter of the triangle is 12
Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
Calculate the slope, x-intercept and y-intercept of y = 2x -2
Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
Compare the slopes in tasks 8 and 9.
Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
Find the length of 'python' and 'dragon' and make a falsy comparison statement.
Use and operator to check if 'on' is found in both 'python' and 'dragon'
I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
There is no 'on' in both dragon and python
Find the length of the text python and convert the value to float and convert it to string
Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
Check if type of '10' is equal to type of 10
Check if int('9.8') is equal to 10
Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
Enter hours: 40
Enter rate per hour: 28
Your weekly earning is 1120
Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
Enter number of years you have lived: 100
You have lived for 3153600000 seconds.
Write a Python script that displays the following table
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
"""

#💻 Exercises - Day 3
import math


#1
age = 32

#2
height = 1.71

#3
complexs = 4 - 4j

#4
base = float(input("Enter base: "))
height = float(input("Enter height: "))
area_triangle =  f"The area of a triangle is: {int(0.5 * base * height)}"

#5
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
perimetre_triangle = f"The perimeter of the triangle is: {int(a + b + c)}"

#6 
length_rectangle = float(input("Enter length: "))
width_rectangle = float(input("Enter width: "))
area_rectangle = f"The area of a rectangle is: {int(length_rectangle * width_rectangle)}"
perimeter_rectangle = f"The perimeter of a rectangle is: {int(2 * (length_rectangle + width_rectangle))}"

#7
radius_circle = float(input("Enter radius: "))
area_circle = f"The area of a circle is: {(math.pi * (radius_circle ** 2)):.2f}"
circumference = f"The circumference of a circle is: {(2 * math.pi * radius_circle):.2f}"

#8
None
#9
x1, x2 = 2, 6
y1, y2 = 2, 10
slope = f"The slope is: {(y2-y1) / (x2 - x1)}"
euclidean_distance = f"The euclidean distance is: {math.sqrt((y1 - x1)** 2 + (y2 - x2)** 2)}"

#10
None
#11
None
#12
print(len("python") != len("dragon"))

#13
"on" in "python" and "on" in "dragon"

#14
"jargon" in "I hope this course is not full of jargon."

#15
"on" not in "python" and "on" not in "dragon"

#16
str(float(len("python")))

#17
numbers = float(input("Enter number: "))
numbers_divisible = lambda: "It's divisible" if numbers % 2 == 0 else "It's not divisible"
print(numbers_divisible)

#18
floor_division = 7 // 3
lambda: floor_division == int(2.7)

#19
lambda: "10" == 10

#20
lambda: float('9.8') == 10

#21
hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
pay_of_the_person = f"Your weekly earning is: {hours * rate}"

#22
number_of_years = int(input("Enter number of years you have lived: "))
number_of_seconds_person = f"You have lived for {number_of_years * 365 * 24 * 60 * 60} seconds."

#23
for i in range(1,6):
    print(f"{i} {1} {i} {i*i} {i*i*i}")