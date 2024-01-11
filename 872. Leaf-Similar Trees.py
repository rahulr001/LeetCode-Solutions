root1 = [3,5,1,6,2,9,8,None,None,7,4]
root2 = [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]


class Tree:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


def leafSimilar(root1, root2) -> bool:
    def dfs(root):
        if root is None:
            return []      
        else:
            return dfs(root.left) + dfs(root.right) or [root.value]
    return dfs(root1) == dfs(root2)  



root1 = Tree(3)
root1.left = Tree(5)
root1.right = Tree(1)
root1.left.left = Tree(6)
root1.left.right = Tree(2)
root1.right.left = Tree(9)
root1.right.right = Tree(8)
root1.left.right.left = Tree(7)
root1.left.right.right = Tree(4)

root2 = Tree(3)
root2.left = Tree(5)
root2.right = Tree(1)
root2.left.left = Tree(6)
root2.left.right = Tree(7)
root2.right.left = Tree(4)
root2.right.right = Tree(2)
root2.right.right.left = Tree(9)
root2.right.right.right = Tree(8)


print(leafSimilar(root1, root2))