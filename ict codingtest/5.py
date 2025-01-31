#!/bin/python3
'''
이 문제는 서버 작업 스케줄링에 관한 것입니다. 차근차근 설명해드리겠습니다:

1. 기본 상황:
- 두 개의 서버가 있습니다: 유료 서버와 무료 서버
- 무료 서버는 유료 서버가 사용 중일 때만 사용할 수 있습니다
1. 서버 특징:
- 유료 서버: 각 작업마다 비용(cost)이 발생하고, 작업 완료에 time[i] 시간이 걸립니다
- 무료 서버: 비용은 0이고, 모든 작업을 1시간 안에 처리합니다
1. 목표:
- 모든 작업을 완료하는데 필요한 최소 비용을 찾는 것입니다
1. 예시:
- n = 4개의 작업이 있고
- 비용은 cost = [1, 1, 3, 4]
- 시간은 time = [3, 1, 2, 3]일 때
- 첫 번째 작업을 유료 서버에서 실행하고(비용 1),
나머지 작업들은 무료 서버에서 실행하면 총 비용 1로 모든 작업을 완료할 수 있습니다s
'''
import math
import os
import random
import re
import sys
input=sys.stdin.readline


def getMinCost(cost, time):
    arr=[]
    for i in range(len(cost)):
        arr.append([cost[i],time[i]])
    arr.sort(key=lambda x:(-x[1],x[0]))
    timer=0
    minCost=0
    for i in range(len(cost)):#작업이 4개
        #0 1 
        minCost+=arr[i][0] #2 2
        timer+=arr[i][1] #1 (1+1=2)
        if timer>=(len(cost)-(i+1)): #남은 작업 개수 보다 크거나 같으면 
            break
    
    return minCost
    
if __name__ == '__main__':
    cost=[]
    time=[]
    n=int(input())
    for _ in range(n):
        cost.append(int(input()))
    m=int(input())
    for _ in range(m):
        time.append(int(input()))
    print(getMinCost(cost,time))