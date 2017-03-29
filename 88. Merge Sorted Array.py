class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if n > 0:
            i = m
            j = 0
            while i < m+n:
                if i < len(nums1):
                    nums1[i] = nums2[j]
                else:
                    nums1.append(nums2[j])
                i += 1
                j += 1
            nums1.sort()

if __name__ == '__main__':
    s = Solution()
    list1 = [0]
    list2 = [1]
    print(s.merge(list1,0,list2,1))
