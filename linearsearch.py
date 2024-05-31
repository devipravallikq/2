nums = [12, 10, 6, 23, 123]
target = 23
flag = -1
n = len(nums)
for index in range(n):
    if nums[index] == target:
        flag = index 
        break 
if flag == -1:
    print("Not found")
else:
    print("Target found at:", flag)