#-------------------------------------------------------------------------------
#
# The purpose of this file is to exercise some Python by way of mathematics.
#
#-------------------------------------------------------------------------------

def get_cycle_length(n):
    steps = 1
    while( n != 1):
        if n % 2 == 0 :
                n = n / 2
                steps += 1
        elif n % 2 == 1:
                n = n * 3 + 1
                steps += 1
    return steps

def get_cycle_length_range(start, end):
    max_steps = 0
    if start < end :
        a , b = start, end
    else: 
        a , b = end, start
    for n in range (a, b+1):
        if get_cycle_length(n) > max_steps:
            max_steps = get_cycle_length(n)
    return max_steps
