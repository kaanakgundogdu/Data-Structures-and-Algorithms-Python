def merge(list1,list2):
    combined_list=[]
    i=0
    j=0
    while i< len(list1) and j<len(list2):
        if list1[i] < list2[j]:
            combined_list.append(list1[i])
            i+=1
        else:
            combined_list.append(list2[j])
            j+=1
    while i< len(list1):
        combined_list.append(list1[i])
        i+=1
    while j<len(list2):
        combined_list.append(list2[j])
        j+=1
    
    return combined_list


def merge_sort(nums):
    if len(nums) == 1:
        return nums
    mid =int(len(nums) / 2)
    left = nums[:mid]
    right = nums[mid:]
    return merge(merge_sort(left), merge_sort(right))

print(merge_sort([1,6,12,2,30,5,9,11,40]))
