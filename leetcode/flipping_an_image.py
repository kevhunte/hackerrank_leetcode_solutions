class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        #pop and append to new list to reverse
        #Then invert digits
        ans = []
        for i in A:
            temp = []
            while(len(i)> 0):
                #val = i.pop()
                if(i.pop() == 1):
                    temp.append(0)
                else:
                    temp.append(1)
            ans.append(temp)
        #print(ans)
        return ans
