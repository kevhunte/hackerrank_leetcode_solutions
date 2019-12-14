def is_leap(year):
    leap = False
    
    if(year % 4 == 0): # by 4 good. Only exclude 100s not by 400.
        leap = True
        if(year % 100 == 0 and not year % 400 == 0):
            leap = False
    # Write your logic here
    
    return leap

year = int(raw_input())
print is_leap(year)
