"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 
Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 
Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""
import string
def isAnagram(s, t):
    # anagram is word frase formed by reaging letters
    # Time Complexity O(3n), O(n)
    # space complexity O(n)

    if len(s) != len(t):
        return False

    hashS = {}
    hashT = {}

    for i in range(len(s)):
        hashS[s[i]] = hashS.get(s[i], 0) + 1
        hashT[t[i]] = hashT.get(t[i], 0) + 1

    # when I do letter in a key, value is always the key
    for letter in hashS:
        if hashS[letter] != hashT.get(letter, 0):
            return False
    
    return True



def isAnagram2(s, t):
    # another solution is to order the both array and then se if them are equal
    if len(s) != len(t):
        return False

    sortedS = sorted(s)
    sortedT = sorted(t)
    for i in range(len(s)):
        if sortedS[i] != sortedT[i]:
            return False
    return True

if __name__ == "__main__":
    print(isAnagram(s = "rat", t = "car"))
    print(isAnagram2(s = "rat", t = "car"))