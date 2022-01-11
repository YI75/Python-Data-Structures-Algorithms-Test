from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


if __name__ == '__main__':
    string = "Talking Heads"
    stack = Stack()
    for letter in string:
        stack.push(letter)
    print(stack.container)
    ret = ""
    while stack.size() != 0:
        ret += stack.pop()
    print(ret)