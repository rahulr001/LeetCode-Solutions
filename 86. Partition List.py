class LinkedList:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

def partition(head: LinkedList, x: int) -> LinkedList:
    current = head

    less_val_dummy = LinkedList(0)
    less_val = less_val_dummy

    greater_val_dummy = LinkedList(0)
    greater_val = greater_val_dummy

    while current:
        if current.val < x:
            less_val.next = LinkedList(current.val)
            less_val = less_val.next
        else:
            greater_val.next = LinkedList(current.val)
            greater_val = greater_val.next

        current = current.next

    less_val.next = greater_val_dummy.next

    return less_val_dummy.next
