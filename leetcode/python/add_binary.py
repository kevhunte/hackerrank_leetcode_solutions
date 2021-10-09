class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # go through strings in reverse and add bits
        # if bit sum + carry greater than 1,  add overflow to carry, and set val to '0'
        # else
        
        ans = []
        carry = 0
        alist = list(a)
        blist = list(b)
        
        while alist and blist:
            bit_sum = int(alist.pop()) + int(blist.pop()) + carry
            #print(a,b,'bit_sum:',bit_sum, 'ans: ',''.join(ans))
            
            if bit_sum == 0:
                ans.insert(0,'0')
                carry = 0
            elif bit_sum == 1:
                ans.insert(0,'1')
                carry = 0
            elif bit_sum == 2:
                ans.insert(0,'0')
                carry = 1
            elif bit_sum == 3:
                ans.insert(0,'1')
                carry = 1
                
        while alist:
            bit_sum = int(alist.pop()) + carry
            
            if bit_sum == 0:
                ans.insert(0,'0')
                carry = 0
            elif bit_sum == 1:
                ans.insert(0,'1')
                carry = 0
            elif bit_sum == 2:
                ans.insert(0,'0')
                carry = 1
            elif bit_sum == 3:
                ans.insert(0,'1')
                carry = 1
                
        while blist:
            bit_sum = int(blist.pop()) + carry
            
            if bit_sum == 0:
                ans.insert(0,'0')
                carry = 0
            elif bit_sum == 1:
                ans.insert(0,'1')
                carry = 0
            elif bit_sum == 2:
                ans.insert(0,'0')
                carry = 1
            elif bit_sum == 3:
                ans.insert(0,'1')
                carry = 1
        if carry > 0:
            ans.insert(0,str(carry))
            carry = 0
        
        return ''.join(ans)