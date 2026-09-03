class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def deleteNode(self, node):

        node.val = node.next.val
        node.next = node.next.next


head = ListNode(4)
head.next = ListNode(5)
head.next.next = ListNode(1)
head.next.next.next = ListNode(9)

node = head.next

solution = Solution()
solution.deleteNode(node)

while head:
    print(head.val, end=" ")
    head = head.next
