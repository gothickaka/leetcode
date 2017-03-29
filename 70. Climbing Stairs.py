#Fibonacci sequence
class Solution(object):
    def climbStairs(self, n):
        a = 1
        b = 2
        for _ in range(1, n):
            tmp = b
            b = a + b
            a = tmp
        return a

if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(9))
