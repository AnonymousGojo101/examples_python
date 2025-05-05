"""
Problem 724: Find Pivot Index

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left 
of the index is equal to the sum of all the numbers strictly to the right.

Return the leftmost pivot index. If no such index exists, return -1.

Constraints:
- 1 <= nums.length <= 10^4
- -1000 <= nums[i] <= 1000

Examples:

Example 1:
Input: nums = [1, 7, 3, 6, 5, 6]
Output: 3
Explanation: Left sum = 1 + 7 + 3 = 11, Right sum = 5 + 6 = 11

Example 2:
Input: nums = [1, 2, 3]
Output: -1

Example 3:
Input: nums = [2, 1, -1]
Output: 0
Explanation: Left sum = 0, Right sum = 1 + -1 = 0
"""

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # TODO: Implement this method
        pass


def main():
    sol = Solution()

    # Test case 1
    nums1 = [1, 7, 3, 6, 5, 6]
    expected1 = 3
    result1 = sol.pivotIndex(nums1)
    print("Test case 1:")
    print("Output:", result1)
    assert result1 == expected1, f"Failed test case 1: expected {expected1}, got {result1}"
    print("Passed ✅\n")

    # Test case 2
    nums2 = [1, 2, 3]
    expected2 = -1
    result2 = sol.pivotIndex(nums2)
    print("Test case 2:")
    print("Output:", result2)
    assert result2 == expected2, f"Failed test case 2: expected {expected2}, got {result2}"
    print("Passed ✅\n")

    # Test case 3
    nums3 = [2, 1, -1]
    expected3 = 0
    result3 = sol.pivotIndex(nums3)
    print("Test case 3:")
    print("Output:", result3)
    assert result3 == expected3, f"Failed test case 3: expected {expected3}, got {result3}"
    print("Passed ✅\n")


if __name__ == "__main__":
    main()
