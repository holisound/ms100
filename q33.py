# -*- coding: utf-8 -*-
# @Author: wangwh8
# @Date:   2019-09-12 10:09:13
# @Last Modified by:   edward
# @Last Modified time: 2019-09-12 21:27:37
# 33、字符串的排列

# 题目：输入一个字符串，打印出该字符串中字符的所有排列。

# 例如输入字符串abc，则输出由字符a、b、c 所能排列出来的所有字符串abc、acb、bac、bca、cab 和cba。


def permute(s):
    return backtrack(list(s), [])


def backtrack(chars, result, first=0):
    n = len(chars)
    if first == n:
        result.append(''.join(chars))
    for i in range(first, n):
        chars[first], chars[i] = chars[i], chars[first]
        backtrack(chars, result, first + 1)
        chars[first], chars[i] = chars[i], chars[first]
    return result


res = permute('abc')
print(res)
