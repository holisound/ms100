# -*- coding: utf-8 -*-
# @Author: wangwh8
# @Date:   2019-09-12 11:35:11
# @Last Modified by:   wangwh8
# @Last Modified time: 2019-09-12 12:10:16
# 70、华为面试题

# （1）判断一字符串是不是对称的，如：abccba。


def isPalindrome(s):
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l, r = l + 1, r - 1
    return True

# （2）用递归的方法判断整数组a[N]是不是升序排列。

def isAsc(nums, i=0):
    if len(nums) - 1 > i:
        return nums[i] <= nums[i+1] and isAsc(nums, i+1)
    return True