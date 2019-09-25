from typing import List


class Solution:
	def two_sum(self, nums: List[int], target: int) -> List[int]:
		for i1, v1 in enumerate(nums):
			for i2, v2 in enumerate(nums[i1 + 1:]):
				if v1 + v2 == target:
					return [i1, i1 + i2 + 1]

		return []

	def two_sum_map_loop_twice(self, nums: List[int], target: int) -> List[int]:
		num_map = {}
		for i, v in enumerate(nums):
			num_map[v] = i

		for i, v in enumerate(nums):
			j = num_map.get(target - v)
			if j is not None and i != j:
				return [i, j]

		return []

	def two_sum_map_loop_once(self, nums: List[int], target: int) -> List[int]:
		num_map = {}

		for i, v in enumerate(nums):
			j = num_map.get(target - v)
			if j is not None and i != j:
				return [j, i]
			num_map[v] = i

		return []


nums = [1, 3, 7, 8, 9, 5, 2]
target = 5

s = Solution()
print(s.two_sum_map_loop_once(nums, target))

