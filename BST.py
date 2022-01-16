# Guidance from codingbasics
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root


class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_min(self):
        if self is None:
            return
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def find_max(self):
        if self is None:
            return
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def post_order_traversal(self):
        element = []
        if self.left:
            element += self.left.post_order_traversal()
        if self.right:
            element += self.right.post_order_traversal()
        element.append(self.data)
        return element

    def pre_order_traversal(self):
        element = []
        element.append(self.data)
        if self.left:
            element += self.left.pre_order_traversal()
        if self.right:
            element += self.right.pre_order_traversal()
        return element

    def in_order_traversal(self):
        element = []
        if self.left:
            element += self.left.in_order_traversal()
        element.append(self.data)
        if self.right:
            element += self.right.in_order_traversal()
        return element

    def calculate_sum(self):
        su = 0
        for i in self.in_order_traversal():
            su += i
        return su


if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    print("Input numbers:", numbers)
    print("Min:", numbers_tree.find_min())
    print("Max:", numbers_tree.find_max())
    print("Sum:", numbers_tree.calculate_sum())
    print("In order traversal:", numbers_tree.in_order_traversal())
    print("Pre order traversal:", numbers_tree.pre_order_traversal())
    print("Post order traversal:", numbers_tree.post_order_traversal())
