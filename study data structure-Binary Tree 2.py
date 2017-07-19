from collections import deque
class Node:
    def __init__(self, data, **kwargs):
        self.data = data
        self.freq = kwargs.get('frequent', None)
        self.left = kwargs.get('left', None)
        self.right = kwargs.get('right', None)
        # self.child = kwargs.get('child', None)
def insert_node(root, node_value, frequent = None):
    new_node = Node(node_value, frequent=frequent)
    if root is None:
        return new_node
    if node_value > root.data:
        root.right = insert_node(root.right, node_value)
    else:
        root.left = insert_node(root.left, node_value)
    return root

def print_tree(root):
    if root is None:
        return
    print_tree(root.left)
    print(root.data, end = ' ')
    print_tree(root.right)

def decodeHuff(root , s):
   #Enter Your Code Here
    if root is None:
        return
    current = root
    position = 0
    while position < len(s):
        if int(s[position]) == 0:
            if current.left is None:
                print(current.freq, end='')
                current = root
            else:
                current = current.left
        elif int(s[position]) == 1:
            if current.right is None:
                print(current.freq, end = '')
                current = root
            else:
                current = current.right
        position += 1

def main():
    first_root = Node(0)

    insert_node(first_root, 0)
    insert_node(first_root, 1, 'A')
    first_root.left.left = insert_node(first_root.left.left, 0, 'B')
    first_root.left.right = insert_node(first_root.left.right, 1, 'C')
    print_tree(first_root)
    decodeHuff(first_root, "1001011")

if __name__ == '__main__':
    main()

