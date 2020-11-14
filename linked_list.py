class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, value=None):
        self.head = Node(value) if value else None

    def length(self):
        counter = 0
        node = self.head
        while node:
            node = node.next
            counter += 1

        return counter

    def list(self):
        lst = []
        node = self.head

        while node:
            lst.append(node)
            node = node.next

        return lst

    def prepend(self, value):
        self.head = Node(value, self.head or None)

        return self

    def get(self, index):
        length = self.length()
        if index < 0:
            return None
        if length == 0:
            return None
        if length - 1 < index:
            return None

        counter = 0
        node = self.head
        while counter < index:
            node = node.next
            counter += 1

        return node

    def first(self):
        return self.head

    def last(self):
        length = self.length()
        return self.get(length - 1) if length > 0 else None

    def append(self, value):
        last = self.last()
        if not last:
            self.head = Node(value)
        else:
            last.next = Node(value)

        return self

    def insert(self, index, value):
        if index == 0:
            return self.prepend(value)

        length = self.length()

        if index == length - 1:
            return self.append(value)

        if index > length - 1 or index < 1:
            return self

        prev_node = self.get(index - 1)
        node = Node(value, prev_node.next)
        prev_node.next = node

        return self

    def delete(self, index):
        if index < 0:
            return None
        node = self.get(index - 1)
        if not node:
            return None

        node_to_remove = node.next
        node.next = node.next.next

        return node_to_remove


linked_list = LinkedList()
linked_list.prepend('hello').prepend('hello').prepend('hello').prepend('hello').prepend('hello')
print(linked_list.get(2))
print(linked_list.last())
linked_list.append('hello').append('hello').append('hello')
print(linked_list.length())
print(linked_list.list())
