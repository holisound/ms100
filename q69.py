# -*- coding: utf-8 -*-
# @Author: wangwh8
# @Date:   2019-09-12 12:12:03
# @Last Modified by:   wangwh8
# @Last Modified time: 2019-09-12 13:52:48
# 69、微软笔试题

# 求随机数构成的数组中找到长度大于等于3 的最长的等差数列, 输出等差数列由小到大，如果没有符合条件的就输出格式：

# 输入[1,3,0,5,-1,6]

# 输出[-1,1,3,5]

# 要求时间复杂度，空间复杂度尽量小。
# 动态规划
def longestArithSeq(nums):
    nums.sort()
    dp=[{} for _ in nums]
    maxlen = -1
    res=[]

    for i in range(1, len(nums)):
        for j in range(i): # j 表示上次子问题的解
            diff=nums[i]-nums[j]
            if diff in dp[j]:
                dp[i][diff] = dp[j][diff]+[nums[i]]
            else:
                dp[i][diff]=[nums[j], nums[i]]
            if len(dp[i][diff]) > maxlen:
                maxlen = len(dp[i][diff])
                res = dp[i][diff]
    return res

print(longestArithSeq([1,3,0,5,-1,6]))