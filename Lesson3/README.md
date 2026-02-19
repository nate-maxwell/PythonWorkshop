# Lesson 3 - Modules and Classes

## Modules

### What are Modules?
Modules are Python files that contain collections of related functions, classes,
and variables. They help you organize code and reuse functionality without
rewriting it.

### Importing Built-in Modules
Python comes with many built-in modules. You've already used random:
```python
import random
number = random.randint(1, 100)
```
### The math Module
```python
import math

print(math.sqrt(16))      # Output: 4.0
print(math.pi)            # Output: 3.141592653589793
print(math.ceil(4.2))     # Output: 5 (rounds up)
print(math.floor(4.8))    # Output: 4 (rounds down)
```

### The datetime Module
```python
import datetime

now = datetime.datetime.now()
print(now)  # Output: 2026-02-16 14:30:45.123456

today = datetime.date.today()
print(today)  # Output: 2026-02-16
```

### Different Ways to Import

### Standard Import - Access functions using the module name:
```python
import math
result = math.sqrt(25)
```
In `math.sqrt()`, the `math.` part is the namespace of the `sqrt()` function.

### Import Specific Items - Use functions directly without the module prefix:
```python
from math import sqrt, pi
result = sqrt(25)
print(pi)
```
This only exposes the imported items into your file. Other items in the math
module are not imported in this example.
```python
from math import sqrt, pi
print(ceil(4.2))  # Produces and error
```

### Import Everything - Imports all functions from a module:
```python
from math import *
result = sqrt(25)
```
Note: many developers have strong opinions about `import *` as it can make your
code harder to read and may cause naming conflicts, but in some cases it can help.
I personally think namespaces are a resource and should be utilized.

### Creating Your Own Module
You can create your own modules by saving functions in a .py file.

Create a file called game_utils.py:
```python
def get_guess() -> int:
    while True:
        guess = input("Enter your guess: ")
        if guess.isdigit():
            return int(guess)
        else:
            print("Please enter a valid number!")

def check_guess(guess: int, secret: int) -> str:
    if guess < secret:
        return "low"
    elif guess > secret:
        return "high"
    else:
        return "correct"
```
Then import and use it in another file:
```python
import game_utils

secret = 42
guess = game_utils.get_guess()
result = game_utils.check_guess(guess, secret)
print(result)
```
Files that exist in the same folder can be imported as-is. Files located in
another directory require that the folder be added to the `PYTHONPATH` environment
variable. We will expand more on this later.

## Classes

What are Classes?
Classes are blueprints for creating objects. They bundle data (variables) and
functionality (methods) together.

Think of a class as a template - like a cookie cutter - and objects as the
individual cookies made from that template.

### Class Structure
You can define a class using the `class` keyword like so:
```python
class Player(object):
    def __init__(self, name):
        self.name = name
        self.score = 0
    
    def add_points(self, points):
        self.score = self.score + points
    
    def get_info(self):
        print(f"{self.name} has {self.score} points")
```

### The `__init__()` Constructor
The `__init__()` method is special - it runs automatically when you create a new
instance of the class. It's where you set up the initial state of your object:
```python
def __init__(self, name: str) -> None:
    self.name = name
    self.score = 0
```

### The self Parameter
`self` refers to the specific instance of the class. It's how each object keeps
track of its own data. Every method in a class must have `self` as its first
parameter (Python passes it automatically).

### Instance Variables
Instance variables are data that belongs to each individual object.
They're created using `self.variable_name`:
```python
class Player(object):
    def __init__(self, name: str) -> None:

        self.name = name    # Each player has their own name
        self.score = 0      # Each player has their own score
```

### Methods
Methods are functions that belong to a class. They can access and modify the
instance's data:
```python
class Player(object):
    def __init__(self, name: str) -> None:
        self.name = name
        self.score = 0
    
    def add_points(self, points: int) -> None:
        self.score = self.score + points
    
    def reset_score(self) -> None:
        self.score = 0
    
    def get_info(self) -> str:
        return f"{self.name}: {self.score} points"
```

### Creating Instances and Using Methods
```python
# Create two player instances
player1 = Player("Alice")
player2 = Player("Bob")

# Each player has their own score
player1.add_points(10)
player2.add_points(5)

player1.get_info()  # Output: Alice has 10 points
player2.get_info()  # Output: Bob has 5 points
```

## Hands-on Project: Contact Book

Let's create an in-memory contact book system using classes.
For now, this will only exist when we run the program, and later we can look at
saving the data to files to repopulate the classes at a later time.

### Part 1: Create a Contact Class
```python
def print_line_separator() -> None:
    print("-" * 80)


class Contact(object):
    def __init__(self, name: str, phone: str, email: str, group: str) -> None:
        self.name = name
        self.phone = phone
        self.email = email
        self.group = group

    def update_phone(self, new_phone: str) -> None:
        self.phone = new_phone

    def update_email(self, new_email: str) -> None:
        self.email = new_email

    def display(self) -> None:
        print_line_separator()
        print(f"Name: {self.name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")
```

### Part 2: Create a ContactBook Class
```python
class ContactBook(object):
    def __init__(self) -> None:
        self.contacts: list[Contact] = []

    def add_contact(self, contact: Contact) -> None:
        self.contacts.append(contact)
        print(f"Added {contact.name} to contacts")

    def find_contact(self, name: str) -> Contact | None:
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return contact

        return None

    def list_all_contacts(self) -> None:
        if len(self.contacts) == 0:
            print("No contacts found")
        else:
            print(f"\n=== Contact Book ({len(self.contacts)} contacts) ===")
            for contact in self.contacts:
                contact.display()

            print_line_separator()
            print()

    def search_contacts(self, query: str) -> list[Contact]:
        found = []

        for i in self.contacts:
            if query in i.name:
                found.append(i)

        return found

    def delete_contact(self, name: str) -> None:
        contact = self.find_contact(name)
        if contact:
            self.contacts.remove(contact)
            print(f"Deleted {name}")
        else:
            print(f"Contact {name} not found")
```

# Using the Classes Together

```python
# Create a contact book
contact_book = ContactBook()

# Add some contacts
alice = Contact("Alice", "555-1234", "alice@email.com", "Friends")
bob = Contact("Bob", "555-5678", "bob@email.com", "Family")

contact_book.add_contact(alice)
contact_book.add_contact(bob)

# List all contacts
contact_book.list_all_contacts()

# Find and update a contact
contact = contact_book.find_contact("Alice")
if contact:
    contact.update_phone("555-9999")
    contact.display()

# Delete a contact
contact_book.delete_contact("Bob")
```

# Assignment
Extend the contact book with a grouping system:
* Add a group parameter to the Contact class (e.g., "Family", "Work", "Friends")
* Create a `list_by_group(group)` method in ContactBook that displays all
contacts in a specific group
* Create a `get_all_groups()` method that returns a list of unique group names
(no duplicates)
* Add a menu option to view contacts by group

## Challenge
* Create a `move_contact_to_group(name, new_group)` method
* Create a `count_contacts_by_group()` method that returns how many contacts are
in each group
* Display group statistics when listing all contacts
