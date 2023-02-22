"""

A phrase is a palindrome if , after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.


Example 1:
----------
Input: s = "A man, a plan, a canal: Panama"
Output: true

Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
----------
Input: s = "race a car"
Output: false

Explanation: "raceacar" is not a palindrome.

Example 3:
----------

Input: s = " "
Output: true

Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        output = ''
        for i in s:
            if i.isalnum():
                output += i.lower()
        return output == output[::-1]


# Explanation

"""

The function first initializes an empty string called output.
It then loops through each character in the input strings and
checks if the character is alphanumeric using the isalnum() method.
If the character is alphanumeric, it is converted to lowercase using the lower() method and
appended to the output string. This effectively removes any non-alphanumeric characters from the input string and
converts all alphabetic characters to lowercase.
Finally, the function checks if the output string is equal to its reverse using slicing notation([::-1]).
If they are equal, the function returns True indicating that the input string is a palindrome. Otherwise, it returns False.

"""