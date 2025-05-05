"""
Problem: 2130. Maximum Twin Sum of a Linked List

In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.

Constraints:
- The number of nodes in the list is an even integer in the range [2, 10^5].
- 1 <= Node.val <= 10^5

Examples:

Example 1:
Input: head = [5,4,2,1]
Output: 6
Explanation: Twin sums are (5+1)=6 and (4+2)=6 → max = 6.

Example 2:
Input: head = [4,2,2,3]
Output: 7
Explanation: Twin sums are (4+3)=7 and (2+2)=4 → max = 7.

Example 3:
Input: head = [1,100000]
Output: 100001
Explanation: Twin sum is (1+100000)=100001.
"""

from typing import Optional, List


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
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
    head1 = list_to_linkedlist([5, 4, 2, 1])
    expected1 = 6
    result1 = sol.pairSum(head1)
    print("Test case 1:")
    print("Output:", result1)
    assert result1 == expected1, f"Failed test case 1: expected {expected1}, got {result1}"
    print("Passed ✅\n")

    # Test case 2
    head2 = list_to_linkedlist([4, 2, 2, 3])
    expected2 = 7
    result2 = sol.pairSum(head2)
    print("Test case 2:")
    print("Output:", result2)
    assert result2 == expected2, f"Failed test case 2: expected {expected2}, got {result2}"
    print("Passed ✅\n")

    # Test case 3
    head3 = list_to_linkedlist([1, 100000])
    expected3 = 100001
    result3 = sol.pairSum(head3)
    print("Test case 3:")
    print("Output:", result3)
    assert result3 == expected3, f"Failed test case 3: expected {expected3}, got {result3}"
    print("Passed ✅\n")


if __name__ == "__main__":
    main()
