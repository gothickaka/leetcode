# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

#iterative
class Solution(object):
    def deleteDuplicates(self, head):
        tmp = head
        while tmp:
            while tmp.next and tmp.val == tmp.next.val:
                tmp.next = tmp.next.next
            tmp = tmp.next
        return head

if __name__ == '__main__':
    s = Solution()
    list1 = ListNode(1)
    print(s.deleteDuplicates(list1))
