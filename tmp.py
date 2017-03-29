import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        queue, res = collections.deque([(root, 0)]), []
        while queue:
            node, level = queue.popleft()
            if node:
                if len(res) < level + 1:
                    res.insert(0, [])
                res[-(level + 1)].append(node.val)
                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))
        return res

if __name__ == '__main__':
    s = Solution()
    list1 = TreeNode(1)
    list2 = TreeNode(2)
    list3 = TreeNode(3)
    list4 = TreeNode(4)
    list5 = TreeNode(5)
    list1.left = list2
    list1.right = list3
    list2.left = list4
    list2.right = list5
    print(s.levelOrderBottom(list1))
