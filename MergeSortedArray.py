#!/usr/bin/python
# -*- coding: <encoding name> -*-
"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to
hold additional elements from nums2.
"""
"""
思路解析：给定两个有序数组A(m),B(n)，且len(A)>m+n,要将这两个数组整合成一个数组，两种思路：
1.从头开始比较，遇到插入后需要移动后面的所有元素的位置，时间复杂度太高，不建议采用
2.采用倒序排序，直接从最后一个值做比较，较大的放到n+m-1的位置
需要注意的最多的问题就是边界问题。即一方的值用完了后面就不需要再做处理了，直接赋值即可
"""
class Solution:
    def merge(self, nums1, m, nums2, n):
        """

        :param nums1:list[int]
        :param m: int
        :param nums2:list[int]
        :param n: int
        :return:
        """
        index = m + n -1
        lastM = m - 1
        lastN = n - 1
        # 数组必须要考虑越界问题
        while index >= 0:
            if lastN < 0:
                return
            if lastM < 0:
                nums1[0:index + 1] = nums2[0:lastN+1]
                return
            if nums1[lastM] > nums2[lastN]:
                nums1[index] = nums1[lastM]
                lastM = lastM - 1
            else:
                nums1[index] = nums2[lastN]
                lastN = lastN - 1
            index = index - 1

        return

