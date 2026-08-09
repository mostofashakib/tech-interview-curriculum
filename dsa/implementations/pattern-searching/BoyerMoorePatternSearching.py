"""
Time Complexity: O(m(m-n+1))
Space Complexity: O(n)

Video explanation: https://www.youtube.com/watch?v=4Xyhb72LCX4
"""

def BoyerMoorePatternSearching(pat,text):
    # The preprocessing function for Boyer Moore's bad character heuristic
    
    def badCharacterHeuristic(string, size):
        NO_OF_CHARS = 256
        
        # Initialize all occurrence as -1
        badChar = [-1] * NO_OF_CHARS
        
        # Fill the actual value of last occurrence
        for i in range(size):
            badChar[ord(string[i])] = i
            
        return badChar
        
    patternLength = len(pat)
    textLength = len(text)

    # NoOfShifts is shift of the pattern with respect to text 
    NoOfShifts = 0

    # create the bad character list by calling the preprocessing function badCharacterHeuristic() for the given pattern 
    badChar = badCharacterHeuristic(pat, patternLength)
    
    while NoOfShifts < textLength - patternLength:
        j = patternLength - 1 
        
         # Keep reducing index j of pattern while characters of pattern and text are matching at this shift NoOfShifts 
        while j >= 0 and text[NoOfShifts+j] == pat[j]:
            j -= 1
        
        # If the pattern is present at current shift, then index j will become -1 after the above loop 
        if j < 0:
            print("Pattern found at index", NoOfShifts)

            """
            Shift the pattern so that the next character in text aligns with the last occurrence of it in pattern. 
            The condition NoOfShifts+patternLength < textLength is necessary for the case when pattern occurs at the end of text
            """
            # You can write either on of these
            NoOfShifts += patternLength + 1 if patternLength+ NoOfShifts < textLength else 1
            # NoOfShifts += patternLength - badChar[ord(text[NoOfShifts+patternLength])] if patternLength+ NoOfShifts < textLength else 1
            
        else:
            """
            Shift the pattern so that the bad character in text aligns with the last occurrence of the character to the left
            of the current mispatched character in pattern.The max function is used to make sure that we get a positive shift.
            We may get a negative shift if the last occurrence of bad character in pattern is on the right side of the current character. 
            """

            NoOfShifts += max(1, j - badChar[ord(text[NoOfShifts+j])])

Pattern = "Adib"
text = "My name is Adib Shakib"

BoyerMoorePatternSearching(Pattern, text)