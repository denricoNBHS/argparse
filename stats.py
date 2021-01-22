import argparse
def mean(nums: list):
  return sum(nums)/len(nums)
def median(nums: list):
  nums.sort()
  if len(nums) % 2 == 1:
     return nums[len(nums) // 2]
  else:
    median1 = nums[len(nums) // 2]
    median2 = nums[(len(nums) // 2) -1]
    return (median1 + median2)/2
parser = argparse.ArgumentParser(description='Process some integers to find the mean or median')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer to find mean or median')
parser.add_argument('-m','--median',dest='accumulate', action='store_const',
                    const=median, default=mean,
                    help='find the median (default: find the mean)')
args = parser.parse_args()
print(args.accumulate(args.integers))
