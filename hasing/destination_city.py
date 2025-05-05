"""
Problem 1436: Destination City

You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path
going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing
to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly
one destination city.

Examples:

Example 1:
Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo"
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consists of: 
"London" -> "New York" -> "Lima" -> "Sao Paulo".

Example 2:
Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are: 
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
Clearly the destination city is "A".

Example 3:
Input: paths = [["A","Z"]]
Output: "Z"

Constraints:
- 1 <= paths.length <= 100
- paths[i].length == 2
- 1 <= cityAi.length, cityBi.length <= 10
- cityAi != cityBi
- All strings consist of lowercase and uppercase English letters and the space character.
"""

from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # Initialize a set to store cities that have outgoing paths
        cities_with_outgoing_paths = set()
        
        # Iterate through the paths to identify cities with outgoing paths
        for path in paths:
            cities_with_outgoing_paths.add(path[0])  # cityAi has an outgoing path
        
        # Now find the city that does not have any outgoing paths (destination city)
        for path in paths:
            if path[1] not in cities_with_outgoing_paths:
                return path[1]  # Return the destination city


def main():
    sol = Solution()

    # Test case 1
    paths1 = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
    expected1 = "Sao Paulo"
    result1 = sol.destCity(paths1)
    print("Test case 1:", result1)
    assert result1 == expected1, f"Failed: expected {expected1}, got {result1}"
    print("Passed ✅\n")

    # Test case 2
    paths2 = [["B","C"],["D","B"],["C","A"]]
    expected2 = "A"
    result2 = sol.destCity(paths2)
    print("Test case 2:", result2)
    assert result2 == expected2, f"Failed: expected {expected2}, got {result2}"
    print("Passed ✅\n")

    # Test case 3
    paths3 = [["A","Z"]]
    expected3 = "Z"
    result3 = sol.destCity(paths3)
    print("Test case 3:", result3)
    assert result3 == expected3, f"Failed: expected {expected3}, got {result3}"
    print("Passed ✅\n")


if __name__ == "__main__":
    main()
