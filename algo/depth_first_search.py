from tree import Tree

tree = Tree()

tree.insert(9).insert(4).insert(1).insert(7).insert(12).insert(5).insert(11).insert(22).insert(21)

# print(tree.depth_search_tree())
# print(tree.depth_search_tree(9))

print(tree.depth_search_tree_in_order())
print(tree.depth_search_tree_pre_order())
print(tree.depth_search_tree_post_order())
