# Best time to buy and sell stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def maxProfit(prices):

    maxP=0
    l,r=0,1

    while r<len(prices):
        if prices[l]<prices[r]:
            maxP=max(maxP,prices[r]-prices[l])
        else:
            l=r
        
        r+=1

    return maxP