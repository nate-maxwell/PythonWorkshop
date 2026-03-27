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

# \_\_main__

Consider the following code:

```python
# math_utils.py

def example_pow(x: int, y: int) -> int:
    return x ** y


foo = example_pow(3, 4)
```

When importing a library, all top level code (code not bound to a function or
class) will execute.

This can be helpful when setting up values that are dependent on the platform
executing the code, or other functionality a library is dependent on that cannot
be determined beforehand.

However, sometimes you want code to run while working on your library but you
do not want the code to run when it is imported into another. A very common
idiom to get around this is as follows:

```python
# math_utils.py

def example_pow(x: int, y: int) -> int:
    return x ** y


if __name__ == '__main__':
    foo = example_pow(3, 4)
```

Lets break this down.

first, lets print
```python
print(__name__)
```

`__name__` will print the value of `"__main__"`.
However, if we import our library into another, it will print the name of the
file it was declared in.
Give this a try, printing it in the file you execute vs printing it in a file
you import to see the results.

By checking if `__name__` evaluates to `"__main__"` we can limit code to only
run if we are executing the exact file it is located in, and not importing it
from another.

## Virtual Environments

A Python virtual environment is an isolated directory that contains a specific
Python interpreter and its own independent set of Python packages. This prevents
conflicts between different projects that may require different versions of the
same library, keeping the system-wide Python installation clean.

Many facilities will use package managers like `Rez` or `UV` rather than a virtual
environment, but for learning and solo projects, they are convenient and effective.

To create a virtual environment open the terminal in the root fo your python
project and type the following command:

`python -m venv <name_of_venv>`

This will create a virtual environment (venv) in the root fo your project.
The newly created venv will contain a symbolic link to your installed copy of
python, as well as a library directory for all of your dependencies.

Next, to tell your machine to use the venv, type the following command:

`venv/Scripts/active`

Or navigate to `your_project/venv/Scripts` and run `activate.bat` in your
terminal.

Now, whenever you install a dependency via `pip`, it will be installed here.

## PyPi

[PyPi](https://pypi.org/) is the Python Package Index, a python foundation
supported repository of released python packages by developers. Here you can
find all sorts of released pacakges. Many, if not most, of these packages can
also be found on [GitHub](http://github.com/).

### The pip command

To install a package from PyPi you can use the `pip` command.
With your venv activated, lets run `pip install PySide6`.
This will install `PySide6` and `Shiboken6` into your virtual environment.
`PySide` is an application framework library for created python applications.
