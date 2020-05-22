import os
import requests
import sys
import json
from .data import v_project, v_gitignore, v_module
from .directory import create

def project():    
    v_tmp = create("project")
    if(v_tmp != None):
        v_rep = v_tmp["rep"]
        v_response = requests.get(v_gitignore)
        if v_response.status_code == 200:
            with open(v_rep + ".gitignore", "w+") as v_target:
                v_target.write(v_response.text)
        else:
            raise requests.RequestException(f'.gitignore <response {v_response.status_code}>')
        for v_file, v_content in v_project.items():
            with open(v_rep + v_file, "w") as v_target: 
                v_target.write(f"{v_content}")

def module():
    v_tmp = create("module")
    if(v_tmp != None):
        v_rep = v_tmp["rep"]
        with open(v_rep + "__init__.py","w"): pass
        with open(v_rep + v_tmp["name"] + ".py","w") as v_target:
            v_target.write(v_module["py"])

def remove():
    return 0