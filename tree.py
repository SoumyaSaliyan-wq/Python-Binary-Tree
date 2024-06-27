# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

class TreeNode:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.value=value
    
    def insert(self,value):
        if value<self.value:
            if self.left is None:
                self.left=TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right=TreeNode(value)
            else:
                self.right.insert(value)
    ##It prints the deep most left value where we dont have any left the firls value of the traversal will be the last left value
    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.value)
        if self.right:
            self.right.inorder_traversal()
            
    def preorder_traversal(self):
        print(self.value)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()
            
    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.value)

    def find(self,value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None :
                return False
            else:
                return self.right.find(value)
        else:
            return True
                
tree=TreeNode(10)
tree.insert(5)
tree.insert(34)
tree.insert(3)
# print(tree.preorder_traversal())
# 10
# 5
# 3
# 34
# None
# print(tree.postorder_traversal())
# 3
# 5
# 34
# 10
# None

# print(tree.inorder_traversal())
# 3
# 5
# 10
# 34
# None
