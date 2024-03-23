"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
              
"""
from typing import List


def longestCommonPrefix(self, strs: List[str]) -> str:
    smallest_word = min(strs, key=len)

    res = smallest_word

    for word in strs:        
        while res and not word.startswith(res):
            res = res[:-1]

        if not res:
            return ""
        
    return res



            

