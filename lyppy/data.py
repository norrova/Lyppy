# Project
v_link = {
        "github":"https://github.com/norrova/Lyppy",
        ".gitignore":"https://www.gitignore.io/api/python"
    }
v_gitignore = v_link[".gitignore"]
v_project = {
    "files" :{
        "LICENCE":"https://choosealicense.com/",
        "requirements.txt":"# Example comment\n# Requirements without version specifiers (Lasted version)\npackage\n\n# Requirements with version specifiers\npackage (==, >, >=, <, <=) 0.0.1\t# Comment \n# condition can be represented by comma \",\"\npackage >= 1, <=2",
        "setup.py":"""import setuptools\n# https://setuptools.readthedocs.io/en/latest/\n\nsetuptools.setup(\n\tname="distribution name of your package", # only contains letters, numbers, _ , and -\n\tversion="0.0.1",\n\t# author="lyppy",\n\t# author_email="author@lyppy.com",\n\t# description="A small package generated by Lyppy",\n\t# long_description="detailed description of the package",\n\t# long_description_content_type="text/..."\n\t# url="https://github.com/norrova/Lyppy"\n\tpackages=setuptools.find_packages(),\n\t# https://pypi.org/classifiers/\n\tclassifiers=[\n\t\t"Programming Language :: Python"\n\t],\n\t# https://www.python.org/dev/peps/pep-0440/\n\tpython_requires=">= 3"\n)""",
        "README.md":f"""# Generated by Lyppy\n> A project developed by norro valentin\n* Lyppy : {v_link["github"]}\n* .gitignore : {v_gitignore}""",
    },
    "directories":[
        "bin",
        "docs",
        "data",
        "tests",
    ]
}