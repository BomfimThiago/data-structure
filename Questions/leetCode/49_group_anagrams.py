"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""

def groupAnagrams(strs):
    hashGroup = {}
    for s in strs:
        sortedS = "".join(sorted(s)) # O(n log n) # dont forget sorted in a string, retorn a list

        if not hashGroup.get(sortedS):
            hashGroup[sortedS] = [s]
        else:
            hashGroup[sortedS].append(s)


    return hashGroup.values()
    # time complexity O(m x n log n)
    # space complexity? O (m x n) considerando que m is the number of keys in the array, and n is the number of words that I stored in memory in each loop?


from collections import defaultdict
def groupAnagrams2(strs):
    res = defaultdict(list)
    for word in strs:
        # for each word we creat a tmp list with buckets to each letter in the lowercase alphabet 
        count = [0] * 26 # a ... Z 
        # this is faster then ordering because ordering is n logn , to create this is O(n)

        # for "eat" -> e, a, t
        for letter in word:
            # to discover the index of the letter in my list its enough to do the following
            # consider that all the letter are lowercase
            count[ord(letter) - ord("a")] += 1

        res[tuple(count)].append(word)
    return res.values()

    # time complexity O(n) or O(n log n) ? m size of the array e n log n ordering
    # time complexity O(m x n log n)
    # space complexity? 

if __name__ == "__main__":
    print(groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
    print(groupAnagrams2(strs = ["eat","tea","tan","ate","nat","bat"]))