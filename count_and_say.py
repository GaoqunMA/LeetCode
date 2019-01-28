#!/usr/bin/python
# -*- coding: utf-8-*-
'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.
'''
'''
解题思路：下一个输出是由上一个决定，因此本题可以用递归来解
    基本用例：当n=1时，返回“1”
    通用方法：根据n=n-1设定规则来计算n
'''
def countAndSay(n):
    """

    :param n: int,the number your want to calulate
    :return:
    """
    # 基本用例
    if n == 1:
        print ("1")
        return "1"
    else:
        # 递归表达，表示n-1与n之间的关系
        s_temp = countAndSay(n-1) + '*'
        count = 1
        s_final = ''
        for i in range(len(s_temp)-1):
            if s_temp[i] == s_temp[i+1]:
                count = count + 1
            else:
                s_final = s_final + str(count) + s_temp[i]
                count = 1
        print (s_final)
    return s_final

print (countAndSay(5))