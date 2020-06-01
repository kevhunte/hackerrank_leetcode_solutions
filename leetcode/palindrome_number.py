class Solution:
    def isPalindrome(self, x: int) -> bool:
        # negative, fail.
        # flip number and compare to input
        if(x < 0):
            return False
        copy = x
        flipped = 0
        
        while(copy > 0):
            flipped *= 10 #slide left
            ones = copy % 10
            copy = floor((copy - ones)/10) #slide right
            flipped += ones
        return x == flipped
