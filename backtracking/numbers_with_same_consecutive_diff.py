"""
Leetcode Problem: Numbers With Same Consecutive Differences

Given two integers n and k, return an array of all the integers of length n 
where the absolute difference between every two consecutive digits is k.

Note:
- The integers should not have leading zeros.
- Return the answer in any order.

Constraints:
- 2 <= n <= 9
- 0 <= k <= 9

Examples:

Example 1:
Input: n = 3, k = 7
Output: [181, 292, 707, 818, 929]

Example 2:
Input: n = 2, k = 1
Output: [10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98]
"""

from typing import List

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        # TODO: Implement this method
        pass


def main():
    sol = Solution()
    
    # Test case 1
    n1, k1 = 3, 7
    expected1 = [181, 292, 707, 818, 929]
    result1 = sol.numsSameConsecDiff(n1, k1)
    print("Test case 1: n =", n1, ", k =", k1)
    print("Output:", result1)
    assert set(result1) == set(expected1), f"Failed test case 1: expected {expected1}, got {result1}"
    print("Passed ✅\n")

    # Test case 2
    n2, k2 = 2, 1
    expected2 = [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
    result2 = sol.numsSameConsecDiff(n2, k2)
    print("Test case 2: n =", n2, ", k =", k2)
    print("Output:", result2)
    assert set(result2) == set(expected2), f"Failed test case 2: expected {expected2}, got {result2}"
    print("Passed ✅\n")

    # Test case 3
    n3, k3 = 2, 0
    expected3 = [11, 22, 33, 44, 55, 66, 77, 88, 99]
    result3 = sol.numsSameConsecDiff(n3, k3)
    print("Test case 3: n =", n3, ", k =", k3)
    print("Output:", result3)
    assert set(result3) == set(expected3), f"Failed test case 3: expected {expected3}, got {result3}"
    print("Passed ✅\n")


if __name__ == "__main__":
    main()
