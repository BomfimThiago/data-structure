"""
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
Example 3:

Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").

"""
# top down
def numDecodings(s):
    def dfs(nums, cache):
        if not nums:
            return 1
        
        if nums in cache:
            return cache[nums]
        
        count = 0

        if nums[0] != "0":
            count += dfs(nums[1:], cache)

        if len(nums) >= 2 and 10 <= int(nums[:2]) <= 26:
            count += dfs(nums[2:], cache)

        cache[nums] = count

        return cache[nums]
    
    return dfs(s, {})

# bottom up
def numDecodings2(s):
    n = len(s)
    dp = [0] * (n + 1)
    dp[n] = 1  # A inicialização para o caso base

    for i in range(n - 1, -1, -1):
        if s[i] == '0':
            continue

        # Contagem simples do caso onde consideramos apenas o dígito atual
        dp[i] += dp[i + 1]

        # Contagem para os casos onde consideramos o dígito atual e o próximo, se formarem um código válido
        if i < n - 1 and (s[i] == '1' or (s[i] == '2' and s[i + 1] <= '6')):
            dp[i] += dp[i + 2]

    return dp[0]


if __name__ == "__main__":
    # print(numDecodings("11106"))
    print(numDecodings2("12"))
