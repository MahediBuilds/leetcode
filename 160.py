class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(self, headA, headB):
        l1 = headA
        l2 = headB

        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1


# Create common part
common = ListNode(8)
common.next = ListNode(9)


# Create List A
headA = ListNode(4)
headA.next = ListNode(1)
headA.next.next = common


# Create List B
headB = ListNode(5)
headB.next = ListNode(6)
headB.next.next = ListNode(1)
headB.next.next.next = common


solution = Solution()
result = solution.getIntersectionNode(headA, headB)


# Print intersection node
if result:
    print("Intersection:", result.val)
else:
    print("No intersection")
