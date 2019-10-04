from typing import List


# TODO improve performance
class Solution:

    def three_sum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()
        i, j, k = 0, 1, len(nums) - 1
        result = []
        while nums[k] >= 0 and k >= 2:
            t_sum = nums[i] + nums[j] + nums[k]
            if t_sum == 0:
                result.append([nums[i], nums[j], nums[k]])
                i, j, k = self.mv_i(i, j, k, nums)
            elif t_sum < 0:
                i, j, k = self.mv_j(i, j, k, nums)
            else:
                if j == i + 1 or (nums[i] > 0 and nums[j] > 0):
                    i, j, k = self.mv_k(i, j, k, nums)
                else:
                    i, j, k = self.mv_j(i, j, k, nums)

        return result

    def mv_k(self, i, j, k, nums):
        k -= 1
        while nums[k] == nums[k + 1] and k > 1:
            k -= 1
        return 0, 1, k

    def mv_i(self, i, j, k, nums):
        i += 1
        while nums[i] == nums[i - 1] and i < k - 1:
            i += 1

        if i == k - 1:
            return self.mv_k(i, j, k, nums)
        else:
            return i, i + 1, k

    def mv_j(self, i, j, k, nums):
        j += 1
        while nums[j] == nums[j - 1] and j < k:
            j += 1

        if j == k:
            return self.mv_i(i, j, k, nums)
        else:
            return i, j, k
