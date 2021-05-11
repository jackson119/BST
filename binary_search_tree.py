"""
initially all the node properties is None
"""
class Node():
    def __init__(self,value=None):
        self.value=value
        self.left=None
        self.right=None
        self.parent=None
        

class Bst():
    """
    initially there is no root in the tree,so we set it to None
    """
    def __init__(self):
        self.root=None
    
        
    """
    this is the insert function
    """
    def insert(self,value):
        if self.root is None:
            self.root=Node(value)
        else:
            self._insert(self.root,value)
            
    """
    helper function to implement recursive function
    -if value less than current node value and there are no left child in current node
    -insert the value to the current node and the current_node becomes the parent
    -if not it will continue with recursion fuction to insert the value .
    the bigger value will continue with same operation with another way.
    """
    def _insert(self,current_node,value):
        if value<current_node.value:
            if current_node.left is None:
                current_node.left=Node(value)
                current_node.parent=current_node
            else:
                self._insert(current_node.left,value)
   
        elif value>current_node.value:
            if current_node.right is None:
                current_node.right=Node(value)
                current_node.parent=current_node
            else:
                self._insert(current_node.right,value)
        else:
            print(str(value) + " is already inside the tree")
        
            
    """
    this method  allow tree to perform inorder
    if there are not root inside this function it will not print out the output
    """    
    def inorder(self,node):
        if node is not None:
            self.inorder(node.left)
            print(node.value)
            self.inorder(node.right)
    
    """
    this method allow tree to perform preorder and print out the output.
    if the root is not empty it will print out the tree
    """
    def preorder(self,node):
      if node is not None:
          print(node.value)
          self.preorder(node.left)
          self.preorder(node.right)
    """
    this method allow tree to perform post order and print out the output.
    if the root is not empty it will print out the value 
    """      
    def postorder(self,node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value)
         
            
    """
    if the root node is not empty it will call the recursion fuction else it will return false
    """
    def find(self,value):
        if self.root is not None:
            return self._find(self.root,value)
        else:
            return False
    """
    there are 3 parameters inside this function current,node and values
    
    """
    def _find(self,current_node,value):
        if value == current_node.value:
            return True
        elif value < current_node.value:
            if current_node.left is None:
                return False
            else:
                return self._find(current_node.left,value)
        elif value > current_node.value: 
            if current_node.right is  None:
                return False
            else:
                return self._find(current_node.right,value)
        else:
            return False
    """
    this method is usef for find the maximum height of the tree.
    """ 
    def Tree_max(self,node):
        if node is None:
            return 0
        else:
            return 1 + max(self.Tree_max(node.left), self.Tree_max(node.right))
    """
    this method is used for find the minimum height of the tree
    """
    def Tree_min(self,node):
        if node is None:
            return 0
        else:
            return 1 + min(self.Tree_min(node.left), self.Tree_min(node.right))
        
    def delete(self,value):
        """
        part 1 for root node
        """
        #Case 1: Empty Tree
        if self.root == None:
            return False
        #Case 2: Deleting root node
        if self.root.value == value:
            #Case 2.1: Root node has no children
            if self.root.left is None and self.root.right is None:
                self.root= None
            #Case 2.2: Root node has left child
            elif self.root.left is not None and self.root.right is None:
                self.root= self.root.left
                return True
            #Case 2.3: Root node has right child
            elif self.root.right is not None and self.root.left is None:
                self.root= self.root.right
                return True
            #Case 2.4: Root node has two children
            else:
                moveNode= self.root.right
                moveNodeParent= None               
                while moveNode.left:
                    moveNodeParent= moveNode
                    moveNode= moveNode.left
                ### copy move node to root node
                self.root.value= moveNode.value
                if moveNode.value < moveNodeParent.value:
                    moveNodeParent.left= None
                else:
                    moveNodeParent.right= None
                return True
        #Find node to remove
        """
        part 2 for children node 
        """
        parent=None
        root= self.root
        while  root.value != value:
            parent= root
            if value < root.value:
                root= root.left
            elif value> root.value:
                root= root.right
            #Case 1: Node not found
        """
        if there are no node , return false
        """
        if root == None or root.value!=value:
            return False
        #Case 2: node has no children
        elif root.left is None and root.right is None:
            ### every node compare with root node first
            if value < parent.value:
                parent.left= None
            else:
                parent.right= None
            return True
        #Case 3: Node has left child only
        # there are two case if remove the node that are smaller than root node
        elif root.left and root.right is None:
            if value < parent.value:
                parent.left= root.left
            else:
                parent.right= root.left
            return True
        #Case 4: Node has right child only
        # there are two case 
        elif root.right and root.left is None:
            if value < parent.value:
                parent.left= root.right
            else:
                parent.right= root.right
            return True
        #Case 7: node has right and left child
        
        else:
            # lowest value in the right tree
            moveNodeParent=root
            moveNode= root.right
            while moveNode.left:
                moveNodeParent= moveNode
                moveNode= moveNode.left
            # copy value
            root.value= moveNode.value
            if moveNode.right:
                if moveNode.value < moveNodeParent.value:
                    moveNodeParent.left= moveNode.value
                else:
                    moveNodeParent.right= moveNode.right
            else:
                if moveNode.value < moveNodeParent.value:
                    moveNodeParent.left= None
                else:
                    moveNodeParent.right= None
            return True


        
if __name__ == '__main__':
    tree=Bst()    
    tree.insert(15)
    tree.insert(11)
    tree.insert(5)
    tree.insert(6)
    tree.insert(15)
    print("this is inorder")
    tree.inorder(tree.root)

    print()
    print("this is preorder")
    tree.preorder(tree.root)
    
    print()
    print("this is postorder")
    tree.postorder(tree.root)
    print()
    print(tree.find(6))
    print(tree.Tree_max(tree.root))
    print()
    
    tree.delete(15)
    
    tree.inorder(tree.root)
        
                    
             


                
                
         
         



        
                
                 
                 
                 
             
             


