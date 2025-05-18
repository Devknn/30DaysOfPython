"""
💻 Exercises: Day 9
Exercises: Level 1
Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive.
Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

Enter your age: 30
You are 5 years older than me.
Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

Enter number one: 4
Enter number two: 3
4 is greater than 3
Exercises: Level 2
Write a code which gives grade to students according to theirs scores:

80-100, A
70-89, B
60-69, C
50-59, D
0-49, F
Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

The following list contains some fruits:

```sh
fruits = ['banana', 'orange', 'mango', 'lemon']
```

If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
Exercises: Level 3
Here we have a person dictionary. Feel free to modify it!
        person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
 * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 * If the person is married and if he lives in Finland, print the information in the following format:
    Asabeneh Yetayeh lives in Finland. He is married.
"""
#1
age = 15 #input("Enter your age: ")
if age >= 18:
    print("You are old enough to drive.")
elif age <= 0:
    print("You can't enter a negative number.")
else:
    print(f"You need {18 - age} more years to learn to drive.")


#2
my_age = 25 #input("Enter your age: ")
your_age =30 #input("Enter your age: ")
if my_age == your_age:
    print("We've the same age.")
elif my_age > your_age:
    print(f"I'm {my_age - your_age} years older than you.")
elif my_age < your_age:
    print(f"You're {your_age - my_age} years older than me.")

"""#3
value_one = int(input("Enter number one: "))
value_two = int(input("Enter number two: "))
if value_one > value_two:
    print(f"{value_one} is greater than {value_two}")
elif value_one < value_two:
    print(f"{value_one} is smaller than {value_two}")
elif value_one == value_two:
    print(f"{value_one} is equal than {value_two}")
else:
    print("Enter valid value.")

   
#Level 2

#1
scores_student = 1
if scores_student >= 80 and scores_student <= 100:
    print("A")
elif scores_student >= 70 and scores_student <= 79:
    print("B")
elif scores_student >= 60 and scores_student <= 69:
    print("C")
elif scores_student >= 50 and scores_student <= 59:
    print("D")
elif scores_student >= 0 and scores_student <= 49:
    print("F")

#2
season = input("Enter the season: ").title()
if season in ["September", "October", "November"]:
    print("The season is Autumn")
elif season in ["December", "January", "February"]:
    print("The season is Winter.")
elif season in ["March", "April", "May"]:
    print("The season is Spring.")
elif season in ["June", "July", "August"]:
    print("The season is Summer.")
else:
    print("Invalid season")


#4
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruits = input("Add fruit: ")
if new_fruits in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(new_fruits)
    print(fruits)
"""
#Level 3

person={
    'first_name': 'Kenier',
    'last_name': 'Noriega',
    'age': 32,
    'country': 'Venezuela',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'roque hernandez 16',
        'zipcode': '61005'
    }
    }
#
middle = len(person["skills"]) // 2
print(person["skills"][middle])

#
print("Python" in person["skills"])

#
skills = set(person['skills'])

if skills == {"JavaScript", "React"}:
    print('He is a front end developer')
elif skills == {"Node", "Python", "MongoDB"}:
    print('He is a backend developer')
elif {"React", "Node", "MongoDB"}.issubset(skills):
    print('He is a fullstack developer')
else:
    print('unknown title')


#
if person['is_marred'] and person["country"] == "Venezuela":
    print(f"{person['first_name']} {person['last_name']} lives in Finland. He is married.")
