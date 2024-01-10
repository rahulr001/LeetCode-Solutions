Input = [3,9,20,None,None,15,7]

class Tree:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

def maxDepth(root) -> int:
    return 0 if root is None else max(maxDepth(root.left), maxDepth(root.right)) + 1


root = Tree(3)
root.left = Tree(9)
root.right = Tree(20)
root.left.left = Tree(15)
root.left.right = Tree(7)


print(maxDepth(root))