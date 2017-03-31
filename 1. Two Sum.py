class Solution(object):
    def twoSum(self, nums, target):
        i = 0
        while i<len(nums)-1:
            j = i+1
            while j < len(nums):
                if nums[i]+nums[j] == target:
                    return [i,j]
                else:
                    j = j+1
            i = i+1

if __name__=='__main__':
    numlist = [1,2,3,4,5]
    s = Solution()
    print(s.twoSum(numlist,7))