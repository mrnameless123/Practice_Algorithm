import sys

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next_node
    def set_next(self, new_next):
        self.next_node = new_next

class Linked_List(object):
    def __init__(self, head = None):
        self.head = head

    def insert(self, data, index = None):
        new_node = Node(data)
        if index is None:
            new_node.set_next(self.head)
            self.head = new_node
        else:
            current_index = 0
            current = self.head
            previous_next_node = None
            while current_index <= index and current:
                if current_index == index:
                    previous_next_node.set_next(new_node)
                    new_node.set_next(current)
                    break
                else:
                    previous_next_node = current
                    current = current.get_next()
                    current_index += 1
            if current is None:
                raise ValueError('Index not in list')

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def print_list(self):
        current = self.head
        index = 1
        while current is not None:
            print('value at index ', index, ' is ', current.get_data())
            index +=1
            current = current.get_next()

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError('Data not in list')
        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError('Data not in list')
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

def main():
    mylist = Linked_List()
    temp = Node(100)
    print(temp.get_data())
    mylist.insert(100)
    mylist.insert(101)
    mylist.insert(110)
    mylist.insert(201)
    mylist.insert(200)
    mylist.print_list()
    print(mylist.size())
    mylist.insert(204, 3)
    mylist.print_list()
    print(mylist.size())


if __name__ == '__main__':
    main()


