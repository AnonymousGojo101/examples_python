"""
Leetcode Problem: Combination Sum III

Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

- Only numbers 1 through 9 are used.
- Each number is used at most once.

Return a list of all possible valid combinations. 
The list must not contain the same combination twice, and the combinations may be returned in any order.

Constraints:
- 2 <= k <= 9
- 1 <= n <= 60

Examples:

Example 1:
Input: k = 3, n = 7
Output: [[1, 2, 4]]

Example 2:
Input: k = 3, n = 9
Output: [[1, 2, 6], [1, 3, 5], [2, 3, 4]]

Example 3:
Input: k = 4, n = 1
Output: []
Explanation: The smallest sum using 4 different numbers is 1+2+3+4 = 10 > 1, so no valid combinations.
"""

from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # TODO: Implement this method
        pass


def main():
    sol = Solution()
    
    # Test case 1
    k1, n1 = 3, 7
    expected1 = [[1, 2, 4]]
    result1 = sol.combinationSum3(k1, n1)
    print("Test case 1: k =", k1, ", n =", n1)
    print("Output:", result1)
    assert set(map(tuple, result1)) == set(map(tuple, expected1)), f"Failed test case 1: expected {expected1}, got {result1}"
    print("Passed ✅\n")

    # Test case 2
    k2, n2 = 3, 9
    expected2 = [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
    result2 = sol.combinationSum3(k2, n2)
    print("Test case 2: k =", k2, ", n =", n2)
    print("Output:", result2)
    assert set(map(tuple, result2)) == set(map(tuple, expected2)), f"Failed test case 2: expected {expected2}, got {result2}"
    print("Passed ✅\n")

    # Test case 3
    k3, n3 = 4, 1
    expected3 = []
    result3 = sol.combinationSum3(k3, n3)
    print("Test case 3: k =", k3, ", n =", n3)
    print("Output:", result3)
    assert result3 == expected3, f"Failed test case 3: expected {expected3}, got {result3}"
    print("Passed ✅\n")


if __name__ == "__main__":
    main()
