from typing import List


# TODO fix logic issue
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
                i, j = i + 1, i + 2
            elif t_sum < 0:
                if j == k - 1:
                    i, j = i + 1, i + 2
                else:
                    j += 1
            else:
                k -= 1
                j = i + 1

        return result
