# --- SECTION 1: String & List Conversion ---
# From your screenshot: Converting strings to lists
developer_name = "jessica"
print(list(developer_name))  # Output: ['j', 'e', 's', 's', 'i', 'c', 'a']

developer_as_list = ["jessica"]
print(list(developer_as_list)) # Output: ['jessica']

# --- SECTION 2: List Sizing & Basic Indexing ---
# From your screenshot: Using len() and basic indexing
numbers = [1, 2, 3, 4, 5, 6]
print(f"List length: {len(numbers)}") # Output: 6

# --- SECTION 3: Tuple Mastery (Unpacking & Slicing) ---
# From your screenshot: Working with immutable Tuples
tuble_info = ('ali', 13, 'hamza', 'java dev')
print(f"Index 1 in tuple: {tuble_info[1]}") # Output: 13

# Tuple Unpacking: Professional way to assign variables
dev_profile = ('alisa', 19, 'femme', 'morocco')
name, age, sexe, nationality = dev_profile
print(f"Unpacked: {name}, {age}, {sexe}, {nationality}")

# Tuple Slicing
desserts = ('cake', 'pie', 'cookies', 'ice cream')
print(f"Sliced Desserts: {desserts[1:3]}") # Output: ('pie', 'cookies')

# --- SECTION 4: List Modification & Removal ---
# From your screenshot: Using 'del' to remove items
dev_list = ['ali', 19, 'femme', 'morocco']
del dev_list[1] # Removing '19'
print(f"List after 'del': {dev_list}") # Output: ['ali', 'femme', 'morocco']

# --- SECTION 5: Advanced Sorting & Counting ---
# From your screenshot: Counting elements and professional sorting
dev_skills = ("java", "javascript", "rest", "php", "c", "php")
print(f"Occurrences of 'php': {dev_skills.count('php')}") # Output: 2

# Sorting by character length (key=len)
languages = ['java', 'javascript', 'python', 'c++']
languages.sort(key=len)
print(f"Sorted by length: {languages}")

#reversing (reverse= True)
programming_language = ["java", "javascript", "python", "c++","rast","c"]
print(sorted(programming_language,reverse=True))
#################################
for char in "ali ennadafy":
  print(char)
###################################
categoris = ['Fruit', 'Vegetable']
names =["hamza", "ali", "fatimazahra", "oussama"]
#####################################
for categori in categoris:
  for cat in names:
    print(categori,cat)
####################################"
dev = ["java", "javascript", "python", "c++"]
for devlopeur in dev:
  if devlopeur == "python":
    break;
  print(devlopeur)
  #########################################
dev = ["dev", "nodejs", "nextjs","typescript"]
for item in dev:
  if item == "nextjs":
    continue
  print(item)
######################################
words = ['sky', 'apple', 'rhythm', 'fly', 'orange']

for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f"'{word}' contains the vowel '{letter}'")
            break
    else:
        print(f"'{word}' has no vowels")
##################################################
for num in range(5):
  print(num)
###########################################
for num in range(1,5):
  print(num)
#############################################
for num in range(2,12,2):
  print(num)
#########################################
for num in range(3):
  pass
print(num)
############################################
numbers = (1,2,3,4,5)
print(numbers[2])
############################################
name = "jessica"
print(tuple(name))
print(list(name))
print(set(name))
#############################################
number = list(range(2,11,2))
print(number)
##########################################
name = ["lock", "weak","father", "sister"]
print(list(enumerate(name)))
#######################################
even_numbers = [num for num in range(21) if num % 2 == 0]
print(even_numbers)
#####################################
name = ["ali", "oussama", "fatima", "yahya"]
for names in name:
  print(names)
######################################
name = ["ahmed","ali","oussama","aymen"]

index = 0

for names in name:
  print(f"index {index} :{names}")
  index += 1
###################################
number = [1,2,3,4,5,6]

result = [(number ,"even") if number % 2 == 0 else (number , "odd") for number in number]
print(result)
#####################################
words = ["hmed", "lamin", "full", "the", "life", "inside"]

def is_long(words):
  return len(words) > 3

res = list(filter(is_long,words))
print(res)
#############################
celsius = [0, 10, 20, 30, 40]

def is_celsius(celsius):
  return (celsius * 9/5) + 32

res = list(map(is_celsius,celsius))
print(res)
######################################
number = [29,39,938,93,48,92]
res = sum(number)
print(res)

number = [29,39,938,93,48,92]
res = sum(number,10)
print(res)

number = [29,11, 12,14,93,957]
res = sum(number, start=2)
print(res)
#####################################
numbers =[19,3,9,18,26,86,20,199]
numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

numbers =[19,3,9,18,26,86,20,199]
print(numbers.index(20))

names = ["ali", "oussama", "fatima", "yahya"]
names.index("yahya")

numbers.pop()
print(numbers)
###########################################
developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

for name, id in zip(developers, ids):
    print(f'Name: {name}')
    print(f'ID: {id}')
###########################################
numbers = [1, 2, 3, 4, 5]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]
