#!/bin/python3

import math
import os
import random
import re
import sys
def solve(s):
    x=s.split(' ')
    k=[element.capitalize() for element in x]
    return ' '.join(k)
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
