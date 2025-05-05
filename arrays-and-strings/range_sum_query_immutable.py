"""
Problem 303: Range Sum Query - Immutable

Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right (inclusive).

Implement the NumArray class:
- NumArray(int[] nums): Initializes the object with the integer array nums.
- int sumRange(int left, int right): Returns the sum from index left to right (inclusive).

Constraints:
- 1 <= nums.length <= 10^4
- -10^5 <= nums[i] <= 10^5
- 0 <= left <= right < nums.length
- At most 10^4 calls to sumRange

Examples:

Input:
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output:
[null, 1, -1, -3]

Explanation:
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2);  // returns 1
numArray.sumRange(2, 5);  // returns -1
numArray.sumRange(0, 5);  // returns -3
"""

from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        # TODO: Initialize prefix sums for efficient range queries
        pass

    def sumRange(self, left: int, right: int) -> int:
        # TODO: Implement range sum query
        pass


def main():
    # Initialize object
    nums = [-2, 0, 3, -5, 2, -1]
    numArray = NumArray(nums)

    # Test case 1
    result1 = numArray.sumRange(0, 2)
    expected1 = 1
    print("Test case 1:", result1)
    assert result1 == expected1, f"Failed: expected {expected1}, got {result1}"
    print("Passed ✅\n")

    # Test case 2
    result2 = numArray.sumRange(2, 5)
    expected2 = -1
    print("Test case 2:", result2)
    assert result2 == expected2, f"Failed: expected {expected2}, got {result2}"
    print("Passed ✅\n")

    # Test case 3
    result3 = numArray.sumRange(0, 5)
    expected3 = -3
    print("Test case 3:", result3)
    assert result3 == expected3, f"Failed: expected {expected3}, got {result3}"
    print("Passed ✅\n")


if __name__ == "__main__":
    main()
