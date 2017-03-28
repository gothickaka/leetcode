class Solution(object):
    def maxSubArray(self, nums):
        result = nums[0]
        tmp = 0
        for i in range(len(nums)):
            tmp += nums[i]
            result = max(result, tmp)
            tmp = max(tmp, 0)
        return result

if __name__ == '__main__':
    s = Solution()
    list1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(s.maxSubArray(list1))
