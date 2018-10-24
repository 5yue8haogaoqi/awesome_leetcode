# -*- coding: utf-8 -*-
# @Time    : 2018/10/24 10:18
# @Author  : frank@insightcredit
# @File    : twoSum.py
# @Desc    :

class Solution(object):
    """
    Given nums = [2, 7, 11, 15], target = 9,
    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
    """
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = dict()
        for i, v in enumerate(nums):
            dic[v] = i

        for i, v in enumerate(nums):
            remains = target - v
            print(remains)
            if remains in dic:
                if dic.get(remains) ==i:
                    continue
                two = dic.get(remains)
                return [i, two]
        raise KeyError("no match up")


if __name__ == '__main__':
    test = [3, 2, 4]
    re = Solution().twoSum(test, 6)
    print(re)
