class TreeNode:
    def __init__(self,item=None):
        self.item=item
        self.left=None
        self.right=None
    

class BinaryTree:
    def __init__(self, root):
        self.root=TreeNode(root)

    def __len__(self):
        return self.len_aux(self.root)
    def len_aux(self,current):
        if current is None:
            return 0
        else:
            return 1+self.len_aux(current.left)+self.len_aux(current.right)

        
    

 #Task 1 ... Write your code here

    
    
    

ex=TreeNode(25)
bt=BinaryTree(ex)
bt.root.left=TreeNode(20)
bt.root.right=TreeNode(22)
bt.root.left.left=TreeNode(10)
bt.root.right.left=TreeNode(19)
bt.root.right.right=TreeNode(8)

print("The size of the binary tree is : ", bt.__len__())
#print("The sum of the leaves is : ",bt.sum_leaves())
