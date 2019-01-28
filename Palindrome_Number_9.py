class Solution:
    def isPalindrome(self, x):
        """

        :param x:int
        :return: bool
        """
        # 1.如果是负数，直接返回假
        if x < 0:
            return False
        # 2.如果不是负数，就需要进行判断，判断标准就是需要除10取余数乘10，然后将最后得到的结果和原结果比较

        # （1） 给一个间接变量保存最初的x值
        temp = x
        # （2）给一个sum方便后面的求和不断相加
        sum = 0
        while True:
            if x//10 == 0:
                sum =sum + x % 10
                break
            remain = x % 10
            x = x //10
            sum = (sum+remain) * 10
        if sum == temp:
            return True
        return False

if __name__ == "__main__":

    sol =Solution()
    print(sol.isPalindrome(121))