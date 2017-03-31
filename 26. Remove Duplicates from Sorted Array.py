class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums)<=1:
            return len(nums)
        i = 0
        while i < len(nums)-1:
            if(nums[i] == nums[i+1]):
                del nums[i]
            else:
                i = i + 1
        return  len(nums)

if __name__=='__main__':
    s = Solution()
    list1 = []
    list2 = ['1','1','2','2','3']
    print(s.removeDuplicates(list1))
    print(s.removeDuplicates(list2))