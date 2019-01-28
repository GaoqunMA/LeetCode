#!/usr/bin/python
# -*- coding: <encoding name> -*-
"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.
"""
"""
解题思路：先将字符串翻转，然后转换成数字进行相加；其次，对相加的字符串做一个加法判断，可能取值为（0,1,2,3），只需判断
后两种情况,考虑一下最后一位的进位问题即可;最后对整个字符串进行翻转
"""
class Solution():
    def addBinary(self, a, b):
        """

        :param self:
        :param a: str
        :param b: str
        :return: str
        """
        # 翻转
        a = a[::-1]
        b = b[::-1]
        # 相加
        short = min(len(a), len(b))
        if len(a) > len(b):
            temp = list(a)
        else:
            temp = list(b)
        for i in range(short):
            temp[i] = str(int(a[i]) + int(b[i]))
        # 定义相加规则
        for i in range(len(temp) - 1):
            if temp[i] == '2':
                temp[i + 1] = str(int(temp[i+1]) + 1)
                temp[i] = '0'
            elif temp[i] == '3':
                temp[i + 1] = str(int(temp[i+1]) + 1)
                temp[i] = '1'
            else:
                pass
        # 对最后一位判断是否需要进位
        if temp[len(temp)-1] == '2':
            temp[len(temp) -1] = '0'
            temp.insert(len(temp), '1')
        elif temp[len(temp) -1] == '3':
            temp[len(temp) - 1] = '1'
            temp.insert(len(temp), '1')
        else:
            pass
        # 翻转同时转化为字符串
        return ''.join(temp[::-1])

if __name__ == '__main__':
    sol = Solution()
    print (sol.addBinary('1010', '1011'))
