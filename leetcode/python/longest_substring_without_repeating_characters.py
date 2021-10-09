class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #go through string, and make set with seen values this iteration
        #move right index for all unique values, check curr max with length of set
        #edge case, if s less than 2, return length
        longest = 0
        if len(s) < 2:
            return len(s)
        
        for i in range(len(s)):
            seen = set()
            seen.add(s[i])
            for j in range(i+1,len(s)):
                if(s[j] in seen):
                    break
                else:
                    seen.add(s[j])
            currSum = len(seen)
            longest = currSum if currSum > longest else longest
            if(longest == len(s)):
                return longest # max possible, no need to keep going
                
        return longest
