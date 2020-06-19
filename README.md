# Lyppy - version 0.3
![toucan](https://i.ibb.co/Wt5P0qX/68747470733a2f2f6c68342e676f6f676c6575736572636f6e74656e742e636f6d2f546a6d446748723355514f4c326143783447517a7138684b70645752556c5a6b4e57354e4947526b5268366c33613450417969626f333631586b7a4f61584d74425165386c.png)
> lyppy picture created by <a href="https://github.com/Lunia-UK">Lunia</a> • 2020

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
    * `-m <name>` : make module
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
