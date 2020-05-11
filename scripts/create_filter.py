#!/usr/bin/env python3
"""
Outputs the indexes (0-indexed) of the particular graph classes based on the given invariant file.
"""

__author__ = 'Yosuke Mizutani'
__version__ = '0.0.1'
__license__ = 'Apache License, Version 2.0'

import sys
import argparse
from random import Random


def get_parser():
    """Argument parser."""
    parser = argparse.ArgumentParser(description='Create random samples.')
    parser.add_argument('-c', '--condition', required=True,
                        choices=['conn'], help='filter condition')
    parser.add_argument('--sample', type=int, default=None, help='sample size')
    parser.add_argument('-s', '--seed', type=int,
                        default=None, help='random seed for sampling')
    parser.add_argument('path', help='input invariant file path')
    return parser


def main(args):
    """Entry point of the program. """

    func = {
        'conn': lambda s: int(s) == 1
    }[args.condition]

    ret = []
    i = 0

    with open(args.path) as f:
        for line in f:
            if func(line.strip()):
                ret += [i]
            i += 1

    if args.sample is not None and len(ret) > args.sample:
        rand = Random(args.seed)
        sampled = []
        for x in rand.sample(range(len(ret)), args.sample):
            print(ret[x])
    else:
        for x in ret:
            print(x)


if __name__ == '__main__':
    main(get_parser().parse_args())
