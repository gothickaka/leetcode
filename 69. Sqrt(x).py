class Solution(object):
    def mySqrt(self, x):
        if x<0:
            return
        i = x
        while i*i > x:
            i = (i+x/i)/2
        return i

if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt(-1))
