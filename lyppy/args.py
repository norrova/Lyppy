import argparse
import sys
from .manager import project, module, test, version
from .directory import get_name, special_char

def configure():
    v_parser = argparse.ArgumentParser(description="Create python project")
    # optional arguments
    v_optional = v_parser.add_argument_group('make arguments')
    v_optional.add_argument("-m", "--module", nargs='?', const=True, default=False, required=False, help="make basic module")
    v_optional.add_argument("-p", "--project", nargs='?', const=True, default=False, required=False, help="make basic project")
    v_optional.add_argument("-t", "--test",  nargs='?', const=True, default=False, required=False, help="make basic test")
    # others arguments
    v_other = v_parser.add_argument_group("others arguments")
    v_other.add_argument("-v", "--version", action="store_true", required=False , help="show version of the cli program")
    # interpret argument in command line
    v_size = len(sys.argv)
    if v_size == 1:
        v_parser.print_help(sys.stderr)
        sys.exit(1)
    elif v_size == 3:
        if (check_name()):
            return v_parser
        else:
            v_parser.print_usage()
            sys.exit(1)
    elif v_size > 3:
        v_parser.print_usage()
        sys.exit(1)
    else:
        return v_parser

def checking_requirements(p_parser):
    v_args = p_parser.parse_args()
    print(v_args)
    if v_args.module:
        module(v_args.module) if isinstance(v_args.module, str) else module()
    elif v_args.project:
        project(v_args.project) if isinstance(v_args.project, str) else project()
    elif v_args.test:
        test(v_args.test) if isinstance(v_args.test, str) else test()
    elif v_args.version:
        version()

def check_name():
    # Import manager special char pour checker si faux sys exit
    v_bool = False
    if(len(sys.argv) == 3 and 
    not sys.argv[2].startswith('-') and
    isinstance(sys.argv[2], str) and
    special_char(sys.argv[2]) != None):
        v_bool = True
    return v_bool
