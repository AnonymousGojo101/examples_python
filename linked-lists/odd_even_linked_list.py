"""
Problem: 328. Odd Even Linked List

Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices,
and return the reordered list.

The first node is considered odd, and the second node is even.

You must solve the problem in O(1) extra space and O(n) time.

Constraints:
- The number of nodes is in the range [0, 10^4].
- -10^6 <= Node.val <= 10^6

Examples:

Example 1:
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
"""

from typing import Optional, List


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # TODO: Implement this method
        pass


def list_to_linkedlist(items: List[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    current = dummy
    for item in items:
        current.next = ListNode(item)
        current = current.next
    return dummy.next


def linkedlist_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def main():
    sol = Solution()

    # Test case 1
    head1 = list_to_linkedlist([1, 2, 3, 4, 5])
    expected1 = [1, 3, 5, 2, 4]
    result1 = linkedlist_to_list(sol.oddEvenList(head1))
    print("Test case 1:")
    print("Output:", result1)
    assert result1 == expected1, f"Expected {expected1}, but got {result1}"
    print("Passed ✅\n")

    # Test case 2
    head2 = list_to_linkedlist([2, 1, 3, 5, 6, 4, 7])
    expected2 = [2, 3, 6, 7, 1, 5, 4]
    result2 = linkedlist_to_list(sol.oddEvenList(head2))
    print("Test case 2:")
    print("Output:", result2)
    assert result2 == expected2, f"Expected {expected2}, but got {result2}"
    print("Passed ✅\n")

    # Test case 3 (edge)
    head3 = list_to_linkedlist([])
    expected3 = []
    result3 = linkedlist_to_list(sol.oddEvenList(head3))
    print("Test case 3:")
    print("Output:", result3)
    assert result3 == expected3, f"Expected {expected3}, but got {result3}"
    print("Passed ✅\n")


if __name__ == "__main__":
    main()
