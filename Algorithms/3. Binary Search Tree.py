class Tree:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Tree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Tree(value)
            else:
                self.right.insert(value)

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
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()
        print(self.value)


root = Tree(3)
root.insert(4)
root.insert(1)
root.insert(3)
root.insert(11)
root.insert(34)
root.insert(9)
root.insert(5)
root.insert(6)
root.insert(8)

root.postorder_traversal()