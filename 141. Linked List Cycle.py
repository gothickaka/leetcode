# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

if __name__ == '__main__':
    s = Solution()
    list1 = ListNode(1)
    list2 = ListNode(2)
    list3 = ListNode(3)
    list1.next = list2
    list2.next = list3
    list3.next = list1
    print(s.hasCycle(list1))
