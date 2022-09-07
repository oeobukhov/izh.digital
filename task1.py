import os 
import sys
filename = sys.argv[1]
    with open(filename) as file:
line = file.readline().split()
n, m=int(line[0]), int(line[1])
beg=m
print("1", end='')
while beg%n!=1:
    if beg%n==0: print(n, end='')
    else: print(beg%n, end='')
    beg+=m-1
