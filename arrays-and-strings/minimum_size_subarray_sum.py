"""
Leetcode Problem 209: Minimum Size Subarray Sum

Given an array of positive integers nums and a positive integer target, 
return the minimal length of a subarray whose sum is greater than or equal to target. 
If there is no such subarray, return 0 instead.

Constraints:
- 1 <= target <= 10^9
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^4

Follow up:
- Try a solution with O(n) time complexity.
- Then, try a solution with O(n log n) time complexity.

Examples:

Example 1:
Input: target = 7, nums = [2, 3, 1, 2, 4, 3]
Output: 2
Explanation: The subarray [4, 3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1, 4, 4]
Output: 1

Example 3:
Input: target = 11, nums = [1, 1, 1, 1, 1, 1, 1, 1]
Output: 0
"""

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # TODO: Implement this method
        pass


def main():
    sol = Solution()

    # Test case 1
    target1 = 7
    nums1 = [2, 3, 1, 2, 4, 3]
    expected1 = 2
    result1 = sol.minSubArrayLen(target1, nums1)
    print("Test case 1:")
    print("Output:", result1)
    assert result1 == expected1, f"Failed test case 1: expected {expected1}, got {result1}"
    print("Passed ✅\n")

    # Test case 2
    target2 = 4
    nums2 = [1, 4, 4]
    expected2 = 1
    result2 = sol.minSubArrayLen(target2, nums2)
    print("Test case 2:")
    print("Output:", result2)
    assert result2 == expected2, f"Failed test case 2: expected {expected2}, got {result2}"
    print("Passed ✅\n")

    # Test case 3
    target3 = 11
    nums3 = [1, 1, 1, 1, 1, 1, 1, 1]
    expected3 = 0
    result3 = sol.minSubArrayLen(target3, nums3)
    print("Test case 3:")
    print("Output:", result3)
    assert result3 == expected3, f"Failed test case 3: expected {expected3}, got {result3}"
    print("Passed ✅\n")


if __name__ == "__main__":
    main()
