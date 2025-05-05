"""
Problem 1732: Find the Highest Altitude

There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. 
The biker starts at point 0 with altitude = 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude 
between points i and i + 1.

Return the highest altitude of any point during the trip.

Constraints:
- n == gain.length
- 1 <= n <= 100
- -100 <= gain[i] <= 100

Examples:

Example 1:
Input: gain = [-5, 1, 5, 0, -7]
Output: 1
Explanation: The altitudes are [0, -5, -4, 1, 1, -6]. Highest is 1.

Example 2:
Input: gain = [-4, -3, -2, -1, 4, 3, 2]
Output: 0
Explanation: Altitudes are [0, -4, -7, -9, -10, -6, -3, -1]. Highest is 0.
"""

from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # TODO: Implement this method
        pass


def main():
    sol = Solution()

    # Test case 1
    gain1 = [-5, 1, 5, 0, -7]
    expected1 = 1
    result1 = sol.largestAltitude(gain1)
    print("Test case 1:")
    print("Output:", result1)
    assert result1 == expected1, f"Failed test case 1: expected {expected1}, got {result1}"
    print("Passed ✅\n")

    # Test case 2
    gain2 = [-4, -3, -2, -1, 4, 3, 2]
    expected2 = 0
    result2 = sol.largestAltitude(gain2)
    print("Test case 2:")
    print("Output:", result2)
    assert result2 == expected2, f"Failed test case 2: expected {expected2}, got {result2}"
    print("Passed ✅\n")

    # Test case 3
    gain3 = [1, 2, 3, -2, 4]
    expected3 = 8
    result3 = sol.largestAltitude(gain3)
    print("Test case 3:")
    print("Output:", result3)
    assert result3 == expected3, f"Failed test case 3: expected {expected3}, got {result3}"
    print("Passed ✅\n")


if __name__ == "__main__":
    main()
