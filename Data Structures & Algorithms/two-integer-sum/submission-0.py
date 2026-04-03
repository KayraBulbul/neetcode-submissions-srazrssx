class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in values.keys():
                return [values[difference], i]
            else:
                values[nums[i]] = i