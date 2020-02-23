# coding=utf8

from typing import *

__author__ = "zouxiaoliang"


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class CStyleList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def front(self) -> ListNode:
        return self.head

    def push_back(self, value):
        if self.head is None:
            self.head = ListNode(value)
            self.tail = self.head
        else:
            self.tail.next = ListNode(value)
            self.tail = self.tail.next

    @classmethod
    def to_c_style(cls, array: List):
        c_list = CStyleList()
        for x in array:
            c_list.push_back(x)
        return c_list


class Solution:
    """
    如果存储的数据是按照逆序来存储的话，可以使用递归来解决
    """
    @classmethod
    def add_two_numbers(cls, l1: ListNode, l2: ListNode) -> ListNode:
        c_list = CStyleList()
        adding = 0

        while l1 is not None or l2 is not None:
            if l1 is None:
                value = l2.val + adding
                l2 = l2.next
            elif l2 is None:
                value = l1.val + adding
                l1 = l1.next
            else:
                value = l1.val + l2.val + adding
                l1 = l1.next
                l2 = l2.next
            adding = int(value / 10)
            value = (int(value % 10))
            c_list.push_back(value)

        if adding != 0:
            c_list.push_back(adding)

        return c_list.head


def _main():
    """
    给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
    如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
    您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/add-two-numbers
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
    输出：7 -> 0 -> 8
    原因：342 + 465 = 807
    :return:
    """
    solution = Solution()
    # solution.add_two_numbers(build_list([2, 4, 3]), build_list([5, 6, 4]))
    solution.add_two_numbers(
        CStyleList.to_c_style([1, 8]).front(),
        CStyleList.to_c_style([0]).front())
    pass


if __name__ == "__main__":
    exit(_main())
