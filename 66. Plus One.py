class Solution(object):
    def plusOne(self, digits):
        i = len(digits)-1
        while i>=0:
            if(digits[i]<9):
                digits[i]+=1
                return digits
            digits[i]=0
            i-=1
        digits[0]=1
        digits.append(0)
        return digits

if __name__ == '__main__':
    s = Solution()
    list1 = [1,0,9,9]
    print(s.plusOne(list1))
