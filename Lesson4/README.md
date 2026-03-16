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
