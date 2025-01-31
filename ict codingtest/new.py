#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'balancedOrNot' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY expressions
#  2. INTEGER_ARRAY maxReplacements
#
input=sys.stdin.readline

def balancedOrNot(expressions, maxReplacements):
    result=[]
    for express,maxRep in zip(expressions,maxReplacements):
        # print(express,maxRep)
        arr=[]
        for x in express:
            if x=='<':
                arr.append('<')
            else: #> , <가 있는 경우 >가 있는 경우
                if len(arr)==0:
                    arr.append(x)
                else:
                    if arr[-1]=='<':
                        arr.pop() 
                    else:
                        arr.append(x)
        # print(arr)
        if len(arr)==0:
            result.append(1)
        else:
            if arr.count('<')>0:
                result.append(0)
            elif arr.count('>')==maxRep:
                result.append(1)
            else:
                result.append(0)
    return result
if __name__ == '__main__':
    n=int(input())
    expressions=[]
    for _ in range(n):
        s=input().strip()
        expressions.append(s)
    maxN=int(input())
    maxReplacements=[]
    for _ in range(maxN):
        maxReplacements.append(int(input()))
        
    
    rst=balancedOrNot(expressions,maxReplacements)
    print('\n'.join(map(str,rst)))
    # >>>>>>>>><<
    