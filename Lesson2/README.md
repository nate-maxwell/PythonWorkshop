# Lesson 2 - Lists, For Loops, and Functions

## Lists

What are **Lists**?
Lists are collections that store multiple items in a single variable. They're
ordered, which means items stay in the order you add them, and you can access
items by their position.

### Creating and Using Lists
```python
favorite_foods = ["Pizza", "Tacos", "Sushi"]
print(favorite_foods)  # Output: ['Pizza', 'Tacos', 'Sushi']
```

### Accessing Items by Index
Lists use zero-based indexing, meaning the first item is at position 0:
```python
print(favorite_foods[0])  # Output: Pizza
print(favorite_foods[1])  # Output: Tacos
print(favorite_foods[2])  # Output: Sushi
```

### Adding Items
The `list` type is a `class`, which we will cover later, but for now know that
lists can have what are called `methods` used from them. Methods are invoked using
a `.` and then the method name like so:

Use `.append()` to add items to the end of a list:
```python
favorite_foods.append("Pasta")
print(favorite_foods)  # Output: ['Pizza', 'Tacos', 'Sushi', 'Pasta']
```

### Removing Items
Use `.remove()` to remove a specific item:
```python
favorite_foods.remove("Tacos")
print(favorite_foods)  # Output: ['Pizza', 'Sushi', 'Pasta']
```

### Getting List Length
Use `len()` to find out how many items are in a list:
```python
num_favorite_foods = len(favorite_foods)
print(num_favorite_foods)  # Output: 3
```

### Checking List Contains Item
Use the `in` keyword to find if an item is in a list:
```python
foods = ["apple", "watermelon", "orange"]
print("apple" in foods)  # Output: True
```
The `not` keyword will invert a boolean. If the boolean is `True`, then it will
become `False`, and if the boolean is `False`, it will become `True`:
```python
foods = ["apple", "watermelon", "orange"]
print("chicken" not in foods)  # Output: True
```

## For Loops

### What are For Loops?
A `for` loop lets you iterate over each item in a list (or other collection) and
do something with each item.

### Looping Through a List
```python
favorite_foods = ["Pizza", "Tacos", "Sushi"]

for food in favorite_foods:
    print(food)

# Output:
# Pizza
# Tacos
# Sushi
```

### The range() Function
`range()` generates a sequence of numbers, useful when you need to loop a specific
number of times:
```python
for i in range(5):
    print(i)

# Output: 0, 1, 2, 3, 4
```

### Numbering List Items
You can use range() with len() to number items:
```python
favorite_foods = ["Pizza", "Tacos", "Sushi"]

for i in range(len(favorite_foods)):
    print(f"{i + 1}. {favorite_foods[i]}")

# Output:
# 1. Pizza
# 2. Tacos
# 3. Sushi
```
**Extra credit**: research the `enumerate` function and rewrite the above code snippet.

## Functions

### What are Functions?
Functions are reusable blocks of code that perform a specific task.
They help organize your code and avoid repetition.

### Defining a Function
Use the `def` keyword to create a function:
```python
def greet():
    print("Hello!")

greet()  # Output: Hello!
```
Text underneath the `def` line are a part of the function, as long as they are
indented below, like `if` statements and loops.

### Function Parameters
Parameters let you pass data into a function:
```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
greet("Bob")    # Output: Hello, Bob!
```

### Return Values
Functions can send data back using the `return` keyword:
```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8
```

### Example: Checking if a Number is Even
```python
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(4))  # Output: True
print(is_even(7))  # Output: False
```

## Type Annotations

You may see functions written with type hints that specify what types of data
go in and come out:
```python
def is_even(number: int) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False
```
The `: int` after `number` says "this parameter should be an integer," and `-> bool:`
says "this function returns a boolean."

These annotations are purely for documentation and tooling - Python doesn't
enforce them, and your code runs exactly the same with or without them.

They're helpful for:
* Making code easier to read and understand
* Catching potential bugs with tools like type checkers
* Getting better auto-completion in your code editor

Additionally, they provide more context for AIs to understand your code.

You don't need to use type annotations as a beginner, but you'll see them in a
lot of professional Python code.

## Let's refactor our number guessing game!

### Why Refactor?
Refactoring means reorganizing your code without changing what it does.
By breaking the number guessing game into functions, we make it easier to
understand, test, and extend.

### Function 1: Get a Valid Guess
```python
def get_guess():
    while True:
        guess = input("Enter your guess: ")
        if guess.isdigit():
            return int(guess)
        else:
            print("Please enter a valid number!")
```

### Function 2: Check the Guess
```python
def check_guess(guess, secret):
    if guess < secret:
        return "low"
    elif guess > secret:
        return "high"
    else:
        return "correct"
```

### Function 3: Main Game Logic
```python
import random


def play_game():    
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("I'm thinking of a number between 1 and 100!")
    
    while True:
        guess = get_guess()
        attempts = attempts + 1
        result = check_guess(guess, secret_number)
        
        if result == "correct":
            print("Correct! You got it in", attempts, "attempts!")
            break
        elif result == "low":
            print("Too low!")
        else:
            print("Too high!")

            
play_game()
```

# Assignment

### Contact List
Build a contact manager using a 2D list (list of lists):
Each contact is stored as a list: `["Name", "Phone", "Email"]`

All contacts stored in one big list:
```python
contacts = [
    ["Alice", "555-1234", "alice@email.com"],
    ["Bob", "555-5678", "bob@email.com"]
]
```

Menu options:
* Add new contact (ask for name, phone, email)
* View all contacts (display in a readable format)
* Search for contact by name
* Delete contact by name
* Quit


Use functions for each operation!

## Challenge
- Add an "update contact" feature:
  - Search for contact by name
  - Ask which field to update (name, phone or email)
  - Update that specific field
