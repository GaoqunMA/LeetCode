#!/usr/bin/python
# -*- coding: <encoding name> -*-
'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
'''
"""
思路解析：本题为判断一棵树左右是否对称，即是否是一棵平衡树。那就需要判断左右两边的每个节点的左右值和右左值是否相等。可以用
递归的思想来做。谨记，树一般从根节点开始判断。
"""
# 递归方法
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     def isSymmetric(self, root):
#         def diGui(head_left, head_right):
#             # 基本用例
#             if head_left == None and head_right ==None:
#                 return True
#             # 基本用例
#             if head_right and head_left and head_left.val == head_right.val:
#                 return diGui(head_left.right, head_right.left) and diGui(head_left.left, head_right.right)
#             # 基本用例
#             return False
#         if root == None:
#             return True
#         return diGui(root.left, root.right)
# 迭代方法 树的迭代必然要依靠栈
class Solution:
    def isSymmetric(self, root):
        if root == None:
            return True
        head_left = root.left
        head_right = root.right
        while head_left != None and head_right != None:
            if head_left.right == head_right.left and head_left.left == head_right.right:
                return True
