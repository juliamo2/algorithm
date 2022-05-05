
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def print_linked_list(head):
    if not head or not head.next:
        return []
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

res = ListNode(1)
res.next = ListNode(2)
res.next.next = ListNode(3)
res.next.next.next = ListNode(4)
res.next.next.next.next = ListNode(5)
m = 2
n = 4

b = ListNode(2)

temp = res
print(print_linked_list(temp))
temp.next = ListNode(b.val)
print(print_linked_list(temp))
res = temp
print(print_linked_list(res))