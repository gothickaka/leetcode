#kadanes algorithm
class Solution(object):
    def maxProfit(self, prices):
        tmp = 0
        result = 0
        for i in range(1,len(prices)):
            tmp = tmp + prices[i] - prices[i-1]
            tmp = max(0,tmp)
            result = max(tmp,result)
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([1,6,5]))
