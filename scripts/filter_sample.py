#!/usr/bin/env python3
"""
Filter a file by the line number s in a given sample definition file.
"""

__author__ = 'Yosuke Mizutani'
__version__ = '0.0.1'
__license__ = 'Apache License, Version 2.0'

import sys
import argparse


def get_parser():
    """Argument parser."""
    parser = argparse.ArgumentParser(
        description='Create random samples.')
    parser.add_argument('input_path', help='input file path')
    parser.add_argument('sample_path', help='sample definition file path')
    return parser


def main(args):
    """Entry point of the program. """

    s = set()
    with open(args.sample_path) as f:
        for line in f:
            s.add(int(line))

    lineno = 0
    with open(args.input_path) as f:
        for line in f:
            if lineno in s:
                sys.stdout.write(line)
            lineno += 1


if __name__ == '__main__':
    main(get_parser().parse_args())
