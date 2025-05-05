"""
Problem: Maximum Erasure Value

You are given an array of positive integers `nums` and want to erase a subarray containing unique elements. 
The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l], a[l+1], ..., a[r] for some (l, r).

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^4

Examples:

Example 1:
Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2, 4, 5, 6], which has a sum of 17.

Example 2:
Input: nums = [5,2,1,2,5,2,1,2,5]
Output: 8
Explanation: The optimal subarray here is [5, 2, 1] or [1, 2, 5], both with a sum of 8.
"""

class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        # TODO: Implement this method
        pass


def main():
    sol = Solution()

    # Test case 1
    nums1 = [4, 2, 4, 5, 6]
    expected1 = 17
    result1 = sol.maximumUniqueSubarray(nums1)
    print("Test case 1: nums =", nums1)
    print("Output:", result1)
    assert result1 == expected1, f"Failed test case 1: expected {expected1}, got {result1}"
    print("Passed ✅\n")

    # Test case 2
    nums2 = [5, 2, 1, 2, 5, 2, 1, 2, 5]
    expected2 = 8
    result2 = sol.maximumUniqueSubarray(nums2)
    print("Test case 2: nums =", nums2)
    print("Output:", result2)
    assert result2 == expected2, f"Failed test case 2: expected {expected2}, got {result2}"
    print("Passed ✅\n")


if __name__ == "__main__":
    main()
