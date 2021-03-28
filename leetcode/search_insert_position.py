class Solution:
    def searchHelper(nums: List[int], target: int) -> int:
        len_nums = len(nums)
        for i in range(len_nums):
            num = nums[i]
            if num >= target:
                return i
        return len_nums
    
    def searchInsert(self, nums: List[int], target: int) -> int:
        idx = Solution.searchHelper(nums,target)
        return idx