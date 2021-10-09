class Solution:
    def balancedStringSplit(self, s: str) -> int:
        #make a stack. push similars and pop differences
        #Every time it's empty, increment counter
        #return counter
        ans = 1
        letter = []
        letter.append(s[0])
        for i in range(1,len(s)):
            if(len(letter) == 0): #if empty inc and put next val
                ans +=1
                letter.append(s[i])
            elif(letter[-1] == s[i]): #if repeat, add to list
                letter.append(s[i])
            else:   #different letter
                letter.pop()
        return ans
