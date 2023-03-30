# not optimazied solution
import math

def product_of_array_except_self_1(self,nums):
    answer=[]
    for index,value in enumerate(nums):
        nums.remove(value)
        answer.append(math.prod(nums))
        nums.insert(index,value)


    return answer


# o(n) solution using prefix and postfix array
class Solution:
    def productExceptSelf(self, nums):

        res=[1]*len(nums)

        prefix=1
        
        for i in range(len(nums)):
            res[i]=prefix
            prefix*=nums[i]

        postfix=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]

        return res