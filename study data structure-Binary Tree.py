import sys
from collections import deque
class Node:
    def __init__(self, data, **kwargs):
        self.data = data
        self.left_child = kwargs.get('left_child', None)
        self.right_child = kwargs.get('right_child', None)


def search(root, data):
    current = root
    print('current is: ',current.data)

    while current.data != data:
        if current:
            print(' searching at current is: ', current.data)
        else:
            print('No data found')
            return

        if current.data > data:
            current = current.left_child

        if current.data < data:
            current = current.right_child
    return current.data

def insert(root,data):
    '''
    :param root: pointer to the root of the BST
    :param data: data of the new node
    :return: pointer to the root of new BST
    '''
    new_node = Node(int(data), left_child=None, right_child=None)
    if root is None:
        return new_node
    current = root
    while True:
        parent = current
        if parent.data > data:
            current = current.left_child
            if current is None:
                parent.left_child = new_node
                return root
        else:
            current = current.right_child
            if current is None:
                parent.right_child = new_node
                return root


def delete_node(root, data):
    '''
    :param root: pointer to the head or the BST
    :param data: delete the node with data
    :return: pointer to the head of a new BST
    '''
    if root is None:
        return root
    if root.data == data:
        return None
    if root.data > data:
        root.left_child = delete_node(root.left_child, data)
#TODO: Print tree
def pre_order(root):
    if root is None:
        return
    print(root.data, end=' ')
    pre_order(root.left_child)
    pre_order(root.right_child)

def post_order(root):
    if root is None:
        return
    post_order(root.left_child)
    post_order(root.right_child)
    print(root.data, end=' ')

def in_order(root):
    if root is None:
        return
    in_order(root.left_child)
    print(root.data, end=' ')
    in_order(root.right_child)

def height_of_tree(root):
    if root is None:
        return -1
    left_height = 1 + height_of_tree(root.left_child)
    right_height = 1 + height_of_tree(root.right_child)
    return max(left_height, right_height)

def top_view(root):
    if hasattr(top_view, 'counter') is False:
        top_view.counter = 0
    if root.left_child and top_view.counter >= 0:
        top_view.counter += 1
        top_view(root.left_child)
    top_view.counter -= 1
    print(root.data, end=' ')

    if root.right_child and top_view.counter < 0:
        top_view.counter -= 1
        top_view(root.right_child)

def topView(root, order = 0):
    if root is None:
        return
    if order <= 0:
        topView(root.left_child, -1)
    print(root.data, end=' ')
    if order >= 0:
        topView(root.right_child, 1)

#TODO: Breadth-first search (BFS) is an algorithm
def level_order(root):
    if root is None:
        return
    queue = deque()
    queue.append(root)
    while len(queue) != 0:
        current = queue.popleft()
        print(current.data, end=' ')
        if current.left_child:
            queue.append(current.left_child)
        if current.right_child:
            queue.append(current.right_child)


def main():
    first_root = Node(9)
    # insert(first_root, 11)
    # insert(first_root, 7)
    # insert(first_root, 14)
    # insert(first_root, 12)
    # insert(first_root, 13)
    # insert(first_root, 15)
    insert(first_root, 8)
    insert(first_root, 6)
    insert(first_root, 7)
    insert(first_root, 3)
    insert(first_root, 1)
    print('post order')
    post_order(first_root)
    print()
    print('pre order')
    pre_order(first_root)
    print()
    print('in order')
    in_order(first_root)
    print()
    print('height of tree: ', height_of_tree(first_root))
    print()
    print('top view')
    top_view(first_root)
    print()
    print('topView ')
    topView(first_root)
    print()
    print('level order')
    level_order(first_root)

if __name__ == '__main__':
    main()
