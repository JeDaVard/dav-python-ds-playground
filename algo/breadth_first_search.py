from tree import Tree

tree = Tree()

tree.insert(9).insert(4).insert(1).insert(7).insert(12).insert(5).insert(11).insert(22).insert(21)

print(tree.breadth_search_tree())
print(tree.breadth_search_tree(9))

print(tree.breadth_search_tree_r([tree.root], []))
print(tree.breadth_search_tree_r([tree.root], [], 9))
