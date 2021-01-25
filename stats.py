import argparse
from statistics import mean, median

""" 
Write a command line tool that accepts a list of (one or more) 
numbers and returns their mean by default or, if the '-m' or '--median'
options are included, their median instead.

The mean and median functions from the statistics module have been
included for you.
"""
parser = argparse.ArgumentParser(description='Find median or mean of integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--median', dest='accumulate', action='store_const',
                    const=median, default=mean,
                    help='sum the integers (default: find the mean)')

args = parser.parse_args()
print(args.accumulate(args.integers))
