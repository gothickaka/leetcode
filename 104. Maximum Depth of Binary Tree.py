# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        return 0 if root == None else max(self.maxDepth(root.left), self.maxDepth(root.right))+1

if __name__ == '__main__':
    s = Solution()
    list1 = TreeNode(0)
    list2 = TreeNode(1)
    list3 = TreeNode(2)
    list1.left = list2
    list2.right = list3
    print(s.maxDepth(list1))
