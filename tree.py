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
            return self
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

    def breadth_search_tree(self, value=None):
        current = self.root
        lst = []
        queue = [current]

        if value and value == current.value:
            return value

        while queue:
            current = queue.pop(0)
            lst.append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return lst

    def breadth_search_tree_r(self, queue, lst, value=None):
        if not queue:
            return lst

        current = queue.pop(0)

        if value and value == current.value:
            return value

        lst.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

        return self.breadth_search_tree_r(queue, lst)

    def depth_search_tree_in_order(self):
        return traverse_in_order(self.root, [])

    def depth_search_tree_pre_order(self):
        return traverse_pre_order(self.root, [])

    def depth_search_tree_post_order(self):
        return traverse_post_order(self.root, [])


def traverse_in_order(node, lst):
    if node.left:
        traverse_in_order(node.left, lst)

    lst.append(node.value)

    if node.right:
        traverse_in_order(node.right, lst)

    return lst


def traverse_pre_order(node, lst):
    lst.append(node.value)
    if node.left:
        traverse_in_order(node.left, lst)

    if node.right:
        traverse_in_order(node.right, lst)

    return lst


def traverse_post_order(node, lst):
    if node.left:
        traverse_in_order(node.left, lst)

    if node.right:
        traverse_in_order(node.right, lst)

    lst.append(node.right.value)

    return lst

# test it
# tree = Tree()
# tree.insert(10)
# tree.insert(16).insert(14).insert(4).insert(8).insert(2).insert(19).insert(7).insert(3)
# print(tree.get_tree().right)
# print(tree.lookup(16))
#
# print(tree.remove(14))
# print(tree.get_tree())

