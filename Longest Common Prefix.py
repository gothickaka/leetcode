class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs)==0:
            return ''
        strs.sort()
        i=0
        while i<len(strs[0]):
            if strs[0][i] == strs[len(strs)-1][i]:
                i=i+1
            else:
                break
        return strs[0][:i]

if __name__=='__main__':
    s = Solution()
    strlist = ['aabcd','aab','aabc']
    print(s.longestCommonPrefix(strlist))