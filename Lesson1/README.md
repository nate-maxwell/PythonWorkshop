# Lesson 1 - Variables ,Operators, If Statements, and While Loops

## The `print()` Function
The `print()` function displays text or values to the screen. It's a simple way
to let your program communicates with the user.
```python
print("hello world")  # Output: hello world
```
Functions will be expanded upon in a future lesson, but for now we can use this
to inspect our program.

## Variables

**Strings** are text data enclosed in quotes (`"` or `'`, as long as both match):
```python
first = "hello "
second = 'world'
print(first, second)  # output: hello world
```

**Integers** are whole numbers. They can perform math operations like addition (`+`),
subtraction (`-`), multiplication (`*`), and division (`/`):
```python
age = 25
next_year = age + 1
print(next_year)  # Output: 26
```

**Floats** are decimal numbers. Like integers, they can support multiplication (`*`)
and division (`/`), but are more precise:
```python
price = 19.99
total = price * 2
print(total)  # Output: 39.98
```

## Operators

**Comparison operators** let you compare values:

* `<` less than
* `>` greater than
* `<=` less than or equal to
* `>=` greater than or equal to
* `==` equal to
* `!=` not equal to

These comparisons return **Booleans** - values that are either `True` or `False`.
Booleans are also a type, like string, integer, and float.
```python
happy = True
print(happy)  # output: True
```

### The input() Function
The `input()` function asks the user to type something and returns it as a string:
```python
name = input("What's your name? ")
print(name)
```

### Type Conversion
Since `input()` always returns a string, you need to convert it to use it as a number:
```python
answer = input("What's your age? ")  # saved as string
age = int(answer)  # converted to integer
next_year = age + 1
```

## Control Flow

`if`, `elif`, and `else` Statements

Control flow lets your program make decisions. The `if` statement runs code only
when a condition is `True`. Use `elif` (else-if) for additional conditions, and `else`
as a fallback:
```python
birth_year = int(input("What year were you born? "))

if birth_year >= 1997 and birth_year <= 2012:
    print("You're Gen Z!")
elif birth_year >= 1981 and birth_year <= 1996:
    print("You're a Millennial!")
elif birth_year >= 1965 and birth_year <= 1980:
    print("You're Gen X!")
else:
    print("You're from another generation!")
```
The `and` keyword means both conditions must be true.
Text under the `if`, `elif`, or `else` line must be indented to be executed if
the corresponding condition is met.

### `while` Loops
A `while` loop repeats code as long as a condition is `True`:
```python
count = 0
while count < 5:
    print(count)
    count = count + 1
```

### The `break` Keyword
The `break` keyword immediately exits a loop:
```python
while True:
    age = input("What's your age? (type 'quit' to exit) ")
    if age == "quit":
        break
    print("You entered: ", age)
```

# Assignment: Number Guessing Game

### The random.randint() Function

This function generates a random integer within a range:
```python
import random
secret_number = random.randint(1, 100)  # Random number between 1 and 100
```

## Your Task
Write a program that:

1. Generates a random number between 1 and 100
2. Asks the user to guess the number
3. Tells them if their guess is too high, too low, or correct
4. Keeps asking until they guess correctly

## Challenge
Can you modify your program to limit the user to 8 attempts? If they don't guess
correctly within 8 tries, tell them they've lost and reveal the secret number.
