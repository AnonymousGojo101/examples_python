"""
Problem: Find Lucky Integer in an Array

Given an array of integers `arr`, a lucky integer is an integer that has a frequency in the array 
equal to its value.

Return the largest lucky integer in the array. If there is no lucky integer, return -1.

Constraints:
- 1 <= arr.length <= 500
- 1 <= arr[i] <= 500

Examples:

Example 1:
Input: arr = [2, 2, 3, 4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.

Example 2:
Input: arr = [1, 2, 2, 3, 3, 3]
Output: 3
Explanation: 1, 2, and 3 are all lucky numbers, return the largest of them.

Example 3:
Input: arr = [2, 2, 2, 3, 3]
Output: -1
Explanation: There are no lucky numbers in the array.
"""

from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        # TODO: Implement this method
        pass


def main():
    sol = Solution()
    
    # Test case 1
    arr1 = [2, 2, 3, 4]
    expected1 = 2
    result1 = sol.findLucky(arr1)
    print("Test case 1: arr =", arr1)
    print("Output:", result1)
    assert result1 == expected1, f"Failed test case 1: expected {expected1}, got {result1}"
    print("Passed ✅\n")

    # Test case 2
    arr2 = [1, 2, 2, 3, 3, 3]
    expected2 = 3
    result2 = sol.findLucky(arr2)
    print("Test case 2: arr =", arr2)
    print("Output:", result2)
    assert result2 == expected2, f"Failed test case 2: expected {expected2}, got {result2}"
    print("Passed ✅\n")

    # Test case 3
    arr3 = [2, 2, 2, 3, 3]
    expected3 = -1
    result3 = sol.findLucky(arr3)
    print("Test case 3: arr =", arr3)
    print("Output:", result3)
    assert result3 == expected3, f"Failed test case 3: expected {expected3}, got {result3}"
    print("Passed ✅\n")


if __name__ == "__main__":
    main()
