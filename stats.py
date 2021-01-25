import argparse
from statistics import mean, median

def mean (nums: list) -> int:
  return sum(nums) / len(nums)

def median (nums: list) -> int:
  nums.sort()
  n = len(nums)
  if n % 2 == 0:
          median1 = nums[n // 2]
          median2 = nums [n // 2 -1]
          median = (median1 + median2) / 2
     else:
          median = nums[n // 2]
     return median

  parser = argparse.ArgumentParser(description='Process some numbers.')
 parser.add_argument('integers', metavar='N', type=int, nargs='+',
                      help='an integer for the accumulator')
 parser.add_argument('-m', '--median', dest='accumulate', action='store_const',
                      const=median, default=mean,
                      help='find the median (default: find the mean)')

  args = parser.parse_args()
 print(args.accumulate(args.integers))
