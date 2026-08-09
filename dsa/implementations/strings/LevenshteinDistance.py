"""
This is an algorithm that is used to find the minimum number of operatings needed to transform one string to another
using three edit operations.

Reading: https://www.geeksforgeeks.org/edit-distance-dp-5/
Video Explanation: https://www.youtube.com/watch?v=MiqoA-yF-0M
                   https://www.youtube.com/watch?v=ocZMDMZwhCY
"""

"""
Algorithm: Naive Recursive Algorithm

1) If last characters of two strings are same, nothing much to do. Ignore last characters and get count for remaining strings.
    So we recur for lengths m-1 and n-1.

2) Else (If last characters are not same), we consider all operations on ‘str1’, consider all three operations on last character of first string,
    recursively compute minimum cost for all three operations and take minimum of three values.
        -> Insert: Recur for m and n-1
        -> Remove: Recur for m-1 and n
        -> Replace: Recur for m-1 and n-1

Time Complexity: O(2^n), Exponential
Space Complexity: O(n)
n = length of first string
m = length of second string
"""

def editDistance(str1, str2, m, n): 
  
    # If first string is empty, the only option is to 
    # insert all characters of second string into first 
    if m == 0: 
         return n 
  
    # If second string is empty, the only option is to 
    # remove all characters of first string 
    if n == 0: 
        return m 
  
    # If last characters of two strings are same, nothing 
    # much to do. Ignore last characters and get count for 
    # remaining strings. 
    if str1[m-1]== str2[n-1]: 
        return editDistance(str1, str2, m-1, n-1) 
  
    # If last characters are not same, consider all three 
    # operations on last character of first string, recursively 
    # compute minimum cost for all three operations and take 
    # minimum of three values. 
    return 1 + min(editDistance(str1, str2, m, n-1),    # Insert 
                   editDistance(str1, str2, m-1, n),    # Remove 
                   editDistance(str1, str2, m-1, n-1)    # Replace 
                   ) 
  
# Driver program to test the above function 
str1 = "sunday"
str2 = "saturday"
print editDistance(str1, str2, len(str1), len(str2))


"""
Edge case: This method is not suitable if the length of strings is greater than 2000 as it can only create 2D array of 2000 x 2000.

Time Complexity: O(n*m)
Space Complexity: O(n*m)
n = length of first string
m = length of second string
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)  # column
        n = len(word2)  # row
        
        # Create a table to store results of subproblems 
        dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

        # Base cases

        # If first string is empty, only option is to insert all characters of second string

        for i in range(n+1):
            dp[0][i] = i  # Min. operations = i
        
        # If second string is empty, only option is to remove all characters of first string
        for j in range(m+1):
            dp[j][0] = j  # Min. operations = j 
        
        # Fill d[][] in bottom up manner 
        for i in range(1, m + 1): 
            for j in range(1, n + 1):
                insert = dp[i][j-1]
                remove = dp[i-1][j]
                replace =  dp[i-1][j-1]

                # If last characters are same, ignore last character and recurse for remaining string 
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = replace

                # If last character are different, consider all possibilities and find minimum operations
                else: 
                    dp[i][j] = 1 + min(insert, remove, replace)

        return dp[m][n]
