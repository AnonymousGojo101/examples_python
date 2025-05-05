"""
Leetcode Problem: Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

A well-formed parentheses combination has all opening and closing brackets correctly matched.

Constraints:
- 1 <= n <= 8

Examples:

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
"""

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # TODO: Implement this method
        pass


def main():
    sol = Solution()
    
    # Test case 1
    n1 = 1
    expected1 = ["()"]
    result1 = sol.generateParenthesis(n1)
    print("Test case 1: n =", n1)
    print("Output:", result1)
    assert set(result1) == set(expected1), f"Failed test case 1: expected {expected1}, got {result1}"
    print("Passed ✅\n")

    # Test case 2
    n2 = 2
    expected2 = ["(())", "()()"]
    result2 = sol.generateParenthesis(n2)
    print("Test case 2: n =", n2)
    print("Output:", result2)
    assert set(result2) == set(expected2), f"Failed test case 2: expected {expected2}, got {result2}"
    print("Passed ✅\n")

    # Test case 3
    n3 = 3
    expected3 = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    result3 = sol.generateParenthesis(n3)
    print("Test case 3: n =", n3)
    print("Output:", result3)
    assert set(result3) == set(expected3), f"Failed test case 3: expected {expected3}, got {result3}"
    print("Passed ✅\n")


if __name__ == "__main__":
    main()
