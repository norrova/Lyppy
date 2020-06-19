# Lyppy - version 0.3
![toucan](https://lh4.googleusercontent.com/TjmDgHr3UQOL2aCx4GQzq8hKpdWRUlZkNW5NIGRkRh6l3a4PAyibo361XkzOaXMtBQe8lqU-__2GwyqVY_9k=w223-h1809)
> lyppy picture created by lunia • 2020

> Based on Python Application Layouts: A Reference by Kyle Stratis
> https://realpython.com/python-application-layouts/

A simple, fast and efficient cli program to create some project


## How to install
```bash
$ git clone https://github.com/norrova/Lyppy
$ cd Lyppy
# Windows...
$ install.bat
# Linux | MacOS
$ sh install.sh
```

## Commands
* `lyppy`
    * `-h` : help
    * `-v` : lyppy version
    * `-p <name>` : make project
        * Create `__init__.py`
        * Create :
            * `.gitignore` 
                * `https://www.toptal.com/developers/gitignore/api/python`
                * `https://www.toptal.com/developers/gitignore?templates=python`
            * `LICENCE`
            * `README.md`
            * `requirements.txt`
            * `setup.py`
            * `bin`
            * `data`
            * `docs`
            * `tests`
    * `-mo <name>` : make module
        * Create `__init__.py`
        * Create `<name>.py`
    * `-t <name>` : make test
        * Create `__init__.py`
        * Create `<name>.py`

## Project tree example
```bash
example_project
│   .gitignore
│   LICENCE
│   README.md
│   requirements.txt
│   setup.py
│
├───bin
├───data
├───docs
├───example_module
│       example_module.py
│       __init__.py
│
└───tests
    └───new_test
            test_new_test.py
            __init__.py
```
