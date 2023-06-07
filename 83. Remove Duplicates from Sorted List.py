class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def deleteDuplicates(head):
    temp = head
    while temp and temp.next:
        if temp.next.val == temp.val:
            temp.next = temp.next.next
            continue
        temp = temp.next
    return head


head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(2)

print(deleteDuplicates(head).val)
