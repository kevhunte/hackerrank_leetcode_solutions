
import re

# Enter your code here. Read input from STDIN. Print output to STDOUT
def processNumbers(card):
    #ans = 'Valid'
    rules = [0]*6
    rules[3] = 1 #negative checks below
    rules[4] = 1
    rules[5] = 1
    if('4' == card[0] or '5' == card[0] or '6' == card[0]): rules[0] = 1
    if(len(card) == 16 or (len(card) == 19 and card.count('-') == 3)): rules[1] = 1
    if(re.match(r'^([0-9,-]+)$', card) is not None): rules[2] = 1 #may have to check
    if('-' in card):
        for c in card.split('-'): 
            if(len(c) != 4): 
                rules[3] = 0 
                return 'Invalid'
    if(' ' in card or '_' in card): 
        rules[4] = 0 
        return 'Invalid'
    #check with stack. If stack hits 4, then has 4 repeats. Fail
    repeats = []
    for c in card:
        if(len(repeats) < 1):
            repeats.append(c)
        elif(c == '-'): continue
        elif(c == repeats[-1]):
            repeats.append(c)
            if(len(repeats) > 3): 
                rules[5] = 0 
                return 'Invalid'
        else:
            repeats.clear()
    #each rule is an index. If any zeros at end, print 'Invalid'
    if(0 in rules):
        return 'Invalid'
    else:
        return 'Valid'

    #print(card,rules)


iters = int(input())

for _ in range(iters):
    print(processNumbers(input()))

