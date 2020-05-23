from setuptools import setup, find_packages

setup(
    name="lyppy",
    version="0.1",
    author="Norro valentin",
    author_email="norrova.pro@gmail.com",
    description="Create python project",
    url="https://github.com/norrova/Lyppy",
    packages=find_packages(),
    entry_points = {
        "console_scripts":[
           "lyppy=lyppy.__main__:main"
        ]
    },
    python_requires='>=3',
)