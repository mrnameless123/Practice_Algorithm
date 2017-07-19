from collections import deque
import sys

sys.setrecursionlimit(10 ** 6)
class Node():
    def __init__(self, index, left=None, right=None):
        self.index = index
        self.left = left
        self.right = right


def tree_height(root):
    if root is None:
        return 0
    return max(tree_height(root.left), tree_height(root.right)) + 1


def get_all_nodes_at_lvl(root, current_level, requested_level, results):
    if root is None:
        return
    if current_level == requested_level:
        results.append(root)
    else:
        if root.left:
            get_all_nodes_at_lvl(root.left, current_level + 1, requested_level, results)
        if root.right:
            get_all_nodes_at_lvl(root.right, current_level + 1, requested_level, results)


def insert_node(root, target_index, new_left, new_right):
    if root is None:
        return
    queue = deque()
    queue.append(root)
    while len(queue) != 0:
        current = queue.popleft()
        if current.index == target_index:
            if new_left != -1:
                current.left = Node(new_left)
            if new_right != -1:
                current.right = Node(new_right)
            return
        else:
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

def level_order(root):
    if root is None:
        return
    queue = deque()
    current = root
    queue.append(current)
    while len(queue) != 0:
        current = queue.popleft()
        print(current.index, end=' ')
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

def in_order(root):
    if root is None:
        return
    in_order(root.left)
    print(root.index, end=' ')
    in_order(root.right)


def swap_node_below_height(root, height):
    expecting_nodes = deque()
    for x in range(1, tree_height(root)//height + 1):
        get_all_nodes_at_lvl(root, 1, height * x, expecting_nodes)
        while len(expecting_nodes) != 0:
            tmp_node = expecting_nodes.popleft()
            tmp_left = tmp_node.left
            tmp_node.left = tmp_node.right
            tmp_node.right = tmp_left


def main():
    N = int(input().strip())
    root_node = Node(1)
    for x in range(1, N + 1):
        left, right = list(map(int, input().strip().split(' ')))
        insert_node(root_node, x, left, right)
    T = int(input().strip())
    for x in range(1, T + 1):
        k = int(input().strip())
        swap_node_below_height(root_node, k)
        in_order(root_node)
        print()


if __name__ == '__main__':
    main()