# -*- coding:utf-8 -*-
#
# @Time        : 2018/12/10下午10:08
# @Author      : congxu_frank@163.com
# @File        : v1.py
# @Description : 
# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        length_l1 = self.getLength(l1)
        length_l2 = self.getLength(l2)
        v1 = self.getValue(l1, length_l1)
        v2 = self.getValue(l2, length_l2)
        list_v = [ListNode(v) for i, v in enumerate(list(str(v1 + v2)))]
        for i, v in enumerate(list_v):
            if i == 0:
                continue
            v.next = list_v[i - 1]
        return list_v[len(list_v) - 1]

    def getLength(self, l):
        i = 1
        cur = l
        while True:
            if cur.next is None:
                break
            i += 1
            cur = cur.next
        return i

    def getValue(self, l, length):
        i = 1
        cur = l
        value = 0
        while True:
            value += cur.val * pow(10, i - 1)
            if cur.next is None:
                break
            cur = cur.next
            i = i + 1
        return value


if __name__ == "__main__":
    l11 = ListNode(5)
    l12 = ListNode(4)
    l13 = ListNode(3)
    l11.next = l12
    l12.next = l13

    l21 = ListNode(5)
    l22 = ListNode(6)
    l23 = ListNode(4)
    l21.next = l22
    l22.next = l23

    re = Solution().addTwoNumbers(l11, l21)
    print(re)
    while True:
        print(re.val)
        re = re.next
        if re is None:
            break
