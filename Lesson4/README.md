# Lesson 4 - Dictionaries, Paths, and JSON

## Dictionaries

What are dictionaries? - Key-value pairs for storing related data.
They are great for procedurally looking up values that you know, but are unsure
when they will be needed. They are denoted by an opening and closing curly
brace `{}`. Keys come first and values second, separated by a `:`. Like lists,
entries are separated by a comma.

The key and the value can be of any type, even user defined types like classes.

### Creating and accessing dictionaries
```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "NYC"
}
```
Values can be retrieved by their keys:
```python
print(person["name"])  # Output: Alice
```
Dictionaries do not have rigid structures and can be added to or modified:
```python
person["email"] = "alice@email.com"
```
Similar to lists, the `in` keyword will indicate if a key exists in the dict:
```python
print("age" in person)  # Output: True
```

### Dictionary Methods
Groups of items can be retrieved from a dictionary using the following methods:
* `.keys()` - get all keys
* `.values()` - get all values
* `.items()` - get key-value pairs for looping
* `.get(key, default` - safe access with fallback

### Looping through dictionaries
Like lists, dictionaries can be looped through by declaring variable names for
elements in the loop definition. Unlike lists, dictionaries can be "unpacked"
into multiple values. We will explore unpacking in more detail later.
```python
for key, value in person.items():
    print(f"{key} - {value}")
    # name - Alice
    # age - 25
    # city - NYC
    # email - alice@email.com
```

As of python 3.6 and later dictionaries are ordered, meaning the order of keys
will always be the same, and deterministic. Previously this was not the case and
many online references will use the `OrderedDict` class.

## Pathlib

Python has a pretty large standard library. A language standard library is the
collection of libraries that ship with the language itself. Today we will be
looking at my favorite library: `pathlib`.

`pathlib`  offers classes representing filesystem paths with semantics
appropriate for different operating systems. If you've never used the module
before or aren't sure which class is right for your task, [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)
is most likely what you need, and is also the class I use almost all the time.

<img src="https://docs.python.org/3/_images/pathlib-inheritance.png">

Here is how we would represent our previous file using pathlib:
```python
from pathlib import Path

file_path = Path("C:/Users/nated/OneDrive/Desktop/tutorial/person.json")
```

From here we gain a handful of useful methods we can call on our path object:
```python
print(file_path.parent)      # Output: C:/Users/nated/OneDrive/Desktop/tutorial
print(file_path.name)        # Output: person.json
print(file_path.stem)        # Output: person
print(file_path.suffix)      # Output: .json
print(Path.home())           # C:\Users\<username>
print(Path.home().exists())  # True
```

## JSON

JSON, short for JavaScript Object Notation, is a file format created in the
early 2000s for transferring data between systems on the internet.

JSON supports a handful of types:
* String
* Number (`integer` or `float`)
* Boolean
* Object (`dictionary{}`)
* Array (`list[]`)
* null (`None`)

It can be read across languages and is built-in to python, so it is very handy.
Since JSON's creation, other file formats that serve similar purposes have been
created, such as `.yaml`/`.yml`. Most of these other file formats are not built
into python, so we will look at them later.

We will be saving and loading our contact book data to and from a json file so
that we can keep our contact data around for the next time we run our program.

To save json data to a file we must convert a python object to a json formatted
string using `json.dumps()` like so:
```python
import json

data_str = json.dumps(person, indent=4)
print(data_str)
```

Inversely we can convert json string data into a dictionary using `json.loads()`:
```python
back_to_dict = json.loads(data_str)
```

Now we have a way to convert dictionaries to JSON strings and JSON strings into
dictionaries. From here we can store the JSON string data in a `.json` file on
disk.

Luckily the `pathlib.Path` objects we have been working with make this very easy.
```python
from pathlib import Path

file_path = Path("C:/Users/nated/OneDrive/Desktop/tutorial/person.json")
file_path.parent.mkdir(parents=True, exist_ok=True)
```
This will ensure all necessary parent directories are created and that it is ok
if any of them already exist. By not specifying `exists_ok=True`, an error will
be raised if you attempt to create a folder that already exists.

Now we can use `write_text()` and `read_text()` to persist our data to disk.
```python
file_path.write_text(data_str)

read_data = file_path.read_text()
print(type(read_data))

read_dict = json.loads(read_data)
print(read_dict)
print(type(read_dict))
```

## Let's refactor our contact book!

```python
import json
from pathlib import Path
```

```python
class Contact(object):
    def __init__(self, name: str, phone: str, email: str, group: str = "General") -> None:
        self.name = name
        self.phone = phone
        self.email = email
        self.group = group

    # existing methods...
    
    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "group": self.group
        }
    
    @staticmethod
    def from_dict(data: dict):
        return Contact(
            name=data["name"],
            phone=data["phone"],
            email=data["email"],
            group=data.get("group", "General")  # Default if not present
        )
```

```python
class ContactBook(object):
    def __init__(self) -> None:
        self.contacts: list[Contact] = []

    # existing methods...

    def save_to_file(self, filepath: Path) -> None:
        # Convert all contacts to dictionaries
        contacts_data = []
        for contact in self.contacts:
            contacts_data.append(contact.to_dict())
        
        saved_data = {"contacts": contacts_data}
        
        # Write to file
        json_string = json.dumps(saved_data, indent=4)
        filepath.write_text(json_string)
        print(f"Saved {len(self.contacts)} contacts to {filepath.name}")
    
    def load_from_file(self, filepath: Path) -> None:        
        if not filepath.exists():
            print(f"File {filepath.name} not found")
            return
        
        # Read from file
        json_string = filepath.read_text()
        contacts_data = json.loads(json_string)
        
        # Convert dictionaries back to Contact objects
        self.contacts = []
        for data in contacts_data["contacts"]:
            contact = Contact.from_dict(data)
            self.contacts.append(contact)
        
        print(f"Loaded {len(self.contacts)} contacts from {filepath.name}")
```

```python
contact_book = ContactBook()

save_path = Path("C:/Users/nated/OneDrive/Desktop/tutorial/contact_data.json")
contact_book.load_from_file(save_path)

# list existing contacts
contact_book.list_all_contacts()

# prevent duplicate entries
existing_alice = contact_book.find_contact("Alice")
if existing_alice is None:
    alice = Contact("Alice", "555-1234", "alice@email.com", "Friends")
    contact_book.add_contact(alice)

existing_bob = contact_book.find_contact("Bob")
if existing_bob is None:
    bob = Contact("Bob", "555-5678", "bob@email.com", "Family")
    contact_book.add_contact(bob)

contact_book.save_to_file(save_path)
```

# Assignment

* Add a `get_statistics()` method to ContactBook that returns a dictionary:
```python
{
    "total_contacts": 10,
    "contacts_by_group": {"Family": 3, "Work": 5, "Friends": 2},
    "most_common_group": "Work",
    "total_groups": 3
}
```
* Add a `save_statistics(filepath)` method that saves this dictionary to JSON.
* Add a `display_statistics()` method that prints the stats in a readable format.

## Challenge

Strings have the `.split('substring')` method for splitting strings into parts,
separated by the delimiter. You can use this to get a list of string parts of
an email address.
```python
print("nmaxwell@agbo.com".split("@"))
# Output: ['nmaxwell', 'agbo.com']
```

* Add email domain analysis to statistics:
    * Count how many contacts use each email domain (@gmail.com, @yahoo.com, etc.)
    * Add this to the statistics dictionary as `"email_domains": {"gmail.com": 5, "yahoo.com": 3}`
* Save and load these enhanced statistics
