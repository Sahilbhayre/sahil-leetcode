class TrieNode:
    def __init__(self):
        self.children = {}
        #Store the indeex of the best matching through word passing or ending
        self.best_idx = -1

class Solution(object):
    def stringIndices(self, wordsContainer, wordsQuery):
        """
        :type wordsContainer: List[str]
        :type wordsQuery: List[str]
        :rtype: List[int]
        """
        root = TrieNode()

        # 1. Pre-calculate the global best to initialize the root node.
        global_best_idx = 0
        for i in range(1, len(wordsContainer)):
            if len(wordsContainer[i]) < len(wordsContainer[global_best_idx]):
                global_best_idx = i
            
        root.best_idx = global_best_idx

        # 2. Build the Trie with reversed words
        for idx, word in enumerate(wordsContainer):
            curr = root
            # Reversing the word lets us treat suffix matching as prefix matching
            for char in reversed(word):
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
                
                # Update the best index for the current prefix track
                if curr.best_idx == -1:
                    curr.best_idx = idx
                else:
                    curr_best_len = len(wordsContainer[curr.best_idx])
                    # Strictly shorter length wins
                    if len(word) < curr_best_len:
                        curr.best_idx = idx
                    # If lengths are equal, the earlier index wins.
                    # Since we iterate 'idx' from 0 to N-1, the earlier index 
                    # is already stored, so we don't overwrite it.

        # 3. Process each query
        ans = []
        for query in wordsQuery:
            curr = root
            for char in reversed(query):
                if char in curr.children:
                    curr = curr.children[char]
                else:
                    # Break early if the common suffix path diverges
                    break
            # The node we stop at contains the pre-calculated ideal index
            ans.append(curr.best_idx)
            
        return ans