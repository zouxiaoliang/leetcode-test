# coding=utf8

from typing import *

__author__ = "zouxiaoliang"


class Solution:
    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)):
            p2 = target - nums[x]
            if p2 in nums:
                y = nums.index(p2)
                if x != y:
                    return [x, y]
        return []


def _main():
    """
    给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
    你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/two-sum
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

    给定 nums = [2, 7, 11, 15], target = 9
    因为 nums[0] + nums[1] = 2 + 7 = 9
    所以返回 [0, 1]

    """
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(solution.two_sum(nums, target))


if __name__ == "__main__":
    exit(_main())
