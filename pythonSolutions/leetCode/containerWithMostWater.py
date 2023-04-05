# https://leetcode.com/problems

class Solution:
    def maxArea(height):
        res=0
        
        l=0
        r=len(height)-1
        
        while l<r:
            current=min(height[l],height[r])*(r-l)
            res=max(current,res)

            if(height[l]<=height[r]):
                
                l+=1
            else:
                r-=1
            
            
        return res
    


        
       
        

