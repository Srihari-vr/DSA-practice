# ez way using python just add botht the lists

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=nums+nums
        return ans
    
#traditional way of using a new list and placing the elements
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n= len(nums)
        ans=[0]*(2*n)
        for i in range(n):
            ans[i]=nums[i]
            ans[i+n]=nums[i]
        return ans