def selection_sort(numbers):
    for i in range(len(numbers)-1):
        min_index=i
        for j in range(i+1,len(numbers)):
            if numbers[j]<numbers[min_index]:
                min_index=j
        if i!=min_index:
            temp=numbers[i]
            numbers[i]=numbers[min_index]
            numbers[min_index]=temp

    return numbers

nums=[3,5,2,10,42,1,9]
print(selection_sort(nums))