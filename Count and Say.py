class Solution(object):
    def countAndSay(self, n):
        if n==0:
            return ''
        s = '1'
        result = '1'
        for i in range(n-1):
            start = 0
            result = ''
            while start < len(s):
                count = 1
                next = start + 1
                while next < len(s) and s[start] == s[next]:
                    next += 1
                    count += 1
                result += str(count)
                result += s[start]
                start = next
            s = result
        return result

if __name__=='__main__':
    s = Solution()
    print(s.countAndSay(20))