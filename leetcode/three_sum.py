from typing import List


# TODO fix [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
class Solution:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()
        i, j, k = 0, 1, len(nums) - 1
        result = []
        while i < k - 1 and nums[k] >= 0:
            t_sum = nums[i] + nums[j] + nums[k]
            if t_sum == 0:
                result.append([nums[i], nums[j], nums[k]])
                while nums[i + 1] == nums[i]:
                    i += 1
                j = i + 1
            elif t_sum < 0:
                if j == k - 1:
                    i, j = i + 1, i + 2
                else:
                    j += 1
            else:
                if i == 0 and j == 1 or (nums[i] > 0 and nums[j] > 0):
                    while nums[k - 1] == nums[k]:
                        k -= 1
                    i, j = 0, 1
                else:
                    i, j = i + 1, i + 2

        return result
