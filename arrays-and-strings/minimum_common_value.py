"""
Problem 2540: Minimum Common Value

Given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
return the minimum integer common to both arrays. 
If there is no common integer, return -1.

An integer is said to be common if it appears in both arrays.

Constraints:
- 1 <= nums1.length, nums2.length <= 10^5
- 1 <= nums1[i], nums2[j] <= 10^9
- Both arrays are sorted in non-decreasing order

Examples:

Example 1:
Input: nums1 = [1, 2, 3], nums2 = [2, 4]
Output: 2

Example 2:
Input: nums1 = [1, 2, 3, 6], nums2 = [2, 3, 4, 5]
Output: 2
"""

from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # TODO: Implement this method
        pass


def main():
    sol = Solution()
    
    # Test case 1
    nums1_1 = [1, 2, 3]
    nums2_1 = [2, 4]
    expected1 = 2
    result1 = sol.getCommon(nums1_1, nums2_1)
    print("Test case 1:")
    print("Input:", nums1_1, nums2_1)
    print("Output:", result1)
    assert result1 == expected1, f"Failed test case 1: expected {expected1}, got {result1}"
    print("Passed ✅\n")

    # Test case 2
    nums1_2 = [1, 2, 3, 6]
    nums2_2 = [2, 3, 4, 5]
    expected2 = 2
    result2 = sol.getCommon(nums1_2, nums2_2)
    print("Test case 2:")
    print("Input:", nums1_2, nums2_2)
    print("Output:", result2)
    assert result2 == expected2, f"Failed test case 2: expected {expected2}, got {result2}"
    print("Passed ✅\n")

    # Test case 3
    nums1_3 = [1, 5, 9]
    nums2_3 = [2, 3, 4]
    expected3 = -1
    result3 = sol.getCommon(nums1_3, nums2_3)
    print("Test case 3:")
    print("Input:", nums1_3, nums2_3)
    print("Output:", result3)
    assert result3 == expected3, f"Failed test case 3: expected {expected3}, got {result3}"
    print("Passed ✅\n")


if __name__ == "__main__":
    main()
