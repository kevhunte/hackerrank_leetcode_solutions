# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

uniques = OrderedDict() #sorts strings in alphabetical order

def processWords(word):
    if(uniques.has_key(word)): #add new occurence
        uniques[word] += 1
    else:                      #add key for first occurence
        uniques[word] = 1
        
#make a dict. Print # of keys for first ans and values for second ans
iters = int(raw_input())
values = ""

for _ in range(iters):
    processWords(raw_input())

for n in uniques.values():
    values += str(n)+' '

print(len(uniques))
print values
