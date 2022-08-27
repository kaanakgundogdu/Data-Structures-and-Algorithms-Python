from tkinter.messagebox import NO


class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class Binary_Search_Tree:
    def __init__(self):
        self.root=None
    
    def insert(self,val):
        new_node=Node(val)
        if self.root is None:
            self.root=new_node
            return True
        temp=self.root
        while (True):
            if new_node.value==temp.value:
                return False
            if new_node.value<temp.value:
                if temp.left is None:
                    temp.left=new_node
                    return True
                temp=temp.left
            else:
                if temp.right is None:
                    temp.right=new_node
                    return True
                temp=temp.right

    def contains(self,value):
        temp= self.root
        while temp is not None:
            if value<temp.value:
                temp=temp.left
            elif value>temp.value:
                temp=temp.right
            else:
                return True
        return False
    
    def min_value_node(self,current_node):
        while current_node.left is not None:
            current_node=current_node.left
        return current_node.value


my_bs_tree=Binary_Search_Tree()
my_bs_tree.insert(2)
my_bs_tree.insert(1)
my_bs_tree.insert(3)
my_bs_tree.insert(2)

print(my_bs_tree.root.value)
print(my_bs_tree.root.left.value)
print(my_bs_tree.root.right.value)
print("-----------------")
print("is tree contains 4: ",my_bs_tree.contains(4))
print("is tree contains 2: ",my_bs_tree.contains(2))

my_bs_tree.insert(54)
my_bs_tree.insert(23)
my_bs_tree.insert(0)
my_bs_tree.insert(99)
print("-----------------")
print("root's min value is: ",my_bs_tree.min_value_node(my_bs_tree.root))
print("subtree of  1's min value is: ",my_bs_tree.min_value_node(my_bs_tree.root.left))
print("subtree of  3's min value is: ",my_bs_tree.min_value_node(my_bs_tree.root.right))
