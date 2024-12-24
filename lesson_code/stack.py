class Stack():
    def __init__(self, *args):
        self.stack = [arg for arg in args]

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) < 1:
            return ("No element in the Stack")
        else:
            return self.stack.pop()

    def peek(self):
        if len(self.stack) < 1:
            return ("No element in the Stack")
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)


if __name__ == "__main__":
    x = Stack(*range(10))
    print(x.peek(), ", After peek: ", x)
    print(x.pop(), ", After pop: ", x)
    print(x.push(11), ",After push: ", x)
    print(x.size())
