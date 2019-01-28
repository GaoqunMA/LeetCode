#!/usr/bin/python
# -*- coding: <encoding name> -*-
"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
"""
"""
思路分析：本题是求一个值的平方根，可以折半一半一半的查找，用二分法，时间复杂度是logn。考虑到所有情况，一个整数值的平方根不会超过
n//2 + 1，因此将max设置成这个值，然后将min设置为0即可。如果正好等于立即返回，如果最后没查找到返回最大值。二分法应用范围极广，且
套路非常固定，可以查列表以及字符串或者任意可以迭代的数据类型中是否有某值以及进行插入操作。
"""
class Solution:
    def mySqrt(self, x):
        """

        :param x: int
        :return: int
        """
        min = 0
        max = x//2 + 1
        while(min<=max):
            mid = (min+max)//2
            sq = mid * mid
            if sq == x:
                return mid
            elif sq < x:
                min = mid + 1
            else:
                max = mid - 1
        return max


if __name__ == '__main__':
    sol = Solution()
    x = [1,3,4,5,8,9,12,35,56,78,96]
    print(sol.mySqrt(x,12))