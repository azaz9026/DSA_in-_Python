##  Palindrome Linked List --------------------------------------------------------------------------------------------------------------------------------------


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def is_palindrome(head):
    values = []

    # Step 1: Traverse the linked list and store values in an array
    current = head
    while current:
        values.append(current.value)
        current = current.next

    # Step 2: Check whether the array is a palindrome
    return values == values[::-1]

# Example usage:
# Create a palindrome linked list
palindrome_list = ListNode(1)
palindrome_list.next = ListNode(2)
palindrome_list.next.next = ListNode(3)
palindrome_list.next.next.next = ListNode(2)
palindrome_list.next.next.next.next = ListNode(1)

# Check if the linked list is a palindrome
print(is_palindrome(palindrome_list)) 

 # Output: True
