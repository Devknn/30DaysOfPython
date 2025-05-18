"""
💻 Exercises - Day 4
Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
Declare a variable named company and assign it to an initial value "Coding For All".
Print the variable company using print().
Print the length of the company string using len() method and print().
Change all the characters to uppercase letters using upper() method.
Change all the characters to lowercase letters using lower() method.
Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
Cut(slice) out the first word of Coding For All string.
Check if Coding For All string contains a word Coding using the method index, find or other methods.
Replace the word coding in the string 'Coding For All' to Python.
Change Python for Everyone to Python for All using the replace method or other methods.
Split the string 'Coding For All' using space as the separator (split()) .
"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
What is the character at index 0 in the string Coding For All.
What is the last index of the string Coding For All.
What character is at index 10 in "Coding For All" string.
Create an acronym or an abbreviation for the name 'Python For Everyone'.
Create an acronym or an abbreviation for the name 'Coding For All'.
Use index to determine the position of the first occurrence of C in Coding For All.
Use index to determine the position of the first occurrence of F in Coding For All.
Use rfind to determine the position of the last occurrence of l in Coding For All People.
Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
Does ''Coding For All' start with a substring Coding?
Does 'Coding For All' end with a substring coding?
'   Coding For All      '  , remove the left and right trailing spaces in the given string.
Which one of the following variables return True when we use the method isidentifier():
30DaysOfPython
thirty_days_of_python
The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
Use the new line escape sequence to separate the following sentences.
I am enjoying this challenge.
I just wonder what is next.
Use a tab escape sequence to write the following lines.
Name      Age     Country   City
Asabeneh  250     Finland   Helsinki
Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.
Make the following using string formatting methods:
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
"""

#1
string_value_one = 'Thirty' +" "+ 'Days' +" "+ 'Of' +" "+ 'Python'
print(string_value_one)

#2
string_value_two = 'Coding' +" "+ 'For' +" "+ 'All' 
print(string_value_two)

#3
company = string_value_two

#4
print(company)

#5
print(len(company))

#6
print(f"Method Upper 'AA' {company.upper()}")

#7
print(f"Method lower 'aa'{company.lower()}")

#8
print(f"Method capitalize 'Aa bb' {company.capitalize()}")
print(f"Method title 'Aa Bb' {company.title()}")
print(f"Method swapcase 'aA bB' {company.swapcase()}")

#9
print(f"Cut(slice): {company[6::]}")

#10
print(f"Method find: {company.find('Coding')}")
print(f"Method index: {company.index('Coding')}")
print(f"Operations identity: {'Coding' in company }")

#11
print(f"Method remplace: {company.replace('Coding','python'.title())}")

#12
None

#13
print(f"Method split: {company.split()}")

#14
print(f"Spliting word: {'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'.split(',')}")

#15
print(f"The character at index 0 in the string Coding For All: {'Coding For All'[0]}")

#16
print(f"The character at last index 0 in the string Coding For All: {'Coding For All'[-1]}")

#17
print(f"The character at index 10 in the string Coding For All: {'Coding For All'[10]}")

#18
for acronym in 'Python For Everyone':
    print(acronym[0])

#19
for acronym in 'Coding For All':
    print(acronym[0])

#20
print(f"Using index to determine the position of the first occurrence of C in Coding For All: {'Coding For All'.index('C')}")

#21
print(f"Using index to determine the position of the first occurrence of C in Coding For All: {'Coding For All'.index('F')}")

#22
print(f"Using rfind to determine the position of the last occurrence of l in Coding For All People: {'Coding For All People'.rfind('l')}")

#23
print(f"Using index to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction': {'You cannot end a sentence with because because because is a conjunction'.index('because')}")
print(f"Using find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction': {'You cannot end a sentence with because because because is a conjunction'.find('because')}")

#24
print(f"Using rfind to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction': {'You cannot end a sentence with because because because is a conjunction'.rfind('l')}")

#25
print(f"Using replace: Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction' {'You cannot end a sentence with because because because is a conjunction'.replace('because because because','')}")

#26
print(f"Using find: Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction' {'You cannot end a sentence with because because because is a conjunction'.find('because')}")

#27
print(f"Using replace: Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction': {'You cannot end a sentence with because because because is a conjunction'.replace('because because because','')}")

#28
print(f"Using startswith: Does 'Coding For All' start with a substring Coding?: {'Coding For All'.startswith('Coding')}")

#29
print(f"Using endswith: Does 'Coding For All' end with a substring coding: {'Coding For All'.endswith('coding')}")

#30
print(f"Using strip:'   Coding For All      '  , remove the left and right trailing spaces in the given string.: {'   Coding For All      '.strip()}")

#31
print("""
Which one of the following variables return True when we use the method isidentifier():
30DaysOfPython
thirty_days_of_python
""")
print(f"With 30DaysOfPython: {'30DaysOfPython'.isidentifier()}")
print(f"With thirty_days_of_python: {'thirty_days_of_python'.isidentifier()}")


#32
libraries =  ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
hash = "#"
print(hash.join(libraries))

#33
print("I am enjoying this challenge.\nI just wonder what is next.")

#34
print("Name\t\tAge\t\tCountry\t\tCity\nAsabeneh\t250\t\tFinland\t\tHelsinki")

#35
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

#36
n1,n2 = 8,6
print(f"""
{n1} + {n2} = {n1 + n2}
{n1} - {n2} = {n1 - n2 }
{n1} * {n2} = {n1 * n2 }
{n1} / {n2} = {n1 / n2 }
{n1} % {n2} = {n1 % n2 }
{n1} // {n2} = {n1 // n2 }
{n1} ** {n2} = {n1 * n2 }""")

