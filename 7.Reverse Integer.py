class Solution:
    def reverse(self, x):
        """

        :param x: 需要反转的整型数
        :return: int
        """
        x = int(x)
        if -2147483648 <= x <= 2147483647:
            # 因为涉及正负号，所以要判断x是否大于0
            if x < 0:
                x = -x
                temp = str(x)[::-1]
                reverse_x = int("-" + temp)
                if reverse_x < -2147483648:
                    return 0
                return reverse_x
            reverse_x = int(str(x)[::-1])
            if reverse_x > 2147483647:
                return 0
            return reverse_x
        return 0


if __name__ == "__main__":
    """
    Given a 32-bit signed integer, reverse digits of an integer.
    考虑到有正负号，所以只计算2的31次方，第一位作为符号位；在python中表示为2**31
    """
    sol = Solution()
    x = input("输入一个整数：")
    print(sol.reverse(x))
    # print(2**32)
