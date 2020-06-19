import os
import requests
from .data import v_project, v_gitignore
from .directory import init, create, camel_case, get_name, set_name

def project(p_name = None):   
    v_title = "project"
    v_name = set_name(p_name, v_title)
    v_rep = init(v_name, v_title)
    if(v_rep != None):
        v_response = requests.get(v_gitignore)
        if v_response.status_code == 200:
            with open(v_rep + ".gitignore", "w+") as v_target:
                v_target.write(v_response.text)
        else:
            raise requests.RequestException(f'.gitignore <response {v_response.status_code}>')
        for v_file, v_content in v_project["files"].items():
            with open(v_rep + v_file, "w") as v_target: 
                v_target.write(f"{v_content}")
        for v_directory in v_project["directories"]:
            create(v_rep + v_directory)
            
def module(p_name = None):
    v_title = "module"
    v_name = set_name(p_name, v_title)
    v_rep = init(v_name, v_title)
    if(v_rep != None):
        with open(v_rep + "__init__.py","w"): pass
        with open(v_rep + v_name + ".py","w") as v_target:
            v_target.write("def main():\n\traise NotImplementedError()\n\nif __name__ == \"__main__\":\n\tmain()")

def test(p_name = None):
    v_title = "test"
    v_name = set_name(p_name, v_title)
    v_rep = init(v_name, v_title)
    if(v_rep != None):
        with open(v_rep + "__init__.py","w"): pass
        with open(v_rep + "test_" + v_name + ".py","w") as v_target:
            v_target.write(f"""import unittest\n\nclass Test{camel_case(v_name)}(unittest.TestCase):\n\tdef test_upper(self):\n\t\tself.assertEqual('foo'.upper(), 'FOO')\n\nif __name__ == '__main__':\n\tunittest.main()""")

def version():
    print("Ready to start !")
    print("lyppy: version: 0.3")