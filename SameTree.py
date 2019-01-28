#!/usr/bin/python
# -*- coding: <encoding name> -*-
"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
"""
"""
问题思路：将两棵树都做先序遍历，然后将遍历结果保存至两个数组，比较两个数组是否相同即可；树的先序遍历用递归解决，时间复杂度为o(n);
空间复杂度为o(h),h为树的高度。
还可以不用递归对二叉树进行遍历，借助数据结构栈来进行。
"""
# 递归解决
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# class Solution:
#     def isSameTree(self, p, q):
#         """
#
#         :param p: TreeNode
#         :param q: TreeNode
#         :return:
#         """
#         p_list=[]
#         q_list=[]
#         def bianli(head, tree_list):
#             if head == None:# 基础条件，要判断二者不同，null的位置是需要输出的
#                 tree_list.append('null')
#                 return
#             tree_list.append(head.val)# 先输出结点的值
#             bianli(head.left, tree_list)# 遍历左结点
#             bianli(head.right, tree_list)# 遍历右结点
#         bianli(p, p_list)
#         bianli(q, q_list)
#         if p_list == q_list:
#             return True
#         else:
#             return False
# 非递归解决（用栈解决）
class Solution:
    def isSameTree(self, p, q):
        def bianli(head, tree_list):
            head_list = []
            while head or len(head_list) > 0: # 判断循环结束条件，二者需同时满足，head为none，栈中没有结点
                while head != None:# 左子树遍历到底
                    tree_list.append(head.val)
                    head_list.append(head)
                    head = head.left
                tree_list.append('null')
                if len(head_list) != 0:# 改变结点，开始寻找右子树
                    head = head_list.pop().right
        p_list = []
        q_list = []
        bianli(p, p_list)
        bianli(q, q_list)
        if p_list == q_list:
            return True
        else:
            return False