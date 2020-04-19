#!/usr/bin/env python3
"""
Computes graph invariants.
"""

__author__ = 'Yosuke Mizutani'
__version__ = '0.0.1'
__license__ = 'Apache License, Version 2.0'

import math
import sys
import fileinput

import argparse


def get_parser():
    """Argument parser."""
    parser = argparse.ArgumentParser(description='Computes graph invariants.')
    parser.add_argument('-n', type=int, required=True,
                        help='number of vertices')
    parser.add_argument(
        '-t', choices=['num-edges', 'cc', 'conn'], required=True, help='invariant type')
    parser.add_argument('path', help='input file path')
    return parser


def num_edges(n, edges):
    return sum(len(es) for es in edges) // 2


def num_connected_components(n, edges):
    ret = 0
    visited = [False for i in range(n)]
    for i in range(n):
        if visited[i]:
            continue
        ret += 1
        visited[i] = True
        q = [i]

        while q:
            p = q.pop()
            for r in edges[p]:
                if not visited[r]:
                    visited[r] = True
                    q += [r]
    return ret

def connectedness(n, edges):
    ret = 0
    visited = [False for i in range(n)]

    visited[0] = True
    q = [0]

    while q:
        p = q.pop()
        for r in edges[p]:
            if not visited[r]:
                visited[r] = True
                q += [r]
    return 1 if all(visited) else 0

def main(args):
    """Entry point of the program. """
    func = {
        'num-edges': num_edges,
        'cc': num_connected_components,
        'conn': connectedness,
    }[args.t]

    with open(args.path) as f:
        for line in f:
            line = line.strip()
            edges = [[] for i in range(args.n)]
            if line:
                for s, t in [map(int, e.split('--')) for e in line.strip().split(',')]:
                    edges[s] += [t]
                    edges[t] += [s]
            print(func(args.n, edges))


if __name__ == '__main__':
    main(get_parser().parse_args())
