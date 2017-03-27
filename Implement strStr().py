class Solution(object):
    def strStr(self, haystack, needle):
        if len(haystack)<len(needle):
            return -1
        if len(needle)==0:
            return 0
        i = 0
        while i < len(haystack)-len(needle)+1:
            m = i
            n = 0
            while n < len(needle):
                if needle[n] == haystack[m]:
                    n=n+1
                    m=m+1
                else:
                    break
                if n == len(needle):
                    return i
            i=i+1
        return -1

if __name__=='__main__':
    s = Solution()
    stra = 'abcdefg'
    strb = 'aa'
    print(s.strStr(stra,'cde'))
    print(s.strStr(strb,'aaa'))