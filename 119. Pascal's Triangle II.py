class Solution(object):
    def getRow(self, rowIndex):
        pascal = []
        for i in range(rowIndex+1):
            pascal.append([1] * (i + 1))
            for j in range(1, i):
                pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
        return pascal[rowIndex]

if __name__ == '__main__':
    s = Solution()
    print(s.getRow(0))
