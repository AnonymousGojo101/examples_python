"""
Problem: Sort Characters By Frequency

Given a string `s`, sort it in decreasing order based on the frequency of the characters. 
The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

Constraints:
- 1 <= s.length <= 5 * 10^5
- s consists of uppercase and lowercase English letters and digits.

Examples:

Example 1:
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:
Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""

from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        # TODO: Implement this method
        pass


def main():
    sol = Solution()
    
    # Test case 1
    s1 = "tree"
    expected1 = "eert"  # Valid answers could be "eetr" as well
    result1 = sol.frequencySort(s1)
    print("Test case 1: s =", s1)
    print("Output:", result1)
    assert sorted(result1) == sorted(expected1), f"Failed test case 1: expected {expected1}, got {result1}"
    print("Passed ✅\n")

    # Test case 2
    s2 = "cccaaa"
    expected2 = "aaaccc"  # Valid answers could also be "cccaaa"
    result2 = sol.frequencySort(s2)
    print("Test case 2: s =", s2)
    print("Output:", result2)
    assert sorted(result2) == sorted(expected2), f"Failed test case 2: expected {expected2}, got {result2}"
    print("Passed ✅\n")

    # Test case 3
    s3 = "Aabb"
    expected3 = "bbAa"  # Valid answers could also be "bbaA"
    result3 = sol.frequencySort(s3)
    print("Test case 3: s =", s3)
    print("Output:", result3)
    assert sorted(result3) == sorted(expected3), f"Failed test case 3: expected {expected3}, got {result3}"
    print("Passed ✅\n")


if __name__ == "__main__":
    main()
