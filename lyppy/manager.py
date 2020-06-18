import os
import requests
from .data import v_project, v_gitignore
from .directory import init, create, camel_case

def project():    
    v_tmp = init("project")
    if(v_tmp != None):
        v_rep = v_tmp["rep"]
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
            
def module():
    v_tmp = init("module")
    if(v_tmp != None):
        v_rep = v_tmp["rep"]
        with open(v_rep + "__init__.py","w"): pass
        with open(v_rep + v_tmp["name"] + ".py","w") as v_target:
            v_target.write("def main():\n\traise NotImplementedError()\n\nif __name__ == \"__main__\":\n\tmain()")

def test():
    v_tmp = init("test")
    if(v_tmp != None):
        v_rep = v_tmp["rep"]
        with open(v_rep + "__init__.py","w"): pass
        with open(v_rep + "test_" + v_tmp["name"] + ".py","w") as v_target:
            v_list = list(v_tmp["name"])
            v_list[0] = v_list[0].upper()
            print(camel_case("".join(v_list)))
            v_target.write(f"""import unittest\n\nclass Test{"".join(v_list)}(unittest.TestCase):\n\tdef test_upper(self):\n\t\tself.assertEqual('foo'.upper(), 'FOO')\n\nif __name__ == '__main__':\n\tunittest.main()""")

def version():
    print("Lyppy :: version :: 0.2")