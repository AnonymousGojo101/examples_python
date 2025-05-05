"""
Problem: Count Elements With Maximum Frequency

You are given an integer array `nums`. Return the total frequencies of elements in `nums` 
such that those elements all have the maximum frequency.

The frequency of an element is the number of occurrences of that element in the array.

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100

Examples:

Example 1:
Input: nums = [1, 2, 2, 3, 1, 4]
Output: 4
Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
So the number of elements in the array with maximum frequency is 4.

Example 2:
Input: nums = [1, 2, 3, 4, 5]
Output: 5
Explanation: All elements of the array have a frequency of 1 which is the maximum.
So the number of elements in the array with maximum frequency is 5.
"""

from typing import List

class Solution:
    def countElements(self, nums: List[int]) -> int:
        # TODO: Implement this method
        pass


def main():
    sol = Solution()
    
    # Test case 1
    nums1 = [1, 2, 2, 3, 1, 4]
    expected1 = 4
    result1 = sol.countElements(nums1)
    print("Test case 1: nums =", nums1)
    print("Output:", result1)
    assert result1 == expected1, f"Failed test case 1: expected {expected1}, got {result1}"
    print("Passed ✅\n")

    # Test case 2
    nums2 = [1, 2, 3, 4, 5]
    expected2 = 5
    result2 = sol.countElements(nums2)
    print("Test case 2: nums =", nums2)
    print("Output:", result2)
    assert result2 == expected2, f"Failed test case 2: expected {expected2}, got {result2}"
    print("Passed ✅\n")

    # Test case 3
    nums3 = [5, 5, 5, 5]
    expected3 = 4
    result3 = sol.countElements(nums3)
    print("Test case 3: nums =", nums3)
    print("Output:", result3)
    assert result3 == expected3, f"Failed test case 3: expected {expected3}, got {result3}"
    print("Passed ✅\n")


if __name__ == "__main__":
    main()
