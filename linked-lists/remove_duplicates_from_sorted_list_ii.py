"""
Problem: Remove Duplicates from Sorted List II

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list. Return the linked list sorted as well.

Constraints:
- The number of nodes in the list is in the range [0, 300].
- -100 <= Node.val <= 100
- The list is guaranteed to be sorted in ascending order.

Examples:

Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]
"""

from typing import Optional, List


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
    head1 = list_to_linkedlist([1, 2, 3, 3, 4, 4, 5])
    expected1 = [1, 2, 5]
    result1 = linkedlist_to_list(sol.deleteDuplicates(head1))
    print("Test case 1: head = [1,2,3,3,4,4,5]")
    print("Output:", result1)
    assert result1 == expected1, f"Failed test case 1: expected {expected1}, got {result1}"
    print("Passed ✅\n")

    # Test case 2
    head2 = list_to_linkedlist([1, 1, 1, 2, 3])
    expected2 = [2, 3]
    result2 = linkedlist_to_list(sol.deleteDuplicates(head2))
    print("Test case 2: head = [1,1,1,2,3]")
    print("Output:", result2)
    assert result2 == expected2, f"Failed test case 2: expected {expected2}, got {result2}"
    print("Passed ✅\n")

    # Test case 3
    head3 = list_to_linkedlist([1, 1, 2, 3, 3])
    expected3 = [2]
    result3 = linkedlist_to_list(sol.deleteDuplicates(head3))
    print("Test case 3: head = [1,1,2,3,3]")
    print("Output:", result3)
    assert result3 == expected3, f"Failed test case 3: expected {expected3}, got {result3}"
    print("Passed ✅\n")


if __name__ == "__main__":
    main()
