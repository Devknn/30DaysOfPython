"""
💻 Exercises: Day 8
Create an empty dictionary called dog
Add name, color, breed, legs, age to the dog dictionary
Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
Get the length of the student dictionary
Get the value of skills and check the data type, it should be a list
Modify the skills values by adding one or two skills
Get the dictionary keys as a list
Get the dictionary values as a list
Change the dictionary to a list of tuples using items() method
Delete one of the items in the dictionary
Delete one of the dictionaries

"""
#1
dog = {}

#2
dog.update({"name" : "barney", "color" : "beige", "legs" : 4, "age" : 32})
print(dog)

#3
student = dict()
student.update({"first_name": "kenier",
                "last_name": "noriega",
                "gender": "masculino",
                "age": 32,
                "marital_status": False,
                "skills": ["fire","air","wind","water"],
                "country": "venezuela",
                "city": "monagas",
                "address": "roque hernandez 16"
                })

#4
print(len(student))
print(type(student))

#5
print(student["skills"][0])
print(type(student["skills"]))

#6
student["skills"][0] = "land"
print(student["skills"])

#7
print(student.keys())

#8
print(student.values())

#9
print(student.items())

#10
del student["city"]
print(student)


#11
del student

