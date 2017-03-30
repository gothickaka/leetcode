class Solution(object):
    def maxProfit(self, prices):
        result = 0
        for i in range(0, len(prices)-1):
            if prices[i+1] > prices[i]:
                result += prices[i+1] - prices[i]
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([1,6,8,3,5]))
