import argparse
from statistics import mean, median, stdev


parser = argparse.ArgumentParser(description='Calculates central tendency of a list.')
parser.add_argument('data', type=float, metavar='N', nargs='+', help='numeric data')
parser.add_argument('--mean', action='store_true')
parser.add_argument('--median', action='store_true')
parser.add_argument('--stdev', action='store_true')
args = parser.parse_args()

print(f"data: {args.data}")
# Works just as well if you omit == True
if args.mean == True:
    print(f"mean: {mean(args.data)}")
if args.median == True:
    print(f"median: {median(args.data)}")
if args.stdev == True:
    print(f"stdev: {stdev(args.data)}")
