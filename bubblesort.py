def performBubbleSort(nums):
    n = len(nums)
    fixThisIndex = n - 1 
 
    while fixThisIndex > 0:
        for index in range(fixThisIndex):
            if nums[index] > nums[index + 1]:
                temp = nums[index] 
                nums[index] = nums[index + 1]
                nums[index + 1] = temp 
        print(nums)
 
        fixThisIndex -= 1 
 
def performSelectionSort(nums): 
    n = len(nums)
    fixThisIndex = n - 1 
    while fixThisIndex > 0:
        maxEleIndex = fixThisIndex
 
 
        if maxEleIndex != fixThisIndex:
            temp = nums[maxEleIndex] 
            nums[maxEleIndex] = nums[fixThisIndex]
            nums[fixThisIndex] = temp 
        print(nums)
        fixThisIndex -= 1 
 
def performInsertionSort(nums):
    n = len(nums)
    lastEleInSortedArr = 0 
    for firstIndex in range(1, n):
        temp = nums[firstIndex]
        previous = lastEleInSortedArr 
 
        # [7, 9, 12, 34]
        while previous >= 0 and nums[previous] > temp:
            nums[previous + 1] = nums[previous]
            previous -= 1 
        nums[previous + 1] = temp 
        lastEleInSortedArr += 1
 
nums = [10, 8, 2, 14, 12, 7]
#nums = list(map(int, input().split()))
print("Before sorting:", nums)
 
performInsertionSort(nums)
 
print("After sorting:", nums)