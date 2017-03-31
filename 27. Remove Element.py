class Solution(object):
    def removeElement(self, nums, val):
        if len(nums) == 0:
            return
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                i = i + 1
        return len(nums)

if __name__=='__main__':
    s = Solution()
    list1 = []
    list2 = [1,1,2,2,3]
    print(s.removeElement(list1,1))
    print(s.removeElement(list2,4))