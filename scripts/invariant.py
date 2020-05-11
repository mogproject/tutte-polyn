#!/usr/bin/env python3
"""
Computes graph invariants.
"""

__author__ = 'Yosuke Mizutani'
__version__ = '0.0.2'
__license__ = 'Apache License, Version 2.0'

import math
import sys
import fileinput
from queue import deque

import argparse


def get_parser():
    """Argument parser."""
    parser = argparse.ArgumentParser(description='Computes graph invariants.')
    parser.add_argument('-n', type=int, required=True,
                        help='number of vertices')
    parser.add_argument(
        '-t', choices=['num-edges', 'cc', 'conn', 'cyclic', 'girth', 'triangle'], required=True, help='invariant type')
    parser.add_argument('path', help='input file path')
    parser.add_argument('--insert-trivial', type=bool, default=True,
                        help='process the trivial graph as the first graph input before processing the input file')
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
        q = deque()
        q.append(i)

        while q:
            p = q.pop()
            for r in edges[p]:
                if not visited[r]:
                    visited[r] = True
                    q.append(r)
    return ret


def connectedness(n, edges):
    return 1 if num_connected_components(n, edges) == 1 else 0


def cyclic(n, edges):
    return 0 if girth(n, edges) is math.nan else 1


def girth(n, edges):
    ret = math.inf

    for i in range(n):
        levels = [math.inf for j in range(n)]

        # DFS (recursion)
        def rec(v, level, sofar):
            levels[v] = level
            for u in edges[v]:
                if levels[u] == math.inf:
                    sofar = rec(u, level + 1, sofar)
                elif levels[u] <= levels[v] - 2:
                    sofar = min(sofar, levels[v] - levels[u] + 1)
            return sofar

        ret = rec(i, 0, ret)

    # return nan is the graph is acyclic instead of infinity
    return math.nan if ret == math.inf else ret


def triangle_existence(n, edges):
    return 1 if girth(n, edges) == 3 else 0


def main(args):
    """Entry point of the program. """
    func = {
        'num-edges': num_edges,
        'cc': num_connected_components,
        'conn': connectedness,
        'cyclic': cyclic,
        'girth': girth,
        'triangle': triangle_existence,
    }[args.t]

    if args.insert_trivial:
        print(func(args.n, [[] for i in range(args.n)]))

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
