"""
💻 Exercises: Day 6
Exercises: Level 1
Create an empty tuple
Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
Join brothers and sisters tuples and assign it to siblings
How many siblings do you have?
Modify the siblings tuple and add the name of your father and mother and assign it to family_members
Exercises: Level 2
Unpack siblings and parents from family_members
Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
Change the about food_stuff_tp tuple to a food_stuff_lt list
Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
Slice out the first three items and the last three items from food_staff_lt list
Delete the food_staff_tp tuple completely
Check if an item exists in tuple:
Check if 'Estonia' is a nordic country

Check if 'Iceland' is a nordic country

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

"""

#1
tuples = ()

#2
sister = ("Grisley","Grismar","Rosa","Yulys")
brothers = ("Alfredo","Jean","José","Pepe")

#3
siblings = sister + brothers
#4
print(f"I've: {len(siblings)} siblings")

#5
father = ("Carlos",)
mother = ("Marleny",)
family_members = siblings + father + mother

#Level 2

#1
*siblings, father, mother = family_members

#2
fruits = ("apple","pear","orange",)
vegetables = ("apio","onion","potato")
animal = ("cow","dog","cat","lion","dolphin","shark")
food_stuff_tp = fruits + vegetables + animal

#3
food_stuff_lt = list(food_stuff_tp)

#4
middle_tp = len(food_stuff_tp) // 2
middle_lt = len(food_stuff_lt) // 2
del food_stuff_lt[middle_lt]
print(food_stuff_lt)
#la tupla no es modificable
print(food_stuff_tp)

#5
print(f"The first three items: {food_stuff_lt[:3]}")
print(f"The last three items: {food_stuff_lt[-3:]}")

#6
del food_stuff_tp

#7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
a = lambda : "Estonia" in nordic_countries
print(a())    






