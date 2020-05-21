import argparse
import sys

def configure():
    v_parser = argparse.ArgumentParser(description="Create, Manage project python")
    # required arguments
    v_required = v_parser.add_argument_group("required arguments")
    v_required.add_argument("-m", "--make" ,metavar="", help="make basic module, use after this <-mo> or <-p> who include <-n>")
    # optional arguments
    v_optional = v_parser.add_argument_group('make arguments')
    v_optional.add_argument("-mo", "--module", required=False ,metavar="", help="make basic module")
    v_optional.add_argument("-p", "--project", required=False ,metavar="", help="make basic project")
    v_optional.add_argument("-n", "--name", type=str, required=False ,metavar="<lorem>", help="set name, exclude <>")
    # others arguments
    v_other = v_parser.add_argument_group("others arguments")
    v_required.add_argument("-r", "--remove" ,metavar="<lorem>", help="remove directory, exclude <>")
    v_other.add_argument("-v", "--version", required=False ,metavar="", help="show version of the cli program")
    # interpret argument in command line
    if len(sys.argv)==1:
        v_parser.print_help(sys.stderr)
        sys.exit(1)
    return v_parser.parse_args()
