#!/usr/bin/env python3
"""
Converts a decoded g6 data to the input format for the `tutte` program.
"""

__author__ = 'Yosuke Mizutani'
__version__ = '0.0.1'
__license__ = 'Apache License, Version 2.0'

import math
import sys
import fileinput


def print_edges(edges):
    if not edges:
        return
    edges.sort()
    buf = ','.join('%d--%d' % (u, v) for u, v in edges)
    print(buf)


def main():
    """Entry point of the program. """

    edges = []
    for line in fileinput.input():
        line = line.strip()
        if 'Graph' in line:
            continue
        if not line:
            print_edges(edges)
            edges = []
            continue

        tokens = line.rstrip(';').split(':')
        u = int(tokens[0])
        for vv in tokens[1].split():
            v = int(vv)
            if u < v:
                edges += [(u, v)]
    print_edges(edges)


if __name__ == '__main__':
    main()
