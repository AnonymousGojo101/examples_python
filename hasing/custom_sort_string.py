"""
Problem: Custom Sort String

You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.

Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

Return any permutation of s that satisfies this property.

Constraints:
- 1 <= order.length <= 26
- 1 <= s.length <= 200
- order and s consist of lowercase English letters.
- All the characters of order are unique.

Examples:

Example 1:
Input: order = "cba", s = "abcd"
Output: "cbad"
Explanation: "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a".
Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.

Example 2:
Input: order = "bcafg", s = "abcd"
Output: "bcad"
Explanation: The characters "b", "c", and "a" from order dictate the order for the characters in s. The character "d" in s does not appear in order, so its position is flexible.
Following the order of appearance in order, "b", "c", and "a" from s should be arranged as "b", "c", "a". "d" can be placed at any position since it's not in order. The output "bcad" correctly follows this rule. Other arrangements like "dbca" or "bcda" would also be valid, as long as "b", "c", "a" maintain their order.
"""

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # TODO: Implement this method
        pass


def main():
    sol = Solution()

    # Test case 1
    order1 = "cba"
    s1 = "abcd"
    expected1 = "cbad"
    result1 = sol.customSortString(order1, s1)
    print("Test case 1: order =", order1, ", s =", s1)
    print("Output:", result1)
    assert result1 == expected1, f"Failed test case 1: expected {expected1}, got {result1}"
    print("Passed ✅\n")

    # Test case 2
    order2 = "bcafg"
    s2 = "abcd"
    expected2 = "bcad"
    result2 = sol.customSortString(order2, s2)
    print("Test case 2: order =", order2, ", s =", s2)
    print("Output:", result2)
    assert result2 == expected2, f"Failed test case 2: expected {expected2}, got {result2}"
    print("Passed ✅\n")

    # Test case 3
    order3 = "abc"
    s3 = "xyz"
    expected3 = "xyz"  # Since no characters from s are in order, s stays unchanged.
    result3 = sol.customSortString(order3, s3)
    print("Test case 3: order =", order3, ", s =", s3)
    print("Output:", result3)
    assert result3 == expected3, f"Failed test case 3: expected {expected3}, got {result3}"
    print("Passed ✅\n")


if __name__ == "__main__":
    main()
