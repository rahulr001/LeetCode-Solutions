root = [5,3,6,2,4,None,7]
key = 3

class Tree:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        if self.val > val:
            if self.left is None:
                self.left = Tree(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = Tree(val)
            else:
                self.right.insert(val)
                 


def deleteNode(root, key):
    def min_value_node(node):
            while node.left is not None:
                node = node.left
            return node
    if root is None:
        return root

    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = min_value_node(root.right)
        root.val = temp.val
        root.right = deleteNode(root.right, temp.val)

    return root



        



root = Tree(5)

root.insert(3)
root.insert(6)
root.insert(2)
root.insert(4)
root.insert(7)

print(deleteNode(root, key))

