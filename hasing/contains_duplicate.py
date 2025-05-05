"""
Problem 217: Contains Duplicate

Given an integer array nums, return True if any value appears at least twice in the array,
and return False if every element is distinct.

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

Examples:

Example 1:
Input: nums = [1, 2, 3, 1]
Output: True
Explanation: The element 1 appears more than once.

Example 2:
Input: nums = [1, 2, 3, 4]
Output: False
Explanation: All elements are distinct.

Example 3:
Input: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
Output: True
"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # TODO: Implement this method
        pass


def main():
    sol = Solution()

    # Test case 1
    nums1 = [1, 2, 3, 1]
    expected1 = True
    result1 = sol.containsDuplicate(nums1)
    print("Test case 1:", result1)
    assert result1 == expected1, f"Failed: expected {expected1}, got {result1}"
    print("Passed ✅\n")

    # Test case 2
    nums2 = [1, 2, 3, 4]
    expected2 = False
    result2 = sol.containsDuplicate(nums2)
    print("Test case 2:", result2)
    assert result2 == expected2, f"Failed: expected {expected2}, got {result2}"
    print("Passed ✅\n")

    # Test case 3
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    expected3 = True
    result3 = sol.containsDuplicate(nums3)
    print("Test case 3:", result3)
    assert result3 == expected3, f"Failed: expected {expected3}, got {result3}"
    print("Passed ✅\n")


if __name__ == "__main__":
    main()
