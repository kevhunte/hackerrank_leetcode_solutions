class Solution:
    
    # makes new list
    def mergeLists(self, nums1: List[int], nums2: List[int]) -> list:
        nums = []
        while len(nums1) > 0 and len(nums2) > 0:
            nums.append(nums1.pop(0) if nums1[0] < nums2[0] else nums2.pop(0))
        
        while len(nums1) > 0:
            nums.append(nums1.pop(0))
        
        while len(nums2) > 0:
            nums.append(nums2.pop(0))
        
        return nums
    
    # merges into list1
    def mergeLists2(self, nums1: List[int], nums2: List[int]) -> list:
        i = 0
        while len(nums2) > 0:
            if len(nums1) <= i or nums2[0] < nums1[i]:
                nums1.insert(i, nums2.pop(0))
            i += 1
        
        return nums1
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # merge lists and then find median
        
        nums = self.mergeLists2(nums1, nums2)
        
        return nums[len(nums)//2] if len(nums) % 2 != 0 else (nums[len(nums)//2 - 1] + nums[len(nums)//2])/2