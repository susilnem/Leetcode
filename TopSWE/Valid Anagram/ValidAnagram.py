"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
-------------
Example 1:
-------------
Input: s = "anagram", t = "nagaram"
Output: true
-------------
Example 2:
-------------
Input: s = "rat", t = "car"
Output: false

"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        S = {}
        T = {}

        # counting the letters from the string
        for i in range(len(s)):
            S[s[i]] = 1+S.get(s[i], 0)
            T[t[i]] = 1+T.get(t[i], 0)

        if (S == T):
            return True
