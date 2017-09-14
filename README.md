<img src="https://github.com/johncoleman83/AirBnB_clone/blob/master/dev/HBTN-hbnb-Final.png" width="160" height=auto />

# AirBnB Clone Phase #3

## Description

Project attempts to clone the the AirBnB application and website, including the
database, storage, RESTful API, Web Framework, and Front End.

## Environment

* __OS:__ Ubuntu 14.04 LTS
* __language:__ Python 3.4.3
* __style:__ PEP 8 (v. 1.7.0)

<img src="https://github.com/johncoleman83/AirBnB_clone/blob/master/dev/hbnb_step5.png" />

## Console

To run the console, clone this repository and run `./console.py`

Once in the console, you will see the following:
```
.----------------------------.
|    Welcome to hbnb CLI!    |
|   for help, input 'help'   |
|   for quit, input 'quit'   |
.----------------------------.
(hbnb)
```

Allowed commands can be shown by running `help`:
```
(hbnb) help

Documented commands (type help <topic>):
========================================
Amenity    City  Place   State  airbnb  create   help  show  
BaseModel  EOF   Review  User   all     destroy  quit  update
```
### Commands
#### `airbnb`: Command to change the console prompt string.
- Usage: `airbnb`
#### `all`: Prints all objects of a given class
- Usage: `all <class name>`
#### `create`: Creates a new instance of a given class
- Usage: `create <class name>`
#### `destroy`: Destroys a specific instance of a class
- Usage: `destroy <class name> <instance id>`
#### `EOF`: Handles EOF, exits the console
- Usage: `EOF`
#### `help`
- To list the available commands: `help`
- To show details about a specific command: `help <command>`
#### `quit`: Command to quit the program
- Usage: `quit`
#### `show`: Prints a secific class instance
- Usage: `show <class name> <instance id>`
#### `update`: Updates or adds a new attribute and value to a specific class instance
- Usage: `update <class name> <instance id> <attribute name> <value of attribute>`

#### Using Class Commands
Each Class has various methods that can be run on an instance of that Class.

The syntax to run Class methods is `<Class name>.<comand>(<instance id>)`.

Classes available: `Amenity`, `BaseModel`, `City`, `Place`, `Review`, `State`, `User`

Commands available:
- `save`: Updates attribute "updated_at" to the current time, saves the instance
- `to_json`: Returns JSON representation of the instance
- `delete` : Deletes an instance from storage

## Testing


#### `unittest`

This project uses python library, `unittest` to run tests on all python files.
All unittests are in the `./tests` directory with the command:

* `python3 -m unittest discover -v ./tests/`

The bash script `init_test.sh` executes all these tests:

  * checks `pep8` style

  * runs all unittests

  * runs all w3c_validator tests

  * cleans up all `__pycache__` directories and the storage file, `file.json`

**Usage:**

```
$ ./dev/init_test.sh
```

#### CLI Interactive Tests

This project uses python library, `cmd` to run tests in an interactive command
line interface.  To begin tests with the CLI, run this script:

```
$ ./console.py
```

* For a detailed description of all tests, run these commands inside the
custom CLI:

```
$ ./console.py
(hbnb) help help
List available commands with "help" or detailed help with "help cmd".
(hbnb) help

Documented commands (type help <topic>):
========================================
Amenity    City  Place   State  airbnb  create   help  show
BaseModel  EOF   Review  User   all     destroy  quit  update

(hbnb) help User
class method with .function() syntax
        Usage: User.<command>(<id>)
(hbnb) help create
create: create [ARG]
        ARG = Class Name
        SYNOPSIS: Creates a new instance of the Class from given input ARG
```

* Tests in the CLI may also be executed with this syntax:

  * **destroy:** `<class name>.destroy(<id>)`

  * **update:** `<class name>.update(<id>, <attribute name>, <attribute value>)`

  * **update with dictionary:** `<class name>.update(<id>, <dictionary representation>)`


#### Continuous Integration

Uses [Travis-CI](https://travis-ci.org/) to run all tests on all commits to the
github repo

## Authors

* MJ Johnson, [mj31508](https://github.com/mj31508)
* David John Coleman II, [davidjohncoleman.com](http://www.davidjohncoleman.com/)
* Kimberly Wong, [kjowong](http://github.com/kjowong) | [@kjowong](http://twitter.com/kjowong) | [kjowong@gmail.com](kjowong@gmail.com)
* Carrie Ybay, [hicarrie](http://github.com/hicarrie) | [@hicarrie_](http://twitter.com/hicarrie_)
* Kristen Loyd, [KRLoyd](https://github.com/KRLoyd)  | [@Biebop1](http://twitter.com/Biebop1)

## License

Public Domain, no copyright protection
