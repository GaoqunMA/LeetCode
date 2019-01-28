#!/usr/bin/python
# -*- coding: <encoding name> -*-
# 递归解决
"""
class Solution:
    def climbStairs(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)
"""
'''
思路分析：这是一个典型的fib问题，两种方式可以走的话可以用fib(n-1)+fib(n-2),如果是分三种方式可以走的话，那就再加上fib(n-3)即可
'''
# 直接用数组动态解决
"""
class Solution:
    def climbStairs(self, n):
        fib_list = []
        for i in range(n):
            if i == 0:
                fib_list.append(1)
            elif i == 1:
                fib_list.append(2)
            else:
                fib_list.append(fib_list[i-1] + fib_list[i-2])
        return fib_list.pop()
"""

if __name__ == '__main__':
    sol = Solution()
    print (sol.climbStairs(4))