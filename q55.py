# -*- coding: utf-8 -*-
# @Author: wangwh8
# @Date:   2019-09-12 15:24:00
# @Last Modified by:   wangwh8
# @Last Modified time: 2019-09-12 15:47:01
# 55、（1）编写实现链表排序的一种算法。说明为什么你会选择用这样的方法？

def mergeSortList():
    pass

# （2）编写实现数组排序的一种算法。说明为什么你会选择用这样的方法？

def mergeSortArray(nums):
    # D&C
    if len(nums) < 2:
        return nums
    n = len(nums)
    left, right = nums[:n//2], nums[n//2:]

    def merge(left, right):
        res=[]
        i, j = 0, 0
        m, n = len(left), len(right)
        while i < m and j < n:
            if left[i] < right[j]:
                res.append(left[i])
                i+=1
            else:
                res.append(right[j])
                j+=1
        while i < m:
            res.append(left[i])
            i+=1
        while j < n:
            res.append(right[j])
            j+=1
        return res
    return merge(mergeSortArray(left), mergeSortArray(right))

# （3）请编写能直接实现strstr()函数功能的代码。


def strstr(s, t):
    # 滑动窗口
    m, n = len(s), len(t)
    for i in range(m-n+1):
        if all(t[j] == s[i+j] for j in range(n)):
            return i 
    return -1