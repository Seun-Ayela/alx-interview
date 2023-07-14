#!/usr/bin/python3
'''Interview Challenge module
'''


def minOperations(n):
    '''finds no of time opertion is performed
    '''
    if not isinstance(n, int) or n < 0 or n == 1:
        return 0
    var = 1
    count = 0
    dup = 0
    while var < n:
        if n % var != 0:
            var += dup
            count += 1
        else:
            dup = var
            var += dup
            count += 2
    return (count if var == n else 0)
