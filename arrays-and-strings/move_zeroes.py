"""
Problem 283: Move Zeroes

Given an integer array nums, move all 0's to the end of it 
while maintaining the relative order of the non-zero elements.

Note:
- You must do this in-place without making a copy of the array.

Constraints:
- 1 <= nums.length <= 10^4
- -2^31 <= nums[i] <= 2^31 - 1

Follow-up:
- Could you minimize the total number of operations done?

Examples:

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
"""

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # TODO: Implement this method
        # Do not return anything, modify nums in-place instead.
        pass


def main():
    sol = Solution()

    # Test case 1
    nums1 = [0, 1, 0, 3, 12]
    expected1 = [1, 3, 12, 0, 0]
    sol.moveZeroes(nums1)
    print("Test case 1:")
    print("Output:", nums1)
    assert nums1 == expected1, f"Failed test case 1: expected {expected1}, got {nums1}"
    print("Passed ✅\n")

    # Test case 2
    nums2 = [0]
    expected2 = [0]
    sol.moveZeroes(nums2)
    print("Test case 2:")
    print("Output:", nums2)
    assert nums2 == expected2, f"Failed test case 2: expected {expected2}, got {nums2}"
    print("Passed ✅\n")

    # Test case 3
    nums3 = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
    expected3 = [4, 2, 4, 3, 5, 1, 0, 0, 0, 0]
    sol.moveZeroes(nums3)
    print("Test case 3:")
    print("Output:", nums3)
    assert nums3 == expected3, f"Failed test case 3: expected {expected3}, got {nums3}"
    print("Passed ✅\n")


if __name__ == "__main__":
    main()
