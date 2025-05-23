"""
Problem: Swapping Nodes in a Linked List

You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning 
and the kth node from the end (the list is 1-indexed).

Constraints:
- The number of nodes in the list is n.
- 1 <= k <= n <= 10^5
- 0 <= Node.val <= 100

Examples:

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

Example 2:
Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
"""

from typing import Optional, List


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # TODO: Implement this method
        pass


def list_to_linkedlist(items: List[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    curr = dummy
    for item in items:
        curr.next = ListNode(item)
        curr = curr.next
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
    k1 = 2
    expected1 = [1, 4, 3, 2, 5]
    result1 = linkedlist_to_list(sol.swapNodes(head1, k1))
    print("Test case 1: head = [1,2,3,4,5], k = 2")
    print("Output:", result1)
    assert result1 == expected1, f"Failed test case 1: expected {expected1}, got {result1}"
    print("Passed ✅\n")

    # Test case 2
    head2 = list_to_linkedlist([7,9,6,6,7,8,3,0,9,5])
    k2 = 5
    expected2 = [7,9,6,6,8,7,3,0,9,5]
    result2 = linkedlist_to_list(sol.swapNodes(head2, k2))
    print("Test case 2: head = [7,9,6,6,7,8,3,0,9,5], k = 5")
    print("Output:", result2)
    assert result2 == expected2, f"Failed test case 2: expected {expected2}, got {result2}"
    print("Passed ✅\n")

    # Test case 3
    head3 = list_to_linkedlist([1, 2])
    k3 = 1
    expected3 = [2, 1]
    result3 = linkedlist_to_list(sol.swapNodes(head3, k3))
    print("Test case 3: head = [1,2], k = 1")
    print("Output:", result3)
    assert result3 == expected3, f"Failed test case 3: expected {expected3}, got {result3}"
    print("Passed ✅\n")


if __name__ == "__main__":
    main()
