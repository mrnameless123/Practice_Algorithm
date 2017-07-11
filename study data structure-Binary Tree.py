import sys

class Node:
    def __init__(self, *args, **kwargs):
        data = args
        left_child = kwargs.get('left_child', None)
        right_child = kwargs.get('right_child', None)

    @staticmethod
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
    @staticmethod
    def insert(root,data):
        '''
        :param root: pointer to the root of the BST
        :param data: data of the new node
        :return: pointer to the root of new BST
        '''
        new_node = Node(data, left_child=None, right_child=None)
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
        
