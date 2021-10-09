class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dubs = dict()
        
        for n in nums:
            if n not in dubs:
                dubs[n] = 1
            else:
                dubs[n] += 1
        
        for key,val in dubs.items():
            if val == 1:
                return key
        
        return -1
        