class Solution(object):
    def searchInsert(self, nums, target):
        min = 0
        max = len(nums)-1
        while min<=max:
            i = min + (max-min)/2
            if nums[i] == target:
                return i
            elif nums[i] < target:
                min = i + 1
            else:
                max = i - 1
        return min

if __name__=='__main__':
    s = Solution()
    list1 = [1,2,4,5]
    list2 = [1,5,8,9]
    print(s.searchInsert(list1,3))
    print(s.searchInsert(list2,9))