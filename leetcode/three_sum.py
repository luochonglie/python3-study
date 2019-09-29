from typing import List


# TODO performance issue
class Solution:
	def three_sum(self, nums: List[int]) -> List[List[int]]:
		if len(nums) < 3:
			return 
		two_sum_map = {}
		num_count = {}
		# caching two sum
		for i in range(0, len(nums) - 1):
			if nums[i] not in num_count:
				num_count[nums[i]] = nums.count(nums[i])

			for j in range(i + 1, len(nums)):
				two_sum = nums[i] + nums[j]
				if two_sum in two_sum_map:
					two_sum_tuple = sorted((nums[i], nums[j]))
					if two_sum_tuple not in two_sum_map.get(two_sum):
						two_sum_map.get(two_sum).append(two_sum_tuple)
				else:
					two_sum_map[two_sum] = [sorted((nums[i], nums[j]))]

		if nums[-1] not in num_count:
			num_count[nums[-1]] = nums.count(nums[-1])

		result = set()
		for num in nums:
			gap = 0 - num
			if gap in two_sum_map:
				for two_sum_list in two_sum_map.get(gap):
					if (two_sum_list.count(num) + 1) <= num_count[num]:
						result.add(tuple(sorted(two_sum_list + [num])))

		return [list(x) for x in result]


def main():
	nums = [[-1, 0, 1, 2, -1, -4], [0, 0, 0], []]
	s = Solution()
	for v in nums:
		print(s.three_sum(v))


if __name__ == '__main__':
	main()

