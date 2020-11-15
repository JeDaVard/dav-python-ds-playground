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

    def remove(self, value):
        if not self.root:
            return None

        current = self.root
        parent = None

        while current:
            if value < current.value:
                parent = current
                current = current.left
            elif value > current.value:
                parent = current
                current = current.right
            elif value == current.value:
                if not current.right:
                    if not parent:
                        self.root = current.left
                    else:
                        if current.value < parent.value:
                            parent.left = current.left
                        elif current.value > parent.value:
                            parent.right = current.left
                elif not current.left.right:
                    current.right.left = current.left
                    if not parent:
                        self.root = current.right
                    else:
                        if current.value < parent.value:
                            parent.left = current.right
                        elif current.value > parent.value:
                            parent.right = current.right
                else:
                    left_most = current.right.left
                    left_most_parent = current.right

                    while left_most.left:
                        left_most_parent = left_most
                        left_most = left_most.left

                    left_most_parent.left = left_most.right
                    left_most.left = current.left
                    left_most.right = current.right

                    if not parent:
                        self.root = left_most
                    else:
                        if current.value < parent.value:
                            parent.left = left_most
                        elif current.value > parent.value:
                            parent.right = left_most

                return True


tree = Tree()
tree.insert(10)
tree.insert(16).insert(14).insert(4).insert(8).insert(2).insert(19).insert(7).insert(3)
print(tree.get_tree().right)
print(tree.lookup(16))

print(tree.remove(14))
print(tree.get_tree())

