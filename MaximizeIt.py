from itertools import product
matrix = []
possibleS = []

#load data for combinations needed
def loadMatrix(row,string):
    lst = string.split(' ')
    num = []
    for i in range(1,len(lst)):
        num.append(int(lst[i]))
    matrix.append(num)

#helper function to make S's
def makeS(lst, mod):
    ans = 0
    #print(lst)
    for i in range(len(lst)):
        num = lst[i]
        ans += (num * num)
    return ans % mod

#1) Load data 
#2) Make combinations (cartesian product)
#3) Make S for each combination 
#4) Print max S
if __name__ == '__main__':
    iters, mod = raw_input().split(' ')
    mod = int(mod)
    iters = int(iters)

    for i in range(iters):
        loadMatrix(i,raw_input())

    for prod in product(*matrix): #unpack lists from matrix
        possibleS.append(makeS(prod,mod))

    print(max(possibleS))

