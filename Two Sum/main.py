class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        traversed = {}
        
        for i, value in enumerate(nums):
            req_num = target - nums[i]
            
            if req_num in traversed:
                return [i, traversed[req_num]]
            
            traversed[value] = i
        
        
        
        
nums = [2,7,11,15]
target = 9
sum = Solution()
indices = sum.twoSum(nums, target)
print(indices)