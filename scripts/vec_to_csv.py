#!/usr/bin/env python3
"""
Converts vector data into a CSV file.
"""

__author__ = 'Yosuke Mizutani'
__version__ = '0.0.1'
__license__ = 'Apache License, Version 2.0'

# imports standard libraries
import sys
import argparse


def get_parser():
    """Argument parser."""

    parser = argparse.ArgumentParser(description='<program description>')
    parser.add_argument('path', help='input file path')
    return parser


def main(args):
    """Entry point of the program. """

    with open(args.path) as f:
        for line in f:
            print(line.split(': ')[1].strip().replace(' ', ','))


if __name__ == '__main__':
    main(get_parser().parse_args())
