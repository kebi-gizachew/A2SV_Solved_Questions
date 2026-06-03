class TrieNode:
    def __init__(self):
        self.trie = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.child = TrieNode()    
        
    def addWord(self, word: str) -> None:
        cur = self.child
        for i in word:
            if i not in cur.trie:
                cur.trie[i] = TrieNode()
            cur = cur.trie[i]
        cur.end = True
         

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.end
            if word[i] == ".":
                for k in node.trie.values():
                    if dfs(k , i + 1):
                        return True
                return False
            if word[i] not in node.trie:
                return False
            return dfs(node.trie[word[i]] , i + 1)
        return dfs(self.child , 0)
        

            


        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna