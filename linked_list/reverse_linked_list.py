## reverse a linked list ----------------------------------------------------------------------------------------------------------------------

class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head

        while curr is not None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # At the end of the loop, 'prev' will be pointing to the new head of the reversed list
        return prev

# Example usage:
# Create a linked list
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

# Print the original linked list
print("Original Linked List:")
current = head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")

# Reverse the linked list
solution = Solution()
reversed_head = solution.reverseList(head)

# Print the reversed linked list
print("\nReversed Linked List:")
current = reversed_head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")

## Ans -> Reversed Linked List:
## 4 -> 3 -> 2 -> 1 -> None







