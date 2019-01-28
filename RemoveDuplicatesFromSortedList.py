#!/usr/bin/python
# -*- coding: <encoding name> -*-
'''
Given a sorted linked list, delete all duplicates such that each element appear only once.
'''
"""
思路解析：本题为链表删除重复元素，首先需要做的是保存头结点，保证最后可以输出。
其次应该分为两部分：
第一部分：当前元素与下一元素重复，删除后指针不移动
第二部分：当前元素与下一元素不重复，指针直接后移

第二种类型：有序数组中去除相同的元素，可以遍历以一遍，然后将不相同的元素放到另一个列表中，这样节省时间，但是占用空间
"""
class Solution:
    def deleteDuplicates(self, head):
        p = head
        while p != None:
            if p.next != None and p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return head