def mergeTwoSubarrays(nums, left, mid, right):
    temp = []
    index1 = left 
    index2 = mid + 1 
    while index1 <= mid and index2 <= right:
        if nums[index1] < nums[index2]:
            temp.append(nums[index1])
            index1 += 1
        else:
            temp.append(nums[index2])
            index2 += 1
            
    while index1 <= mid:
        temp.append(nums[index1])
        index1 += 1 
 
    while index2 <= mid:
        temp.append(nums[index2])
        index2 += 1    
 
    position = left 
    for ele in temp:
        nums[position] = ele 
        position += 1 
 
 
 
def mergeAndDivide(nums, left, right):
    if left >= right:
        return 
 
    mid = (left + right) // 2 
    mergeAndDivide(nums, left, mid)
    mergeAndDivide(nums, mid + 1, right)
    mergeTwoSubarrays(nums, left, mid, right)
 
 
 
def performMergeSort(nums):
    n = len(nums) 
    mergeAndDivide(nums, 0, n - 1)
 
nums = [10, 8, 2, 14, 12, 7, 9, 8, 4]
#nums = list(map(int, input().split()))
print("Before sorting:", nums)
 
performMergeSort(nums)
 
print("After sorting:", nums)