from typing import List


class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		i, j = 0, 0
		found = False
		for i in range(len(nums) - 1):
			for j in range(i + 1, len(nums)):
				if nums[i] + nums[j] == target:
					found = True
					break
			if found:
				break

		if found:
			return [i, j]
		else:
			return []


nums = [1,3,7,8,9,5,2]
target = 3

s = Solution()
print(s.twoSum(nums, target))

