"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

"""
# top - bottom solution
def longestCommonSubsequence(text1, text2):
    def dfs(i, j, cache):
        if i == len(text1) or j == len(text2):
            return 0
        
        if (i, j) in cache:
            return cache[(i, j)]
        
        count = 0
        if text1[i] == text2[j]:
            count += 1 + dfs(i + 1, j + 1, cache)
        else:
            count += max(dfs(i, j + 1, cache), dfs(i + 1, j, cache))
    
        cache[(i, j)] = count

        return cache[(i, j)]

    return dfs(0, 0, {})

if __name__ == "__main__":
    print(longestCommonSubsequence(text1 = "ezupkr", text2 = "ubmrapg"))