"""
将古罗马数字转换为阿拉伯数字：
"""


class Solution:
    def romanToInt(self, s):
        """

        :param s:str
        :return:int
        """
        # 首先创建一个字典，让罗马数字与阿拉伯数字对应
        convert_dic ={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        # 传入的是字符串，要想求和需要将所有的字符串遍历，然后按照规则用循环语句判断即可
        length_int = len(s)
        # 1.根据规则，比较时需要比较其前一个字符串和后一个字符串，所以先判断长度是否是1，如果是1直接返回
        if length_int == 1:
            return convert_dic[s]
        # 2.如果不是1，设置一个sum加和变量，而后进行判断，最后将加和结果返回。
        sum = convert_dic[s[0]]
        for i in range(1, length_int):
            if s[i-1] == s[i]:
                sum =sum + convert_dic[s[i-1]]
            elif convert_dic[s[i-1]] > convert_dic[s[i]]:
                sum = sum + convert_dic[s[i]]
            else:
                if s[i-1] == 'I' or s[i-1] =='X' or s[i-1] =='C':
                    sum = sum + convert_dic[s[i]] - 2 * convert_dic[s[i-1]]
        return sum



if __name__ == "__main__":
    sol = Solution()
    print(sol.romanToInt('IV'))