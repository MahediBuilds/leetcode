class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:

            if l1:
                val1 = l1.val
            else:
                val1 = 0

            if l2:
                val2 = l2.val
            else:
                val2 = 0

            val = val1 + val2 + carry
            carry = val // 10
            val = val % 10
            curr.next = ListNode(val)

            l1 = l1.next if l1 else None
            l2 = l2.next if l1 else None
            curr = curr.next

        return dummy.next


# Create first linked list
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

# Create second linked list
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)


solution = Solution()
result = solution.addTwoNumbers(l1, l2)


# Print linked list
while result:
    print(result.val, end="")
    result = result.next
