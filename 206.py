class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):

        curr = head
        prev = None

        while curr:
            tempNext = curr.next
            curr.next = prev
            prev = curr
            curr = tempNext
        return prev


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

solution = Solution()
result = solution.reverseList(head)

while result:
    print(result.val, end=" ")
    result = result.next
