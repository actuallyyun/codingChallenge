# https://leetcode.com/problems/top-k-frequent-elements

from collections import Counter

class Solution:
    def topKFrequent(self, nums,k: int):

        return [x[0] for x in Counter(nums).most_common(k)]