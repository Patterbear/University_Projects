class TreeNode():
    def __init__(self,item):
        self.item=item
        self.left=None
        self.right=None
    

class binarySearchTree():
    def __init__(self):
        self.root=None

    def insert(self,item):
        if self.root is None:
            self.root=TreeNode(item)
        else:
            self._insert(item,self.root)
    
    def _insert(self,item,currentNode):
        if item < currentNode.item:
            if currentNode.left is None:
                currentNode.left=TreeNode(item)
            else:
                self._insert(item,currentNode.left)
        elif item > currentNode.item:
            if currentNode.right is None:
                currentNode.right=TreeNode(item)
            else:
                self._insert(item,currentNode.right)
        else:
            print("Item is already existed in the tree")

    def search(self, item):
        return self.search_aux(self.root, item)

    def search_aux(self, root, item):
            if root == None:
                return False
            elif root.item == item:
                return True
            elif root.item > item:
                return self.search_aux(root.left, item)
            else:
                return self.search_aux(root.right, item)

    def find_minimum(self):
        if self.root == None:
            return None
        else:
            return self.find_min_aux(self.root, self.root.left)

    def find_min_aux(self, root, min_val):
        if root.left == None:
            return root.item
        else:
            return self.find_min_aux(root.left, min_val)
      
    def treeRange(self,a,b):
        targets = list(range(a+1, b))
        found = []
        for i in range(len(targets)):
            if self.search(targets[i]) == True:
                found.append(targets[i])
        return found
    

  # Traversal algorithm, will be discussed next week.
  
    def print_preorder(self):
        self._print_preorder_aux(self.root)
    def _print_preorder_aux(self,current):
        if current is not None:
            print(current.item)
            self._print_preorder_aux(current.left)
            self._print_preorder_aux(current.right)

            

bst=binarySearchTree()
bst.insert(24)
bst.insert(4)
bst.insert(3)
bst.insert(25)
bst.insert(13)
bst.insert(6)
bst.insert(45)
bst.insert(16)
bst.insert(67)
print("The minimum item is : " ,bst.find_minimum())
bst.print_preorder()
print(bst.treeRange(5,50))

print(bst.search(5))
