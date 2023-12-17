#  linked list cycle ------------------------------------------------------------------------------------------------------------------------------------

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def has_cycle(head):
    # base case
    if not head:
        return False

    slow = head
    fast = head


    while slow != None and fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True


# Example usage:
# Create a linked list with a cycle
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = head.next  # Creating a cycle

print(has_cycle(head))  

# Output: True
