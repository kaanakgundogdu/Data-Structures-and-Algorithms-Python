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

my_bs_tree=Binary_Search_Tree()
my_bs_tree.insert(2)
my_bs_tree.insert(1)
my_bs_tree.insert(3)
my_bs_tree.insert(2)

print(my_bs_tree.root.value)
print(my_bs_tree.root.left.value)
print(my_bs_tree.root.right.value)
