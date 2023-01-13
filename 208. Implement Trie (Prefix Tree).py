class Trie:
    class Node:
        def __init__(self, end = False):
            self.edges = dict()
            self.end = end

    def __init__(self):
        self.root = self.Node()

    def insert(self, word: str) -> None:
        self.node = self.root
        for c in word:
            if not c in self.node.edges:
                self.node.edges[c] = self.Node()

            self.node = self.node.edges[c]
            
        self.node.end = True


    def search(self, word: str) -> bool:
        self.node = self.root
        for c in word:
            if not c in self.node.edges:
                return False

            self.node = self.node.edges[c]
            
        return self.node.end
        

    def startsWith(self, prefix: str) -> bool:
        self.node = self.root

        for c in prefix:
            if not c in self.node.edges:
                return False
            
            self.node = self.node.edges[c]
            
        return True