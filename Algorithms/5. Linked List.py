class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def add(self, val):
        if self.next is None:
            self.next = ListNode(val)
        else:
            self.next.add(val)


lis = ListNode(2)
lis.add(3)
lis.add(5)
lis.add(6)

print(lis.next.next.val)
