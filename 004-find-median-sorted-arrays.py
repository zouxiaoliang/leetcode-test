# coding=utf8

from typing import *

__author__ = "zouxiaoliang"


class Solution:
    """
    给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
    请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
    你可以假设 nums1 和 nums2 不会同时为空。

    示例 1:
    nums1 = [1, 3]
    nums2 = [2]

    则中位数是 2.0

    示例 2:
    nums1 = [1, 2]
    nums2 = [3, 4]

    则中位数是 (2 + 3)/2 = 2.5

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return self.o_log_n(nums1, nums2)

    def o_log_n(self, nums1: List[int], nums2: List[int]) -> float:
        numbers = nums1 + nums2
        numbers.sort()
        length = len(numbers)
        if length % 2 != 0:
            return numbers[int(length / 2)]
        else:
            agv = int(length / 2)
            return sum(numbers[agv - 1: agv + 1]) / 2

    def o_log_min_m_n(self, nums1: List[int], nums2: List[int]) -> float:
        pass


def _main():
    solution = Solution()
    print(solution.findMedianSortedArrays([1, 2, 3], [2, 4, 6]))
    pass


if __name__ == "__main__":
    exit(_main())
