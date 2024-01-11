class Tree:
    def __init__(self, value) -> None:
        self.value = value
        self.parent = None
        self.child = []

    def insert(self, child):
        child.parent = self
        self.child.append(child)

    def print_tree(self):
        print(self.value)
        if self.child:
            for child in self.child:
                child.print_tree()
        
    def level(self):
        lev = 0
        p = self.parent
        while p:
            lev += 1
            p = p.parent
            
        return lev
    
root = Tree(4)
root.insert(Tree(5))

root.print_tree()
print(root.level())
