import bst

#########
# BFS FUNCTIONS ADDED TO BST.PY BST CLASS
#########

my_tree= bst.Binary_Search_Tree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print("BSF : ",my_tree.DFS())
print("DFS: PreOrder : ",my_tree.DFS_PreOrder())
print("DFS: PostOrder : ",my_tree.DFS_PostOrder())
print("DFS: InOrder : ",my_tree.DFS_InOrder())