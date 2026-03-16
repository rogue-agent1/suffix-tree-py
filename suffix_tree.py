"""Suffix Tree — Ukkonen's algorithm (simplified)."""
class SuffixTree:
    def __init__(self, text):
        self.text = text + "$"
        self.nodes = [{}]
        self._build()
    def _build(self):
        for i in range(len(self.text)):
            suffix = self.text[i:]
            node = 0
            j = 0
            while j < len(suffix):
                c = suffix[j]
                if c in self.nodes[node]:
                    edge_start, edge_end, child = self.nodes[node][c]
                    edge = self.text[edge_start:edge_end]
                    k = 0
                    while k < len(edge) and j < len(suffix) and edge[k] == suffix[j]:
                        k += 1; j += 1
                    if k == len(edge):
                        node = child
                    else:
                        mid = len(self.nodes)
                        self.nodes.append({})
                        self.nodes[mid][edge[k]] = (edge_start+k, edge_end, child)
                        new_leaf = len(self.nodes)
                        self.nodes.append({})
                        self.nodes[mid][suffix[j]] = (i+j, len(self.text), new_leaf)
                        self.nodes[node][c] = (edge_start, edge_start+k, mid)
                        break
                else:
                    new_leaf = len(self.nodes)
                    self.nodes.append({})
                    self.nodes[node][c] = (i+j, len(self.text), new_leaf)
                    break
    def search(self, pattern):
        node = 0; i = 0
        while i < len(pattern):
            c = pattern[i]
            if c not in self.nodes[node]: return False
            edge_start, edge_end, child = self.nodes[node][c]
            edge = self.text[edge_start:edge_end]
            k = 0
            while k < len(edge) and i < len(pattern):
                if edge[k] != pattern[i]: return False
                k += 1; i += 1
            node = child
        return True

if __name__ == "__main__":
    st = SuffixTree("banana")
    assert st.search("ana")
    assert st.search("ban")
    assert st.search("nana")
    assert not st.search("xyz")
    assert not st.search("banan$")
    print("Suffix tree: all searches correct")
    print("All tests passed!")
