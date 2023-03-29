# https://leetcode.com/problems/group-anagrams/


from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        # define a hashmap to store key value pairs
        res=defaultdict(list)

        for s in strs:
            
            # declare a default array with 26 0s representing 26 english alphabets
            count=[0]*26

            for c in s:
                # count each alphabets in a given word
                count[ord(c)-ord('a')]+=1

            # store the counted array as key, and the word as value in the hashmap
            res[tuple(count)].append(s)

            #return values
        return res.values()
