# Lyppy
> Based on Python Application Layouts: A Reference by Kyle Stratis
> https://realpython.com/python-application-layouts/

A simple, fast and efficient python library to create some project

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
    * `-p` : make project
        * Create __init__.py
        * Create :
            * .gitignore 
                * `https://www.toptal.com/developers/gitignore/api/python`
                * `https://www.toptal.com/developers/gitignore?templates=python`
            * LICENCE
            * README.md
            * requirements.txt
            * setup.py
            * bin
            * data
            * docs
            * tests
    * `-mo` : make module
        * Create __init__.py
        * Create \<name\>.py
    * `-t` : make test
        * Create __init__.py
        * Create \<name\>.py

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
