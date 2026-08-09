"""
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

def NativePatternSearch(pat,txt):
    M = len(pat)
    N = len(txt)
    
    for i in range(N-M+1):
        j = 0
        
        while j < M:
            if txt[i+j] != pat[j]:
                break
            j += 1
            
        if j == M:
            print("The pattern starts from index", i)
            
Pattern = "Adib"
text = "My name is Adib Shakib"

NativePatternSearch(Pattern, text)