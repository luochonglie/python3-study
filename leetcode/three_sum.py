from typing import List


# TODO Fix bug [0,0,0]
class Solution:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        two_sum_map = {}
        # caching two sum
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                two_sum = nums[i] + nums[j]
                if two_sum in two_sum_map:
                    two_sum_tuple = sorted((nums[i], nums[j]))
                    if two_sum_tuple not in two_sum_map.get(two_sum):
                        two_sum_map.get(two_sum).append(two_sum_tuple)
                else:
                    two_sum_map[two_sum] = [sorted((nums[i], nums[j]))]

        result = set()
        for i in nums:
            gap = 0 - i
            if gap in two_sum_map:
                for two_sum_idx_list in two_sum_map.get(gap):
                    if i not in two_sum_idx_list:
                        result.add(tuple(sorted(two_sum_idx_list + [i])))

        return [list(x) for x in result]


def main():
    nums = [[-1, 0, 1, 2, -1, -4], [0, 0, 0]]
    s = Solution()
    for v in nums:
        print(s.threeSum(v))


if __name__ == '__main__':
    main()
