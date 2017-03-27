# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l2.next,l1)
            return l2


if __name__=='__main__':
    s = Solution()
    list1 = ListNode(1)
    list2 = ListNode(2)
    list3 = ListNode(3)
    list4 = ListNode(4)
    list1.next = list4
    list2.next = list3
    print(s.mergeTwoLists(list1,list2).val)