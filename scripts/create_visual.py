#!/usr/bin/env python3
"""
Outputs an image generated by mapped data, colored with graph invariants.
"""

__author__ = 'Yosuke Mizutani'
__version__ = '0.0.1'
__license__ = 'Apache License, Version 2.0'

import json
from kmapper.plotlyviz import plotlyviz
import sys
import argparse

import numpy as np
import warnings
warnings.filterwarnings("ignore")


def get_parser():
    """Argument parser."""
    parser = argparse.ArgumentParser(description='Create random samples.')
    parser.add_argument('-t', '--title', required=True, help='chart title')
    parser.add_argument('-o', '--output', required=True,
                        help='output image path')
    parser.add_argument('mapped_path', help='input mapped file path')
    parser.add_argument('invariant_path', help='input invariant file path')
    return parser


def main(args):
    """Entry point of the program. """

    pl_jet = [[0.0, 'rgb(0, 0, 127)'],  # derived for matplotlib jet
              [0.1, 'rgb(0, 0, 241)'],
              [0.2, 'rgb(0, 76, 255)'],
              [0.3, 'rgb(0, 176, 255)'],
              [0.4, 'rgb(41, 255, 205)'],
              [0.5, 'rgb(124, 255, 121)'],
              [0.6, 'rgb(205, 255, 41)'],
              [0.7, 'rgb(255, 196, 0)'],
              [0.8, 'rgb(255, 103, 0)'],
              [0.9, 'rgb(241, 7, 0)'],
              [1.0, 'rgb(127, 0, 0)']]

    with open(args.mapped_path) as f:
        graph = json.load(f)

    colors = np.genfromtxt(args.invariant_path)
    plotlyviz(graph, title=args.title, colorscale=pl_jet,
              color_function=colors, width=600, height=500, graph_layout='kk', filename=args.output)
    print('Saved: %s' % args.output)


if __name__ == '__main__':
    main(get_parser().parse_args())
