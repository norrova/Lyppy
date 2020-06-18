import argparse
from .manager import project, module, test, version
import sys

def configure():
    v_parser = argparse.ArgumentParser(description="Create python project")
    # optional arguments
    v_optional = v_parser.add_argument_group('make arguments')
    v_optional.add_argument("-m", "--module", action="store_true", required=False, help="make basic module")
    v_optional.add_argument("-p", "--project", action="store_true", required=False, help="make basic project")
    v_optional.add_argument("-t", "--test", action="store_true", required=False, help="make basic test")
    # others arguments
    v_other = v_parser.add_argument_group("others arguments")
    v_other.add_argument("-v", "--version", action="store_true", required=False , help="show version of the cli program")
    # interpret argument in command line
    if len(sys.argv)==1:
        v_parser.print_help(sys.stderr)
        sys.exit(1)
    else:
        return v_parser

def checking_requirements(p_parser):
    v_args = p_parser.parse_args()
    if v_args.module:
        module()
    elif v_args.project:
        project()
    elif v_args.test:
        test()
    elif v_args.version:
        version()