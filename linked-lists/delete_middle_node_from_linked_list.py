"""
Problem: Delete the Middle Node of a Linked List

You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

Constraints:
- The number of nodes in the list is in the range [1, 10^5]
- 1 <= Node.val <= 10^5

Examples:

Example 1:
Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation: Middle node is value 7 (index 3), remove it.

Example 2:
Input: head = [1,2,3,4]
Output: [1,2,4]
Explanation: Middle node is value 3 (index 2), remove it.

Example 3:
Input: head = [2,1]
Output: [2]
Explanation: Middle node is value 1 (index 1), remove it.
"""

from typing import Optional, List


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # TODO: Implement this method
        pass


def list_to_linkedlist(items: List[int]) -> Optional[ListNode]:
    if not items:
        return None
    dummy = ListNode(0)
    current = dummy
    for item in items:
        current.next = ListNode(item)
        current = current.next
    return dummy.next


def linkedlist_to_list(node: Optional[ListNode]) -> List[int]:
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


def main():
    sol = Solution()

    # Test case 1
    head1 = list_to_linkedlist([1, 3, 4, 7, 1, 2, 6])
    expected1 = [1, 3, 4, 1, 2, 6]
    result1 = linkedlist_to_list(sol.deleteMiddle(head1))
    print("Test case 1: [1, 3, 4, 7, 1, 2, 6]")
    print("Output:", result1)
    assert result1 == expected1, f"Failed test case 1: expected {expected1}, got {result1}"
    print("Passed ✅\n")

    # Test case 2
    head2 = list_to_linkedlist([1, 2, 3, 4])
    expected2 = [1, 2, 4]
    result2 = linkedlist_to_list(sol.deleteMiddle(head2))
    print("Test case 2: [1, 2, 3, 4]")
    print("Output:", result2)
    assert result2 == expected2, f"Failed test case 2: expected {expected2}, got {result2}"
    print("Passed ✅\n")

    # Test case 3
    head3 = list_to_linkedlist([2, 1])
    expected3 = [2]
    result3 = linkedlist_to_list(sol.deleteMiddle(head3))
    print("Test case 3: [2, 1]")
    print("Output:", result3)
    assert result3 == expected3, f"Failed test case 3: expected {expected3}, got {result3}"
    print("Passed ✅\n")


if __name__ == "__main__":
    main()
