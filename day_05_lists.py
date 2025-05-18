"""
💻 Exercises: Day 5
Exercises: Level 1
Declare an empty list

Declare a list with more than 5 items

Find the length of your list

Get the first item, the middle item and the last item of the list

Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

Print the list using print()

Print the number of companies in the list

Print the first, middle and last company

Print the list after modifying one of the companies

Add an IT company to it_companies

Insert an IT company in the middle of the companies list

Change one of the it_companies names to uppercase (IBM excluded!)

Join the it_companies with a string '#;  '

Check if a certain company exists in the it_companies list.

Sort the list using sort() method

Reverse the list in descending order using reverse() method

Slice out the first 3 companies from the list

Slice out the last 3 companies from the list

Slice out the middle IT company or companies from the list

Remove the first IT company from the list

Remove the middle IT company or companies from the list

Remove the last IT company from the list

Remove all IT companies from the list

Destroy the IT companies list

Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.

Exercises: Level 2
The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
Sort the list and find the min and max age
Add the min age and the max age again to the list
Find the median age (one middle item or two middle items divided by two)
Find the average age (sum of all items divided by their number )
Find the range of the ages (max minus min)
Compare the value of (min - average) and (max - average), use abs() method
Find the middle country(ies) in the countries list
Divide the countries list into two equal lists if it is even if not one more country for the first half.
['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
"""

#1
lists = []

#2
new_list = ['orange','apple','pear','strawberry','watermelon']

#3
print(len(new_list))

#4
print(f"First item: {new_list[0]}")
print(f"Middle item: {new_list[len(new_list) // 2]}")
print(f"Last item: {new_list[-1]}")

#5
mixed_data_types = ["kenier", 32, 1.71, False, "roque hernandez 16"]

#6
it_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle , Amazon".replace(" ","").split(",")

#7
print(it_companies)

#8
print(len(it_companies))

#9
print(f"First item: {it_companies[0]}")
middle = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    print(f"Middle item: {it_companies[middle - 1]}, {it_companies[middle]}")
else:
    print(f"Middle item: {it_companies[middle]}")

print(f"Last item: {it_companies[-1]}")

#10
it_companies[it_companies.index("Facebook")] = "TikTok"
print(it_companies)

#11
it_companies.append("Samsung")
print(it_companies)

#12
it_companies.insert((len(it_companies) // 2), "Hp")
print(it_companies)

#13
it_companies[len(it_companies)//2] = it_companies[len(it_companies)//2].upper()
print(it_companies)

#14
join = "#".join(it_companies)
print(join)

#15
print(f"{'certain' in it_companies}")

#16
it_companies.sort()
print(it_companies)

#17
it_companies.sort(reverse=True)
print(it_companies)

#18
print(it_companies[:3])

#19
print(it_companies[-3:])

#20
middle = len(it_companies) // 2
it_companies.pop(middle)
print(it_companies)

#21
del it_companies[0]
print(it_companies)

#22
middle = len(it_companies) // 2
del it_companies[middle]
print(it_companies)

#23
del it_companies[-1]
print(it_companies)

#24
it_companies.clear()
print(it_companies)

#25
del it_companies

#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
join_lists = front_end + back_end
print(join_lists)

#27
full_stack = join_lists.copy()
full_stack.append("SQL")
full_stack.append("Redux")
print(full_stack)

#Level 2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#Ordenamos lista
ages.sort()

#Agregamos la min y la max a la lista
min_age = min(ages)
max_age = max(ages)
ages.append(min_age)
ages.append(max_age)

#Ordenamos la lista
ages.sort()

#Mediana edad
middle = len(ages) // 2
if len(ages) % 2 == 0:
    print(f"The median age is: {(ages[middle-1]+ages[middle]//2)}")
else:
    print(f"The median age is: {ages[middle]}")

# Calcular el promedio
average = sum(ages) / len(ages)
print(f"Average age: {average:.2f}")

# Calcular el rango
range_ = max_age - min_age
print(f"Range: {range_}")


# Comparar |min - avg| y |max - avg|
print(f"|Min - Average| = {abs(min_age - average):.2f}")
print(f"|Max - Average| = {abs(max_age - average):.2f}")

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];
length = len(countries)

middle = length // 2
if length % 2 == 0:
    middle = length // 2
    print(f"The middle country is: {countries[middle - 1]},{countries[middle]}")
    first_half = countries[:middle]
    second_half = countries[middle:]
else:
    print(f"The middle country is: {countries[middle]}")
    first_half = countries[:middle + 1]
    second_half = countries[middle + 1:]


print(f"Total countries: {length}")
print(f"First half ({len(first_half)} countries): ")
print(f"Second half ({len(second_half)} countries): ")

china, russia, usa, *scandic_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

print(scandic_countries)
