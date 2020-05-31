class Solution:
    def longestPalindrome(self, s: str) -> str:
        #two pointers, left and right. Use to make a substring
        #reverse substring each time and compare to see if it is a palindrome
        #if it is, take the max of that and what's currently saved
        #optimization: only reverse / check strings that are longer than current max
        #this can be done by moving pointer through loop while less than current max
        ans = ""
        if(len(s) < 2):
            return s
        
        for i in range(len(s)):
            j=i
            while(j < len(s)):
                substring = s[i:j+1]
                #print(i,j,substring)
                if(substring == substring[::-1]):
                    ans = substring if len(substring) > len(ans) else ans
                j = len(ans) if j < len(ans) else j + 1 #optimization: bigger subs only
            if(len(s) - i <= len(ans)):
                return ans #optimization: return when later poss combs < current answer
                    
        return ans
