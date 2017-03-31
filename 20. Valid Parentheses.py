class Solution(object):
    def isValid(self, s):
        if len(s)%2 != 0 or len(s) == 0:
            return False
        strlist = []
        i=0
        while i<len(s):
            if len(strlist) == 0:
                strlist.append(s[i])
            elif (s[i] == ")" and strlist[-1] == "(") or (s[i] == "]" and strlist[-1] == "[") or (s[i] == "}" and strlist[-1] == "{"):
                strlist.pop()
            else:
                strlist.append(s[i])
            i=i+1
        if len(strlist) !=0:
            return False
        else:
            return True

if __name__=='__main__':
    s = Solution()
    print(s.isValid(')}'))