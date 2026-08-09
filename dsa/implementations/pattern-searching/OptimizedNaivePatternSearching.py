def OptimizedNativePatternSearch(pat,txt):
    M = len(pat)
    N = len(txt)
    i = 0
    
    while i < N-M:
        j = 0
        
        while j < M:
            if txt[i+j] != pat[j]:
                break
            j += 1
            
        if j == M:
            print("The pattern starts from index", i)
            i = i + M
            
        elif j == 0:
            i = i + 1
        else:
            i = i + j
            
            
Pattern = "Adib"
text = "My name is Adib Shakib"

OptimizedNativePatternSearch(Pattern, text)