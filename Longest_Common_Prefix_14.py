"""
一个list中存放多个str，要求找出这些str的共同前缀；算法思路：遍历一遍，两两比较，得出的结果与一下个字符串比较，如果结果为空，
立即return
"""


class Solution:
    def longestCommonPrefix(self,strs):
        """

        :param strs:List[str]
        :return: str
        """
        # 1.判断列表是否为空
        length_strs = len(strs)
        if length_strs == 0:
            return ''
        # 2.判断列表长度是否是1，若果不是1，才能进行两两比较
        if length_strs == 1:
            return strs[0]
        # 3.如果不是1，开始遍历，进比较
        # 创建变量对共同前缀进行保存，初始设为第一个字符串的值
        com_str = strs[0]
        for i in range(1, length_strs):
            # 每次比较之前，对com_str进行判断，如果共同前缀为空，直接返回空，后续的操作都不需要做
            if len(com_str) == 0:
                return ''
            # 比较时找出两个字符串的最小值，控制最少比较次数
            len_min = min(len(com_str), len(strs[i]))
            # 设立一个标志，找出二者共同前缀的位置
            flag = 0
            for l in range(len_min):
                if com_str[l] == strs[i][l]:
                    flag += 1
                else:
                    com_str = com_str[0:flag]
                    break
            com_str = com_str[0:flag]

        return com_str


if __name__ == "__main__":
    str_list = ['', "magaoqun"]
    sol = Solution()
    print(sol.longestCommonPrefix(str_list))