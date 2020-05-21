import argparse
from .make import project, module
import sys

def configure():
    v_parser = argparse.ArgumentParser(description="Create, Manage project python")
    # required arguments
    v_required = v_parser.add_argument_group("Main arguments")
    v_required.add_argument("-m", "--make", action="store_true",  required=False, help="make basic module, use after this <-mo> or <-p> who include <-n>")
    # optional arguments
    v_optional = v_parser.add_argument_group('make arguments')
    v_optional.add_argument("-mo", "--module", action="store_true", required=False, help="make basic module")
    v_optional.add_argument("-p", "--project", action="store_true", required=False, help="make basic project")
    v_optional.add_argument("-n", "--name", type=str, required=False ,metavar="<lorem>", help="set name, exclude <>")
    # others arguments
    v_other = v_parser.add_argument_group("others arguments")
    v_required.add_argument("-r", "--remove" ,  required=False, metavar="<lorem>", help="remove directory, exclude <>")
    v_other.add_argument("-v", "--version", required=False ,metavar="", help="show version of the cli program")
    # interpret argument in command line
    if len(sys.argv)==1:
        v_parser.print_help(sys.stderr)
        sys.exit(1)
    else:
        return v_parser

def checking_requirements(p_parser):
    v_args = p_parser.parse_args()
    if v_args.make:
        if not v_args.name:
            if not v_args.module and not v_args.project:
                p_parser.error("-mo/--module is required when -m/--make is set")
            elif not v_args.project and not v_args.module:
                p_parser.error("-p/--project is required when -m/--make is set")
            
            if v_args.module:
                p_parser.error("-n/--name is required when -mo/--module is set")
            elif v_args.project:
                p_parser.error("-n/--name is required when -p/--project is set")
        else:
            if v_args.module:
                module()
            elif v_args.project:
                project()
            