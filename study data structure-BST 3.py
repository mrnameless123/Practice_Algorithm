from collections import deque


class Node():
    def __init__(self, index, left=None, right=None):
        self.index = index
        self.left = left
        self.right = right


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


def in_order(root):
    if root is None:
        return
    in_order(root.left)
    print(root.index, end=' ')
    in_order(root.right)

def get_all_nodes_at_lvl(root, current_lvl, request_level, results):
    if current_lvl == request_level:
        results.append(root)
    else:
        if root.left is not None:
            get_all_nodes_at_lvl(root.left, current_lvl + 1,request_level, results)
        if root.right is not None:
            get_all_nodes_at_lvl(root.right, current_lvl + 1, request_level, results)


def swap_node_below_height(root, height):
    return root


def main():
    N = int(input().strip())
    root_node = Node(1)
    for x in range(1, N + 1):
        left, right = list(map(int, input().strip().split(' ')))
        insert_node(root_node, x, left, right)
    in_order(root_node)
    print('All nodes at lvl 4')
    node_at_lvl2 = deque()
    get_all_nodes_at_lvl(root_node, 1, 5, node_at_lvl2)
    while len(node_at_lvl2) != 0:
        tmp = node_at_lvl2.popleft()
        print(tmp.index, end=' ')


if __name__ == '__main__':
    main()