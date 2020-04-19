#!/usr/bin/env python3
"""
Runs KeplerMapper and outputs a graph as JSON.
"""

__author__ = 'Yosuke Mizutani'
__version__ = '0.0.1'
__license__ = 'Apache License, Version 2.0'

import sys
import argparse
import numpy as np
import kmapper as km
import sklearn
import json


def get_parser():
    """Argument parser."""
    parser = argparse.ArgumentParser(
        description='Runs KeplerMapper and outputs a graph as JSON.')
    parser.add_argument('path', help='input file path')
    return parser


def main(args):
    """Entry point of the program. """

    data = np.genfromtxt(args.path, delimiter=',')
    mapper = km.KeplerMapper(verbose=0)
    lens = mapper.fit_transform(data, projection='l2norm')
    graph = mapper.map(lens, data, nr_cubes=20, overlap_perc=0.7,
                       clusterer=sklearn.cluster.KMeans(n_clusters=2))

    print(json.dumps(graph))


if __name__ == '__main__':
    main(get_parser().parse_args())
