# -*- coding: utf-8 -*-
# @Time    : 2018/10/24 14:43
# @Author  : frank@insightcredit
# @File    : addTwoNumbers.py
# @Desc    :


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.
    """

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c1 = l1
        c2 = l2
        re = list()
        while True:
            v = c1.val + c2.val
            re.append(ListNode(v))
            c1 = c1.next
            c2 = c2.next
            if c1 is None and c2 is None:
                break
            if c1 is None:
                c1 = ListNode(0)
            if c2 is None:
                c2 = ListNode(0)

        for i, v in enumerate(re):
            # print(v.val)
            if re[i].val >= 10:
                re[i].val = re[i].val - 10
                if i < len(re)-1:
                    re[i + 1].val = re[i + 1].val + 1
            if i == len(re) - 1:
                continue
            re[i].next = re[i + 1]
        return re[0]


if __name__ == "__main__":
    l11 = ListNode(5)
    # l12 = ListNode(4)
    # l13 = ListNode(3)
    # l11.next = l12
    # l12.next = l13

    l21 = ListNode(5)
    # l22 = ListNode(6)
    # l23 = ListNode(4)
    # l21.next = l22
    # l22.next = l23

    re = Solution().addTwoNumbers(l11, l21)
    print(re)
    while True:
        print(re.val)
        re = re.next
        if re is None:
            break
