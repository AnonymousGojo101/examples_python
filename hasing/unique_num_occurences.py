"""
Problem: Unique Number of Occurrences

Given an array of integers `arr`, return true if the number of occurrences of each value in the 
array is unique or false otherwise.

Constraints:
- 1 <= arr.length <= 1000
- -1000 <= arr[i] <= 1000

Examples:

Example 1:
Input: arr = [1, 2, 2, 1, 1, 3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2, and 3 has 1. No two values have the same number of occurrences.

Example 2:
Input: arr = [1, 2]
Output: false

Example 3:
Input: arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
Output: true
"""

from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # TODO: Implement this method
        pass


def main():
    sol = Solution()
    
    # Test case 1
    arr1 = [1, 2, 2, 1, 1, 3]
    expected1 = True
    result1 = sol.uniqueOccurrences(arr1)
    print("Test case 1: arr =", arr1)
    print("Output:", result1)
    assert result1 == expected1, f"Failed test case 1: expected {expected1}, got {result1}"
    print("Passed ✅\n")

    # Test case 2
    arr2 = [1, 2]
    expected2 = False
    result2 = sol.uniqueOccurrences(arr2)
    print("Test case 2: arr =", arr2)
    print("Output:", result2)
    assert result2 == expected2, f"Failed test case 2: expected {expected2}, got {result2}"
    print("Passed ✅\n")

    # Test case 3
    arr3 = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
    expected3 = True
    result3 = sol.uniqueOccurrences(arr3)
    print("Test case 3: arr =", arr3)
    print("Output:", result3)
    assert result3 == expected3, f"Failed test case 3: expected {expected3}, got {result3}"
    print("Passed ✅\n")


if __name__ == "__main__":
    main()
