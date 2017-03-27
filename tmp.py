class Solution(object):
    def romanToInt(self, s):
        rom = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        i = 0
        result = 0
        while i<len(s)-1:
            if rom[s[i]]<rom[s[i+1]]:
                result = result - rom[s[i]]
            else:
                result = result + rom[s[i]]
            i = i + 1
        return result+rom[s[len(s)-1]]


if __name__=='__main__':
    s = Solution()
    print(s.romanToInt('X'))