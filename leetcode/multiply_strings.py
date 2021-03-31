class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num_1 = num_2 = 0
        
        # translate into int
        for i in num1:
            num_1 = (num_1*10) + int(i)
        for j in num2:
            num_2 = (num_2*10) + int(j)
            
        # cast back to a string
        return str(num_1 * num_2)