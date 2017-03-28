class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()
        i = s.rfind(' ')+1
        return len(s)-i

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLastWord('  a boy  '))
