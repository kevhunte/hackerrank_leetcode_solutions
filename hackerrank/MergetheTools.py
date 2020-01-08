def merge_the_tools(string, k):
    # your code goes here
    it = 0
    for _ in range(len(string)/k): #logic works here to make ti
        ti = string[it:k+it]
        print(remove_repeats(ti))
        it = it + k
    #print(ans)

def remove_repeats(ti):
    #make dict. If has key, not a unique char.
    uniques = {}
    new_ti = ""
    for i in range(len(ti)):
        letter = ti[i]
        if(not uniques.has_key(letter)):
            uniques[letter]=ti[i] #technically same thing. Here for clarity
            new_ti = new_ti+letter
    return new_ti

if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)
    
