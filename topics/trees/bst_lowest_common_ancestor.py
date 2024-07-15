from typing import Optional

class Node:
    def __init__(self, data):
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        self.data: int = data

def insert(root: Optional[Node], data: int) -> Optional[Node]:
    if root is None:
        return Node(data) # type: ignore
    else:
        if data < root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root

def lca(root, v1, v2):
    while root:
        if root.data > v1 and root.data > v2:
            root = root.left
        elif root.data < v1 and root.data < v2:
            root = root.right
        else:
            return root


# class Node:
#     def __init__(self, info): 
#         self.info = info  
#         self.left = None  
#         self.right = None 
#         self.level = None 

#     def __str__(self):
#         return str(self.info) 

# class BinarySearchTree:
#     def __init__(self): 
#         self.root = None

#     def create(self, val):  
#         if self.root == None:
#             self.root = Node(val)
#         else:
#             current = self.root
         
#             while True:
#                 if val < current.info:
#                     if current.left:
#                         current = current.left
#                     else:
#                         current.left = Node(val)
#                         break
#                 elif val > current.info:
#                     if current.right:
#                         current = current.right
#                     else:
#                         current.right = Node(val)
#                         break
#                 else:
#                     break

# # Enter your code here. Read input from STDIN. Print output to STDOUT
# '''
# class Node:
#       def __init__(self,info): 
#           self.info = info  
#           self.left = None  
#           self.right = None 
           

#        // this is a node of the tree , which contains info as data, left , right
# '''

# def lca(root, v1, v2):
#   while root:
#       if root.info > v1 and root.info > v2:
#           root = root.left
#       elif root.info < v1 and root.info < v2:
#           root = root.right
#       else:
#           return root

# tree = BinarySearchTree()
# t = int(input())

# arr = list(map(int, input().split()))

# for i in range(t):
#     tree.create(arr[i])

# v = list(map(int, input().split()))

# ans = lca(tree.root, v[0], v[1])
# print (ans.info)
