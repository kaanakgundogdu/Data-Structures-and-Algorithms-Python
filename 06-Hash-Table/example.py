def item_in_common(list1,list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True
    for j in list2:
        if j in my_dict:
            return True,j
    return False

list_1=[1,2,3,4,5]
list_2=[10,20,30,40,50]

print(item_in_common(list_1,list_2))