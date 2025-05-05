"""
Problem: Number of Good Pairs

Given an array of integers `nums`, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100

Examples:

Example 1:
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Example 2:
Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.

Example 3:
Input: nums = [1,2,3]
Output: 0
Explanation: No pairs have equal values.
"""

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        # TODO: Implement this method
        pass


def main():
    sol = Solution()
    
    # Test case 1
    nums1 = [1, 2, 3, 1, 1, 3]
    expected1 = 4
    result1 = sol.numIdenticalPairs(nums1)
    print("Test case 1: nums =", nums1)
    print("Output:", result1)
    assert result1 == expected1, f"Failed test case 1: expected {expected1}, got {result1}"
    print("Passed ✅\n")

    # Test case 2
    nums2 = [1, 1, 1, 1]
    expected2 = 6
    result2 = sol.numIdenticalPairs(nums2)
    print("Test case 2: nums =", nums2)
    print("Output:", result2)
    assert result2 == expected2, f"Failed test case 2: expected {expected2}, got {result2}"
    print("Passed ✅\n")

    # Test case 3
    nums3 = [1, 2, 3]
    expected3 = 0
    result3 = sol.numIdenticalPairs(nums3)
    print("Test case 3: nums =", nums3)
    print("Output:", result3)
    assert result3 == expected3, f"Failed test case 3: expected {expected3}, got {result3}"
    print("Passed ✅\n")


if __name__ == "__main__":
    main()
