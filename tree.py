class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def get_tree(self):
        return self.root

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            current = self.root

            while True:
                if value < current.value:
                    if not current.left:
                        current.left = Node(value)
                        return self
                    current = current.left
                else:
                    if not current.right:
                        current.right = Node(value)
                        return self
                    current = current.right

    def lookup(self, value):
        node = self.root
        while node:
            if value < node.value:
                node = node.left
            elif value > node.value:
                node = node.right
            elif value == node.value:
                return node

        return None


tree = Tree()
tree.insert(10)
tree.insert(16).insert(14)
print(tree.get_tree().right)
print(tree.lookup(16))
