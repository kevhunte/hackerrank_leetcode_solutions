class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #search left and right. Return vals on first find of each
        ans = [-1,-1]
        #lfFound = False
        #rtFound = False
        length = len(nums)
        for left in range(length):
            right = length - left - 1
            if(nums[left] == target and ans[0] == -1):  #not lfFound
                #lfFound = True
                ans[0] = left
            if(nums[right] == target and ans[1] == -1): #not rtFound
                #rtFound = True
                ans[1] = right
            if(ans[0] != -1 and ans[1] != -1):
                return ans
        return ans
