"""
Problem 1748: Sum of Unique Elements

You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.

Examples:

Example 1:
Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.

Example 2:
Input: nums = [1,1,1,1,1]
Output: 0
Explanation: There are no unique elements, and the sum is 0.

Example 3:
Input: nums = [1,2,3,4,5]
Output: 15
Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100
"""

class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        # Dictionary to store the frequency of each element
        freq_map = {}
        
        # Count the frequency of each element in the array
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        
        # Calculate the sum of unique elements (those with frequency 1)
        result = 0
        for num, count in freq_map.items():
            if count == 1:
                result += num
        
        return result


def main():
    sol = Solution()

    # Test case 1
    nums1 = [1, 2, 3, 2]
    expected1 = 4
    result1 = sol.sumOfUnique(nums1)
    print("Test case 1:", result1)
    assert result1 == expected1, f"Failed: expected {expected1}, got {result1}"
    print("Passed ✅\n")

    # Test case 2
    nums2 = [1, 1, 1, 1, 1]
    expected2 = 0
    result2 = sol.sumOfUnique(nums2)
    print("Test case 2:", result2)
    assert result2 == expected2, f"Failed: expected {expected2}, got {result2}"
    print("Passed ✅\n")

    # Test case 3
    nums3 = [1, 2, 3, 4, 5]
    expected3 = 15
    result3 = sol.sumOfUnique(nums3)
    print("Test case 3:", result3)
    assert result3 == expected3, f"Failed: expected {expected3}, got {result3}"
    print("Passed ✅\n")


if __name__ == "__main__":
    main()
