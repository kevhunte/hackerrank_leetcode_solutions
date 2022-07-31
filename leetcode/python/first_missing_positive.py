class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # store all positive ints. check from 1 to the biggest to find first missing
        # if the biggest int in the list is negative, 1 is the answer
        # if all positive elements in the list are present, biggest int + 1 is the answer
        seen = set()
        biggestNum = max(nums)
        for num in nums:
            if (num > 0):
                seen.add(num)
        
        for i in range(1, biggestNum):
            if i not in seen:
                return i
        
        return biggestNum + 1 if biggestNum > 0 else 1