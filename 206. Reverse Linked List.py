class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def add(self, val):
        if self.next is None:
            self.next = ListNode(val)
        else:
            self.next.add(val)

    def print_list(self):
        print(self.val)
        if self.next is not None:
            self.next.print_list()


class Solution:
    def reverseList(self, head):
        new_list = None
        curr = head
        
        while curr:
            next_node = curr.next
            curr.next = new_list
            new_list = curr
            curr = next_node
            
        return new_list
            
                


lis = ListNode(1)
lis.add(2)
lis.add(3)
lis.add(4)
lis.add(5)
# lis.print_list()

print(Solution().reverseList(lis))
lis.print_list()