class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # handles invalid input
        if not haystack:
            return 0 if not needle else -1
        
        try:
            return haystack.index(needle)
        except:
            return -1