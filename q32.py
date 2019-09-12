# -*- coding: utf-8 -*-
# @Author: wangwh8
# @Date:   2019-09-12 09:54:49
# @Last Modified by:   wangwh8
# @Last Modified time: 2019-09-12 10:07:36
# 32、二元树的深度

# 题目：输入一棵二元树的根结点，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。

# 分析：这道题本质上还是考查二元树的遍历。 自底向上遍历
def height(root):
    if root:
        return max(height(root.left), height(root.right))+1
    return 0
