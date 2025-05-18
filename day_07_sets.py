"""
💻 Exercises: Day 7
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
Exercises: Level 1
Find the length of the set it_companies
Add 'Twitter' to it_companies
Insert multiple IT companies at once to the set it_companies
Remove one of the companies from the set it_companies
What is the difference between remove and discard
Exercises: Level 2
Join A and B
Find A intersection B
Is A subset of B
Are A and B disjoint sets
Join A with B and B with A
What is the symmetric difference between A and B
Delete the sets completely
Exercises: Level 3
Convert the ages to a set and compare the length of the list and the set, which one is bigger?
Explain the difference between the following data types: string, list, tuple and set
I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

"""

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

#1
print(len(it_companies))

#2
it_companies.add("Twitter")
print(it_companies)

#3
it_companies.update({"Hp","Lenovo","Samsung"})
print(it_companies)

#4
it_companies.discard("Youtube")
print((it_companies))

#discard no lanza error a no conseguir el items buscado
#remove lanza error a no conseguir el items buscado


#Level 2
a = {19, 22, 24, 20, 25, 26}
b = {19, 22, 20, 25, 26, 24, 28, 27}

#1
print(a.union(b))

#2
print(b.intersection(a))

#3
print(a.issubset(b))
print(b.issubset(a))

#4
print(a.isdisjoint(b))
print(b.isdisjoint(a))

#6
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

#7
del a,b

#Level 3

age = [22, 19, 24, 25, 26, 24, 25, 24]

#1
age_set = set(age)
comparation = lambda: "The list is bigger " if len(age) > len(age_set)  else "The set is bigger"
print(comparation())

#2
string = "Hola"
lista = [1, 2, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

#3
frase= "I am a teacher and I love to inspire and teach people".split()
unique_word = set(frase)
print(f"unique words: {len(unique_word)}")