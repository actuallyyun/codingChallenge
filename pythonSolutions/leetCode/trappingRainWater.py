class Solution:
    def trap(height):
        l,r=0,len(height)-1
        maxL,maxR=height[l],height[r]
        res=0

        while l<r:
            if(maxL<maxR):
                l+=1
                maxL=max(maxL,height[l])
                trap=maxL-height[l]
                res+=trap
            else:
                r-=1
                maxR=max(maxR,height[r])
                trap=maxR-height[r]
                res+=trap

        return res