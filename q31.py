# -*- coding: utf-8 -*-
# @Author: wangwh8
# @Date:   2019-09-11 17:26:38
# @Last Modified by:   wangwh8
# @Last Modified time: 2019-09-12 09:52:08
# 31、和为n 连续正数序列

# 题目：输入一个正数n，输出所有和为n 连续正数序列。

# 例如输入15，由于1+2+3+4+5=4+5+6=7+8=15，所以输出3 个连续序列1-5、4-6 和7-8。

def solve(n):
    nums=range(1, n)
    seen={0}
    mem={0:-1} # 缓存前缀和的index
    res=now=0
    ele=[]
    for i, num in enumerate(nums):
        now+=num
        # if now not in mem: # num > 0 所以 now不会重复
        mem[now] = i
        if now-n in seen:
            res+=1
            start = mem[now-n]+1
            ele.append(nums[start:i+1])
        seen.add(now)
    return res, ele
print(solve(15))
