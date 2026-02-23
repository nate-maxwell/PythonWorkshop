# Lesson 1 - Variables, Operators, If Statements, and While Loops

# Motivations

The goal of this workshop is to teach python in the most primitive form. We will
not spend long on each topic, meaning we will not expand on all possible features
the language offers for each topic.

The goal is to make developers able to write program that work, not write the
best version of those programs. As developers grow and explore the language,
they will inevitably learn better ways to write their programs over time.

Independent research is always encouraged.

## The `print()` Function
The `print()` function displays text or values to the screen. It's a simple way
to let your program communicates to the user.
```python
print("hello world")  # Output: hello world
```
Functions will be expanded upon in a future lesson, but for now we can use this
to inspect our program.

## Variables

Variables are pieces of data that we have stored for later use. All variables
have a type and the type defines what actions we can perform with it.

**Strings** are text data enclosed in quotes (`"` or `'`, as long as both match):
```python
first = "hello"
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

**Math operators** are the arithmetic operators:

* `+`  Addition
* `-`  Subtraction
* `/`  Division
* `//` Integer division
* `*`  Multiplication
* `**` Power

I encourage you to experiment with operators and types as they can work in
surprising ways.

For example `print("50" + 8)` will raise an error because python cannot determine
if you want the string `"508"` or the integer `400`.
`print("50" * 8)` will work, however, as strings multiplied by a number will
repeat that number of times, therefore this will output `"5050505050505050"`.

All division will create a float, including dividing integers that would result
in no remainder. `print(10 / 2)` will output `5.0` instead of `5`. Using the
integer division operator will discard the remainder: `print(10 // 2)  # Output: 5`.

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

### The type() Function
The `type()` function returns the type of a value.
This can help us inspect or debug values as we work on them.

```python
greeting_type = type("hello world")
print(greeting_type)  # Output: <class 'str'>
```

### Type Conversion
The `input()` always returns a string. Therefore, if we need the input as some
other type of data, we need to convert it. We can convert the string to an
integer like so:
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
birth_year = int(input("What year were you born"))

if birth_year >= 2006:
    print("You are not old enough to drink...")
elif birth_year <= 2004:
    print("You are old enough to drink...")
else:
    print("You might be old enough to drink...")
```

The `and` keyword means both conditions must be true.
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
    answer = input("What's your age? (type 'quit' to exit) ")
    if answer == "quit":
        break
    print("You entered:", answer)
```

# Assignment: Number Guessing Game

### The random.randint() Function

This function generates a random integer within a range:
```python
import random
secret_number = random.randint(1, 100)  # Random number between 1 and 100
```

# Assignment
Write a program that:

1. Generates a random number between 1 and 100
2. Asks the user to guess the number
3. Tells them if their guess is too high, too low, or correct
4. Keeps asking until they guess correctly

## Challenge
Can you modify your program to limit the user to 8 attempts? If they don't guess
correctly within 8 tries, tell them they've lost and reveal the secret number.
