"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
----------
Input: strs = ["flower","flow","flight"]
Output: "fl"


Example 2:
----------

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


"""


# Solution

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        first = strs[0]
        for i in strs[1:]:
            while i[:len(first)] != first:
                first = first[:-1]
                if not first:
                    return ""
        return first



or 


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        short = min(strs, key=len)
        for i, char in enumerate(short):
            for other in strs:
                if other[i] != char:
                    return short[:i]
        return short
