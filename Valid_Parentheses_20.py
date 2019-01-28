class Solution:
    def isvalid(self, s):
        """

        :param s:string
        :return: bool
        """
        # 新建一个列表作为栈
        stack_list = [' ']
        # 涉及一对的操作建议用字典来做
        str_dict = {')': '(', ']': '[', '}': '{'}
        # 既然要判断字符串，首先必须要写一个循环
        for s_str in s:
            if s_str in str_dict and str_dict[s_str] == stack_list[len(stack_list)-1]:
                stack_list.pop()
            else:
                stack_list.append(s_str)
        if len(stack_list) == 1:
            return True
        return False

if __name__ == "__main__":

    sol = Solution()
    print(sol.isvalid('({})'))