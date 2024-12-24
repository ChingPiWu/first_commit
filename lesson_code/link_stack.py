class StackNode():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedStack():
    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        current = StackNode(data, next=self.top)
        self.top = current

    def peek(self):
        if self.top is None:
            return None
        else:
            return self.top.data

    def pop(self):
        if self.top is None:
            return None
        else:
            pop_item = self.top
            self.top = pop_item.next
            return pop_item.data

    def size(self):
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next
        return count

    def __str__(self):
        current = self.top
        s = ""
        while current:
            s = s + " "+str(current.data)
            current = current.next
        return s


if __name__ == "__main__":
    y = LinkedStack()
    y.push(1)
    print("After push: ", y)
    y.push(2)
    print("After push: ", y)
    y.push(3)
    print("After push: ", y)

    print("After peek: ", y.peek())

    print("After pop: ", y.pop(), y)
    print("After pop: ", y.pop(), y)
    print("size = ", y.size())
