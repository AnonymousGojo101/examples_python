"""
Problem: Palindrome Linked List

Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Constraints:
- The number of nodes in the list is in the range [1, 10^5].
- 0 <= Node.val <= 9

Examples:

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
"""

from typing import Optional, List


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # TODO: Implement this method
        pass


def list_to_linkedlist(items: List[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    current = dummy
    for item in items:
        current.next = ListNode(item)
        current = current.next
    return dummy.next


def main():
    sol = Solution()

    # Test case 1
    head1 = list_to_linkedlist([1, 2, 2, 1])
    expected1 = True
    result1 = sol.isPalindrome(head1)
    print("Test case 1: head = [1,2,2,1]")
    print("Output:", result1)
    assert result1 == expected1, f"Failed test case 1: expected {expected1}, got {result1}"
    print("Passed ✅\n")

    # Test case 2
    head2 = list_to_linkedlist([1, 2])
    expected2 = False
    result2 = sol.isPalindrome(head2)
    print("Test case 2: head = [1,2]")
    print("Output:", result2)
    assert result2 == expected2, f"Failed test case 2: expected {expected2}, got {result2}"
    print("Passed ✅\n")

    # Test case 3
    head3 = list_to_linkedlist([1, 2, 3, 2, 1])
    expected3 = True
    result3 = sol.isPalindrome(head3)
    print("Test case 3: head = [1,2,3,2,1]")
    print("Output:", result3)
    assert result3 == expected3, f"Failed test case 3: expected {expected3}, got {result3}"
    print("Passed ✅\n")


if __name__ == "__main__":
    main()
