def performSelectionsort(nums):
    n = len(nums)
    fixThisIndex = n-1
    while fixThisIndex>0:
        maxEleIndex = fixThisIndex

        for i in range(fixThisIndex):
            if nums[i] > nums[maxEleIndex]:
                maxEleIndex = i
        
        if maxEleIndex != fixThisIndex:
            temp = nums[maxEleIndex]
            nums[maxEleIndex] = nums[fixThisIndex]
            nums[fixThisIndex] = temp
        print(nums)
        fixThisIndex -= 1
nums = [10,8,2,14,12,7]
print("before sirtinf:",nums)

performSelectionsort(nums)
print("after sorting:",nums)