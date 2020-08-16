class Solution:
    def isValid(self, s: str) -> bool:
        # if odd, immediately false
        # make a stack. If open bracket, push. If closing, pop on match, return false if not
        # return len(stack) is 0, empty if balanced
        
        if len(s) is 0:
            return True
        if len(s) % 2 != 0:
            return False
        
        stack = []
        
        # if closing bracket doesn't eq top in stack, immediately false
        for val in s:
            #print('stack:',stack)
            if val is '{' or val is '(' or val is '[':
                stack.append(val)
                continue
            if val is '}' or val is ')' or val is ']':
                if len(stack) is 0:
                    return False
                top = stack[-1]
                if top is '{' and val is '}' or top is '(' and val is ')' or top is '[' and val is ']':
                    stack.pop()
                    
        return len(stack) is 0