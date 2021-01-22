import argparse

def mean(nums: list):
	return sum(nums) / len(nums)

def median(nums: list):
	nums.sort()
	n = len(nums)
	if n % 2 == 0:
		median1 = nums[n//2]
		median2 = nums [n//2 -1]
		median = (median1 + median2) /2
	else:
		median = nums[n//2]
	return median

parser = argparse.ArgumentParser(description='math thingy')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='a math operator that solves the mean and the median')
parser.add_argument('-m','--median',dest='accumulate', action='store_const',
                    const=median, default=mean,
                    help='finds the median of the integers (default: find the mean of the integers)')

args = parser.parse_args()
print(args.accumulate(args.integers))
