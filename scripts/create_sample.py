#!/usr/bin/env python3
"""
Create random samples.
"""

__author__ = 'Yosuke Mizutani'
__version__ = '0.0.1'
__license__ = 'Apache License, Version 2.0'

import sys
import argparse
from random import Random


def get_parser():
    """Argument parser."""
    parser = argparse.ArgumentParser(
        description='Create random samples.')
    parser.add_argument('n', type=int)
    parser.add_argument('k', type=int)
    parser.add_argument('-s', '--seed', type=int,
                        default=None, help='random seed')
    return parser


def main(args):
    """Entry point of the program. """

    assert(args.k <= args.n)
    rand = Random(args.seed)
    for x in rand.sample(range(args.n), args.k):
        print(x)


if __name__ == '__main__':
    main(get_parser().parse_args())
