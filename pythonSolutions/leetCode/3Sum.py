# https://leetcode.com/problems/3sum

# Turn 3 sum into a 2 sum problem

class Solution:
    def threeSum(self,nums):
        
        nums.sort()
        
        list=[]
        
        for i,a in enumerate(nums):
            if i>0 and nums[i-1]==a:
                continue
            
            target=0-nums[i]
            
            l=i+1
            r=len(nums)-1
            
            while l<r:
                current=nums[l]+nums[r]
                
                if current<target:
                    l+=1
                elif current>target:
                    r-=1
                else:
                    list.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                    
        return list
        