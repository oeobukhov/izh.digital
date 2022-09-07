import os 
import sys
filename = sys.argv[1]
with open(filename) as file:
    nums = file.readlines()
nums = [int(line.rstrip()) for line in nums]
n=len(nums)
min=0
for j in range(n):
    min+=abs(nums[0]-nums[j])
for i in range(1,n-1):
    sum=0
    for j in range(n):
        sum+=abs(nums[i]-nums[j])
    if sum<min: min=sum
print(min)


