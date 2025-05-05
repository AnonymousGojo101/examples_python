"""
Problem: Binary Subarrays With Sum

Given a binary array `nums` and an integer `goal`, return the number of non-empty subarrays with a sum equal to the goal.

A subarray is a contiguous part of the array.

Constraints:
- 1 <= nums.length <= 3 * 10^4
- nums[i] is either 0 or 1.
- 0 <= goal <= nums.length

Examples:

Example 1:
Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]

Example 2:
Input: nums = [0,0,0,0,0], goal = 0
Output: 15
Explanation: All possible subarrays have sum 0. Therefore, the total is 15.
"""

class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        # TODO: Implement this method
        pass


def main():
    sol = Solution()
    
    # Test case 1
    nums1 = [1, 0, 1, 0, 1]
    goal1 = 2
    expected1 = 4
    result1 = sol.numSubarraysWithSum(nums1, goal1)
    print("Test case 1: nums =", nums1, ", goal =", goal1)
    print("Output:", result1)
    assert result1 == expected1, f"Failed test case 1: expected {expected1}, got {result1}"
    print("Passed ✅\n")

    # Test case 2
    nums2 = [0, 0, 0, 0, 0]
    goal2 = 0
    expected2 = 15
    result2 = sol.numSubarraysWithSum(nums2, goal2)
    print("Test case 2: nums =", nums2, ", goal =", goal2)
    print("Output:", result2)
    assert result2 == expected2, f"Failed test case 2: expected {expected2}, got {result2}"
    print("Passed ✅\n")


if __name__ == "__main__":
    main()
