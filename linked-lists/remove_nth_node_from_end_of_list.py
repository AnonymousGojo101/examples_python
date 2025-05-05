"""
Problem: Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Constraints:
- The number of nodes in the list is sz.
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz

Examples:

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Explanation: Node with value 4 (2nd from end) is removed.

Example 2:
Input: head = [1], n = 1
Output: []
Explanation: Only one node, it's removed.

Example 3:
Input: head = [1,2], n = 1
Output: [1]
Explanation: Removes the last node.
"""

from typing import Optional, List


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
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
    head1 = list_to_linkedlist([1, 2, 3, 4, 5])
    n1 = 2
    expected1 = [1, 2, 3, 5]
    result1 = linkedlist_to_list(sol.removeNthFromEnd(head1, n1))
    print("Test case 1: head = [1,2,3,4,5], n = 2")
    print("Output:", result1)
    assert result1 == expected1, f"Failed test case 1: expected {expected1}, got {result1}"
    print("Passed ✅\n")

    # Test case 2
    head2 = list_to_linkedlist([1])
    n2 = 1
    expected2 = []
    result2 = linkedlist_to_list(sol.removeNthFromEnd(head2, n2))
    print("Test case 2: head = [1], n = 1")
    print("Output:", result2)
    assert result2 == expected2, f"Failed test case 2: expected {expected2}, got {result2}"
    print("Passed ✅\n")

    # Test case 3
    head3 = list_to_linkedlist([1, 2])
    n3 = 1
    expected3 = [1]
    result3 = linkedlist_to_list(sol.removeNthFromEnd(head3, n3))
    print("Test case 3: head = [1,2], n = 1")
    print("Output:", result3)
    assert result3 == expected3, f"Failed test case 3: expected {expected3}, got {result3}"
    print("Passed ✅\n")


if __name__ == "__main__":
    main()
