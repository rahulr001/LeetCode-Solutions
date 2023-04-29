class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def mergeTwoLists(list1, list2):
    n = dummy = ListNode(0)
    while list1 and list2:
        if list1.val < list2.val:
            n.next = list1
            list1 = list1.next
        else:
            n.next = list2
            list2 = list2.next
        n = n.next
    n.next = list1 if list1 else list2
    return dummy.next


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(5)

l2 = ListNode(1)
l2.next = ListNode(7)
l2.next.next = ListNode(9)

print(mergeTwoLists(l1, l2).val)
