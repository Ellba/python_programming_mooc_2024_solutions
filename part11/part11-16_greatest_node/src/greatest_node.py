# WRITE YOUR SOLUTION HERE:
class Node:
    """ Class is modeling single node in binary tree """
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


def greatest_node(root: Node):
    big_man = root.value

    if root.left_child is not None:
        left_max = greatest_node(root.left_child)
        if big_man < left_max:
            big_man = left_max

    if root.right_child is not None:
        right_max = greatest_node(root.right_child)
        if big_man < right_max:
            big_man = right_max

    return big_man



if __name__ == "__main__":
    tree = Node(2)

    tree.left_child = Node(3)
    tree.left_child.left_child = Node(5)
    tree.left_child.right_child = Node(8)

    tree.right_child = Node(13)
    tree.right_child.right_child = Node(29)

    print(greatest_node(tree))