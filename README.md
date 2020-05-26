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
    * `-m` : make
        * `-p` : make project
        * `-mo` : make module
## Example
### Version **0.1**
```bash
# Create project
$ lyppy -m -p
# Create module
$ lyppy -m -mo
```

Project tree example
```
example
│   .gitignore
│   LICENCE
│   README.md
│   requirements.txt
│   setup.py
│
├───beautiful_module
│       beautiful_module.py
│       __init__.py
│
├───bin
├───data
├───docs
└───tests
```

## Task lists

* [x] : Make project
* [x] : Make module
* [ ] : Show project tree
* [ ] : Make unittest
