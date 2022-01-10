# Guidance from codebasics
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beg(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        itr = self.head
        listr = ''
        while itr:
            listr += str(itr.data) + '->'
            itr = itr.next
        print(listr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_len(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_len():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_len():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_beg(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beg(5)
    ll.insert_at_beg(4)
    ll.print()
    ll.insert_at_end(6)
    ll.print()
    ll.insert_values([i for i in range(1, 11)])
    ll.print()
    print(ll.get_len())
    ll.remove_at(3)
    ll.insert_at(3, 4)
    ll.print()
