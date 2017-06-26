import sys

class Node(object):
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next
    def get_value(self):
        return self.value
    def set_next(self, next_node):
        self.next = next_node
    def get_next(self):
        return self.next

class Linked_List_2(object):
    def __init__(self, head = None):
        self.head = head
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(new_node)

    def insert(self, new_node, prev_node_index):
        current = self.head
        index = 0
        while current.get_next():
            current = current.get_next()
            index += 1
            if index == prev_node_index:
                break
        if current.get_next() is not None:
            next_node = current.get_next()
            current.set_next(new_node)
            new_node.set_next(next_node)
        else:
            raise ValueError('No such the index')

    def delete_node(self, delete_index):
        current = self.head
        index = 0
        while current.get_next() is not None:
            index += 1
            if index == delete_index:
                break
            current = current.get_next()
        if current.get_next() is not None:
            delete_node = current.get_next()
            current.set_next(delete_node.get_next())
        else:
            raise ValueError('No such the index')

    def print(self):
        current = self.head
        while current:
            print(current.get_value())
            current = current.get_next()

def reversed_linked_list(head):
    if head is None or head.get_next() is None:
        return head
    new_head = reversed_linked_list(head.get_next())
    head.next.next=head
    head.set_next(None)
    return new_head
def main():
    mylinkedlist = Linked_List_2()
    mylinkedlist.append(Node(10))
    mylinkedlist.append(Node(11))
    mylinkedlist.append(Node(12))
    mylinkedlist.append(Node(13))
    mylinkedlist.append(Node(15))
    mylinkedlist.print()
    print('==============')
    mylinkedlist.insert(Node(14),3)
    mylinkedlist.print()
    mylinkedlist.delete_node(2)
    print('=================')
    mylinkedlist.print()
    print('===================Reversed')
    mylinkedlist.head = reversed_linked_list(mylinkedlist.head)
    mylinkedlist.print()
if __name__ == '__main__':
    main()

