def pivot(nums,pivot_index, end_index):
    swap_index=pivot_index

    for i in range(pivot_index + 1, end_index + 1):
        if nums[i] < nums[pivot_index]:
            swap_index+=1
            swap(nums, swap_index, i)

    swap(nums, pivot_index,swap_index)
    return swap_index

def swap(nums, index1,index2):
    temp=nums[index1]
    nums[index1] = nums[index2]
    nums[index2] = temp

def quick_sort_handler(nums,left,right):
    if left<right:
        pivot_index= pivot(nums, left,right)
        quick_sort_handler(nums,left,pivot_index - 1)
        quick_sort_handler(nums, pivot_index + 1, right)
    return nums

def quick_sort(nums):
    return quick_sort_handler(nums,0,len(nums)-1)

nums=[4,7,1,5,9,2,8,3,6]

print(quick_sort(nums))
