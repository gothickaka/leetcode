class Solution(object):
    def reverse(self, x):
        result = 0
        flag = 0
        if x<0:
            flag = 1
            x = abs(x)
        while(x != 0):
            result = result*10 + x%10
            x = x//10
        if flag:
            result = -1*result
            if result<-2147483648:
                return 0
            else:
                return result
        elif result>2147483648:
            return 0
        else:
            return result

if __name__=='__main__':
    s = Solution()
    print(s.reverse(-2147447412))