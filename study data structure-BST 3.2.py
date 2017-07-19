from collections import deque
import sys

sys.setrecursionlimit(10 ** 6)
class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def in_order(root):
    if root is None:
        return
    in_order(root.left)
    print(root.data, end=' ')
    in_order(root.right)

def swap_node(root, level):
    if root is None:
        return
    if level == 0:
        tmp = root.left
        root.left = root.right
        root.right = tmp
    else:
        swap_node(root.left, level-1)
        swap_node(root.right, level-1)

def main():
    N = int(input().strip())
    list_nodes = []
    for x in range(1,N+1):
        list_nodes.append(Node(x))
    for x in range(0,N):
        a, b = list(map(int, input().strip().split()))
        if a == -1:
            list_nodes[x].left = None
        else:
            list_nodes[x].left = list_nodes[a-1]
        if b == -1:
            list_nodes[x].right = None
        else:
            list_nodes[x].right = list_nodes[b-1]
    root = list_nodes[0]
    T = int(input().strip())
    while T > 0:
        k = int(input().strip())
        i = k
        while i < N:
            swap_node(root, i-1)
            i+=k
        in_order(root)
        print()
        T -= 1

if __name__ == '__main__':
    main()