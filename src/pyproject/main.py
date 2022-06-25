
"""
Main command line options
"""
import os
import sys 
import argparse
import unittest
import logging

from .utils.logs import CustomLogger
from .utils import project
from .tests.run import run_unittests

mlogger = CustomLogger(__name__)

def parse_args():
    parser = argparse.ArgumentParser(description='PyProject: A template Python repository')
    parser.add_argument('--test',
                        dest = 'test',
                        action = 'store_true',
                        help = 'Perform unit tests')
    parser.add_argument('--testmodule',
                        dest = 'testmodules',
                        metavar = 'MODULES',
                        nargs = "*",
                        type = str,
                        default = None,
                        help = 'Names of modules to be tested')
    parser.add_argument('--version',
                        dest = 'version',
                        action = 'store_true',
                        help = 'Print version number')
    parser.add_argument('--verbose',
                        dest = 'verbose',
                        action = 'store_true',
                        help = 'Print information while running')
    parser.add_argument('--vverbose',
                        dest = 'vverbose',
                        action = 'store_true',
                        help = 'Print more information while running')
    parser.add_argument('--infile',
                        type = str,
                        dest = 'infile',
                        metavar = 'FILE',
                        help = 'Input file example')
    parser.add_argument('--seed',
                        type = int,
                        dest = 'seed',
                        metavar = 'INT',
                        default = None,
                        help = 'Seed for random initialization')
    res = parser.parse_args()
    return parser, res 


def do_task():
    raise NotImplementedError


def show_version():
    print ("")
    print ("PyProject version {:s}".format(project.version()))
    print ("")
    return

def show_help(parser, opts):
    parser.print_help(sys.stderr)
    sys.exit(1)
    return


def main():
    parser, opts = parse_args()
    log_level = logging.INFO  if opts.verbose  else None
    log_level = logging.DEBUG if opts.vverbose else log_level
    mlogger.set_loglevel(log_level)
    mlogger.override_global_default_loglevel(log_level)

    if opts.test:
        mlogger.debug("Calling logger from main")
        run_unittests()

    elif opts.version:
        show_version()

    else:
        if opts.infile:
            do_task()
        else:
            show_help(parser, opts)

if __name__ == "__main__":
    main()
