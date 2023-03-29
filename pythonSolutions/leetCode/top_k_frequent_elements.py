# https://leetcode.com/problems/top-k-frequent-elements

from collections import Counter

class Solution:
    def topKFrequent(self, nums,k: int):
        
        res=Counter(nums).most_common()

        return list(dict(res).keys())[0:k]