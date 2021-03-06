# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        if p == None and q == None:
            return True
        else:
            if p and q and p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) and True
            else:
                return False

if __name__ == '__main__':
    s = Solution()
    list1 = TreeNode(0)
    list2 = TreeNode(1)
    print(s.isSameTree(list1,list2))
