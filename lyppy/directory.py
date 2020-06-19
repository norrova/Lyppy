import os
import re
import sys
from .data import v_project

def init(p_name, p_type):
    v_rep = os.getcwd() + "\\" + p_name + "\\"
    try:
        if not os.path.exists(v_rep):
            os.mkdir(v_rep)
            print("Your " + p_type + " has been created with success !")
        else:
            v_choice = choice()
            if v_choice == None: return v_choice
    except OSError as identifier:
        print(identifier)
    return v_rep

def create(v_rep):
    try:
        if not os.path.exists(v_rep):
            os.mkdir(v_rep)
    except OSError as identifier:
        print(identifier)

def get_name(p_type):
    v_name = ""
    v_error = True
    while v_error:
        try:
            v_name = input("Enter a name of the " + p_type + " : ")
        except KeyboardInterrupt:
            sys.exit()
        if (special_char(v_name) != None):
            v_error = False
        else:
            print("Only lowercase letters or underscores are accepted\"_\"")
    return v_name

def special_char(p_string):
    v_pattern = re.compile("^([a-z]+_*)+$")
    return v_pattern.match(p_string)

def camel_case(p_string):
    v_list = list(p_string)
    v_upper = False
    for index in range(0, len(v_list), 1):
        if(v_list[index] == '_'):
            v_upper = True
        elif(v_upper):
            v_list[index] = v_list[index].upper()
            v_upper = False
        else:
            pass
    if '_' in v_list:
        v_list.remove('_')
    v_list[0] = v_list[0].upper()
    return "".join(v_list)

def choice():
    v_dict = {"true":True, "false":None}
    v_valid = False
    while not v_valid:
        try:
            v_tmp = input("Replace all existing files ? (true | false) : ").lower()
        except KeyboardInterrupt:
            sys.exit()
        if v_tmp in v_dict:
            break
        else:
            print("Please enter \"true\" or \"false\" !")
    return v_dict[v_tmp]