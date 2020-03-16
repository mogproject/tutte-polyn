#!/usr/bin/env python3
"""
Converts output from the tuttepoly program into coefficient vectors for each graph.
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
    parser.add_argument('-n', type=int, required=True, help='number of vertices')
    parser.add_argument('path', help='input file path')
    return parser


def parse_tp_line(line):
    assert(line[:3] == 'TP[')

    tokens = line.split(':=')
    gid = int(tokens[0][3:-2])
    terms = tokens[1].rstrip(':\n').split('+')
    elems = [term.strip().split('*') for term in terms]
    ret = []
    for elem in elems:
        dx, dy = 0, 0
        for e in elem[1:]:
            if e[0] == 'x':
                dx = int(e[2:]) if e[1:2] == '^' else 1
            elif e[0] == 'y':
                dy = int(e[2:]) if e[1:2] == '^' else 1
        ret += [(int(elem[0]), dx, dy)]
    return gid, ret


def parse_graph_line(line):
    assert(line[:2] == 'G[')

    tokens = line.split(':=')
    gid = int(tokens[0][2:-2])
    edges = tokens[1].strip().rstrip('\}').lstrip('\{').split(',')
    ret = []
    for edge in edges:
        vs = edge.split('--')
        ret += [(int(vs[0]), int(vs[1]))]
    return gid, ret


def main(args):
    """Entry point of the program. """

    nx = args.n  # max degree of x: n - 1
    ny = 1 + (args.n - 1) * (args.n - 2) // 2  # max degree of y: n - 1 choose 2

    with open(args.path) as f:
        for line in f:
            if line[0] == 'T':
                parsed = parse_tp_line(line)
                vec = [0 for i in range(nx * ny)]
                for c, dx, dy in parsed[1]:
                    assert(dx < nx)
                    assert(dy < ny)
                    vec[dy * nx + dx] = c
                print('%d: %s' % (parsed[0], ' '.join(map(str, vec))))


if __name__ == '__main__':
    main(get_parser().parse_args())
