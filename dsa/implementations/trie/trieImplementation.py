"""
Look up Time Complexity: O(n)

Explanatiion: https://www.aleksandrhovhannisyan.com/blog/dev/trie-data-structure-implementation-in-python/
"""

from collections import defaultdict

class TrieNode():
	# Initializes a TrieNode with the given string and an initially empty dictionary mapping strings to TrieNodes.
    def __init__(self, text = ''):
        self.text = text
        self.children = defaultdict()
        self.isWord = False
        
class Trie():
    def __init__(self):
        self.root = self.get_node('')
        
    def get_node(self, char):
        return TrieNode(char)
        
    def insert(self, word):
        current = self.root
        
        for i, char in enumerate(word):
            if char not in current.children:
                prefix = word[0:i+1]
                current.children[char] = TrieNode(prefix)
            current = current.children[char]
            
        current.isWord = True
        
    def search(self, word):
    	# Returns the TrieNode representing the given word if it exists and False otherwise.
        current = self.root
        
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
            
        return True if current and current.isWord else False
        
    def delete(self, word):
        current = self.root
        
        for char in word:
            
            if char not in current.children:
                print("Word not found")
                return -1
                
            current = current.children[char]
            
        current.isWord = False
        return 0
        
    def update(self, old_word, new_word):
        val = self.delete(old_word)
        if val == 0:
            self.insert(new_word)
            
    def __child_words_for(self, node, words):
    	# Private helper function. Cycles through all children of node recursively, adding them to words if they constitute whole words
        if node.isWord == True:
            words.append(node.text)
            
        for letter in node.children:
            self.__child_words_for(node.children[letter], words)
        
    def starts_with(self, prefix):
    	# Returns a list of all words beginning with the given prefix, or an empty list if no words begin with that prefix.
        words = []
        current = self.root
        
        for char in prefix:
        
            if char not in current.children:
                return []
                
            current = current.children[char]
        
        self.__child_words_for(current, words)
        
        return words

    def size(self, current = None):
	    '''
	    Returns the size of this prefix tree, defined
	    as the total number of nodes in the tree.
	    '''
	    if not current:
	        current = self.root
	    count = 1
	    for letter in current.children:
	        count += self.size(current.children[letter])
	    return count
            
if __name__ == "__main__":

    strings = ["pqrs", "pprt", "psst", "qqrs", "pqrs"]

    t = Trie()
    for word in strings:
        t.insert(word)

    print(t.search("pqrs"))
    print(t.search("pprt"))
    t.delete("pprt")
    print(t.search("pprt"))
    print(t.search("qqrq"))
    t.delete("pqrq")
    t.update("psst", "pprt")
    print(t.search("pprt"))
    print(t.starts_with("p"))
    print(t.size())