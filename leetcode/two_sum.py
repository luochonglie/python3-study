from typing import List


class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		for i1, v1 in enumerate(nums):
			for i2, v2 in enumerate(nums[i1 + 1:]):
				if v1 + v2 == target:
					return [i1, i1 + i2 + 1]

		return []


nums = [1, 3, 7, 8, 9, 5, 2]
target = 5

s = Solution()
print(s.twoSum(nums, target))

