class PrefixTree:
    def __init__(self):
        self.c = {}
        self.end = False

    def insert(self, word: str) -> None:
        cur = self
        for w in word:
            if w not in cur.c:
                cur.c[w] = PrefixTree()
            cur = cur.c[w]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self
        for w in word:
            if w not in cur.c:
                return False
            cur = cur.c[w]
        return cur.end

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for p in prefix:
            if p not in cur.c:
                return False
            cur = cur.c[p]
        return True
        