import os
import re

def init(p_type):
    v_name = get_name()
    v_rep = os.getcwd() + "\\" + v_name + "\\"
    try:
        if not os.path.exists(v_rep):
            os.mkdir(v_rep)
            print("Your " + p_type + " has been created with success !")
        else:
            v_choice = choice()
            if v_choice == None: return v_choice
    except OSError as identifier:
        print(identifier)
    return {"rep":v_rep,"name":v_name}

def create(v_rep):
    try:
        if not os.path.exists(v_rep):
            os.mkdir(v_rep)
    except OSError as identifier:
        print(identifier)

def get_name():
    v_name = ""
    v_error = True
    while v_error:
        v_name = input("Name of the module to create or over : ")
        if (special_char(v_name) != None):
            v_error = False
        else:
            print("Only lowercase letters or underscores are accepted\"_\"")
    return v_name

def special_char(p_string):
    v_pattern = re.compile("^([a-z]+_*)+$")
    return v_pattern.match(p_string)

def choice():
    v_dict = {"true":True, "false":None}
    v_valid = False
    while not v_valid:
        v_tmp = input("Replace all existing files ? (true | false) : ").lower()
        if v_tmp in v_dict:
            break
        else:
            print("Please enter \"true\" or \"false\" !")
    return v_dict[v_tmp]