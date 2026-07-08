# Basic Python Program

# 1. Variables and Data Types
name = "Harry"
age = 25
height = 5.9
is_student = True

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Is Student: {is_student}")

# 2. Basic Arithmetic
a = 10
b = 5
print(f"\nAddition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")

# 3. String Operations
greeting = "Hello"
name_str = "Python"
full_greeting = greeting + " " + name_str
print(f"\n{full_greeting}")
print(f"Length: {len(full_greeting)}")

# 4. Lists
fruits = ["apple", "banana", "cherry", "date"]
print(f"\nFruits: {fruits}")
print(f"First fruit: {fruits[0]}")
print(f"Number of fruits: {len(fruits)}")

# 5. For Loop
print("\nFruits list:")
for fruit in fruits:
    print(f"  - {fruit}")

# 6. Functions
def greet(name):
    """Function to greet someone"""
    return f"Hello, {name}!"

def add(x, y):
    """Function to add two numbers"""
    return x + y

print(f"\n{greet('World')}")
print(f"Sum of 20 and 30: {add(20, 30)}")

# 7. Conditionals
score = 85
if score >= 90:
    print("\nGrade: A")
elif score >= 80:
    print("\nGrade: B")
elif score >= 70:
    print("\nGrade: C")
else:
    print("\nGrade: F")

# 8. While Loop
print("\nCounting from 1 to 5:")
count = 1
while count <= 5:
    print(count, end=" ")
    count += 1
print()

# 9. Dictionary
person = {
    "name": "Harry",
    "age": 25,
    "city": "New York"
}
print(f"\nPerson Dictionary: {person}")
print(f"Name: {person['name']}, Age: {person['age']}")

# 10. List Comprehension
squares = [x**2 for x in range(1, 6)]
print(f"\nSquares of 1-5: {squares}")
