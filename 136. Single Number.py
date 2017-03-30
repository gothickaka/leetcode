class Solution(object):
    def singleNumber(self, nums):
        for i in range(1,len(nums)):
            nums[0] = nums[0] ^ nums[i]
        return nums[0]

if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([1,2,1]))
