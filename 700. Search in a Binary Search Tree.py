root = [4,2,7,1,3]
val = 2

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

def searchBST(root, val):
    if not root:
        return None
    if root.value == val:
        return root
    elif root.value < val:
        return searchBST(root.right, val)
    elif root.value > val:
        return searchBST(root.left, val)
        


root = Tree(4)
root.insert(2)
root.insert(7)
root.insert(1)
root.insert(3)

print(searchBST(root, val))