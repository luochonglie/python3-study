from typing import List


# TODO Fix bug [0,0,0]
class Solution:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        two_sum_map = {}
        num_count = {}
        # caching two sum
        for i in range(0, len(nums) - 1):
            if nums[i] in num_count:
                num_count[nums[i]] = num_count.get(nums[i]) + 1
            else:
                num_count[nums[i]] = 1

            for j in range(i + 1, len(nums)):
                two_sum = nums[i] + nums[j]
                if two_sum in two_sum_map:
                    two_sum_tuple = sorted((nums[i], nums[j]))
                    if two_sum_tuple not in two_sum_map.get(two_sum):
                        two_sum_map.get(two_sum).append(two_sum_tuple)
                else:
                    two_sum_map[two_sum] = [sorted((nums[i], nums[j]))]

        if nums[-1] in num_count:
            num_count[nums[-1]] = num_count[nums[-1]] + 1
        else:
            num_count[nums[-1]] = 1

        result = set()
        for i in nums:
            gap = 0 - i
            if gap in two_sum_map:
                for two_sum_list in two_sum_map.get(gap):
                    if (two_sum_list.count(i) + 1) < num_count[i]:
                        result.add(tuple(sorted(two_sum_list + [i])))

        return [list(x) for x in result]


def main():
    nums = [[-1, 0, 1, 2, -1, -4], [0, 0, 0]]
    s = Solution()
    for v in nums:
        print(s.three_sum(v))


if __name__ == '__main__':
    main()
