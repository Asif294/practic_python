# Variables & Data Types
x = 10          # int
y = 3.14        # float
name = "Asif"   # str
is_active = True # bool

# Strings
text = "  Hello World  "
print(text.upper())   # HELLO WORLD
print(text.lower())   # hello world
print(text.title())   # Hello World
print(text.strip())   # "Hello World"
print(text.replace("World", "Asif")) # Hello Asif
print(text.split())   # ['Hello', 'World']

# f-string:
age = 21
print(f"My name is {name}, I am {age}")

# Booleans & if-else
x, y = 5, 10

if x < y:
    print("x is smaller")
elif x == y:
    print("Equal")
else:
    print("x is greater")

# Tuples, Lists, Sets, Dictionaries
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")
fruits.remove("banana")
print(fruits[0])   # indexing
print(fruits[1:3]) # slicing

# Tuple
numbers = (1, 2, 3)
print(numbers[0])  # immutable

# Set
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1.union(s2))        # {1,2,3,4,5}
print(s1.intersection(s2)) # {3}

# Dictionary
student = {"name": "Asif", "age": 21}
print(student["name"])
print(student.get("age"))
print(student.keys())
print(student.values())

# Loops
for i in range(5):
    print(i)  # 0,1,2,3,4

# while loop
count = 0
while count < 5:
    print(count)
    count += 1

# Functions
def greet(name):
    return f"Hello {name}!"

print(greet("Asif"))


# Default Parameter:

def add(a, b=10):
    return a + b

print(add(5)) # 15
