class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """

        :param l1:ListNode
        :param l2: ListNode
        :return: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        dummy =ListNode(0)
        p = dummy
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        if l1:
            p.next = l1
        else:
            p.next = l2
        return dummy.next


def sort_zhenzhen(p):
    while True:
        if not p:
            break
        print(p.val)
        p = p.next


if __name__ == "__main__":
    l1_node = ListNode(None)
    l2_node = ListNode(None)
    wei_p1 = l1_node
    wei_p2 = l2_node
    while True:
        choose_node = input("请选择你想输入内容的结点：l1 or l2 or no:")
        if choose_node == 'l1':
            p = wei_p1
            while True:
                temp_x = input("输入您想传入的数值，如果停止传入，输n：")
                if temp_x == 'no':
                    break
                p.next = ListNode(None)
                p = p.next
                p.val = temp_x
                wei_p1 = p
        elif choose_node == 'l2':
            p = wei_p2
            while True:
                temp_x = input("输入您想传入的数值，如果停止传入，输n：")
                if temp_x == 'no':
                    break
                p.next = ListNode(None)
                p = p.next
                p.val = temp_x
                wei_p2 = p
        else:
            break

    sol = Solution()
    paixu_zhizhen = sol.mergeTwoLists(l1_node.next, l2_node.next)
    sort_zhenzhen(paixu_zhizhen)