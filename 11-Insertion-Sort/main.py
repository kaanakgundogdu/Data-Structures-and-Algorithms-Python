def insertion_sort(nums):
    for i in range(1,len(nums)):
        temp=nums[i]
        j=i-1
        while temp< nums[j] and j>-1:
            nums[j+1] = nums[j]
            nums[j] = temp
            j-=1
    return nums

nums=[3,5,2,10,42,1,9]
print(insertion_sort(nums))