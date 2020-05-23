import os
import requests
import sys
import json
from .data import v_project, v_gitignore, v_module
from .directory import init, create

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
            v_target.write(v_module["py"])

def version():
    print("Lyppy :: version :: 0.1")