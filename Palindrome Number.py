class Solution(object):
    def isPalindrome(self, x):
        result = 0
        y=x
        if x==0:
            return True
        if x<0:
            return False
        while(x != 0):
            result = result*10 + x%10
            x = x//10

        if result>2147483648:
            return False

        if result == y:
            return True
        else:
            return False


if __name__=='__main__':
    s = Solution()
    print(s.isPalindrome(2147447412))