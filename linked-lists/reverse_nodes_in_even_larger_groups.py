"""
Problem: 2074. Reverse Nodes in Even Length Groups

You are given the head of a linked list.

The nodes in the linked list are sequentially assigned to non-empty groups whose lengths form the sequence of the natural numbers (1, 2, 3, 4, ...). 
The length of a group is the number of nodes assigned to it.

Reverse the nodes in each group with an even length, and return the head of the modified linked list.

Constraints:
- The number of nodes in the list is in the range [1, 10^5].
- 0 <= Node.val <= 10^5

Examples:

Example 1:
Input: head = [5,2,6,3,9,1,7,3,8,4]
Output: [5,6,2,3,9,1,4,8,3,7]

Example 2:
Input: head = [1,1,0,6]
Output: [1,0,1,6]

Example 3:
Input: head = [1,1,0,6,5]
Output: [1,0,1,5,6]
"""

from typing import Optional, List


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"


class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
    head1 = list_to_linkedlist([5, 2, 6, 3, 9, 1, 7, 3, 8, 4])
    expected1 = [5, 6, 2, 3, 9, 1, 4, 8, 3, 7]
    result1 = linkedlist_to_list(sol.reverseEvenLengthGroups(head1))
    print("Test case 1:")
    print("Output:", result1)
    assert result1 == expected1, f"Failed test case 1: expected {expected1}, got {result1}"
    print("Passed ✅\n")

    # Test case 2
    head2 = list_to_linkedlist([1, 1, 0, 6])
    expected2 = [1, 0, 1, 6]
    result2 = linkedlist_to_list(sol.reverseEvenLengthGroups(head2))
    print("Test case 2:")
    print("Output:", result2)
    assert result2 == expected2, f"Failed test case 2: expected {expected2}, got {result2}"
    print("Passed ✅\n")

    # Test case 3
    head3 = list_to_linkedlist([1, 1, 0, 6, 5])
    expected3 = [1, 0, 1, 5, 6]
    result3 = linkedlist_to_list(sol.reverseEvenLengthGroups(head3))
    print("Test case 3:")
    print("Output:", result3)
    assert result3 == expected3, f"Failed test case 3: expected {expected3}, got {result3}"
    print("Passed ✅\n")


if __name__ == "__main__":
    main()
