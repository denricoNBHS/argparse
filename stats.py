import argparse
from statistics import mean, median

def means (nums: list) -> int:
        return mean(nums)

def medians (nums: list) -> int:
        return (median(nums))

parser = argparse.ArgumentParser(description='Process some numbers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                     help='an integer for the accumulator')
parser.add_argument('-m', '--median', dest='accumulate', action='store_const',
                     const=medians, default=means,
                     help='find the median (default: find the mean)')

args = parser.parse_args()
print(args.accumulate(args.integers))
