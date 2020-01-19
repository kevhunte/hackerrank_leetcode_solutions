import itertools
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #create a dict with values for each digit.
        #get cartesian product for letters
        #process into string for ans
        letters = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz',
        }
        if(digits == ""):   #skip when empty
            return []
        combs = []
        for d in digits:        #gets codes
            combs.append(letters[d])
            
        products = itertools.product(*combs)    #makes combinations
        combs.clear()
        for p in products:
            combs.append(''.join(p))
        return combs
