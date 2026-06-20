class Solution:
    def topoSort(self, V, adj):
        indeg = [0] * V
        topo = []
        
        for i in range(V):
            for n in adj[i]:
                indeg[n] += 1
                
        q = deque()
        for i in range(V):
            if indeg[i] == 0:
                q.append(i)
                
        while q:
            node = q.popleft()
            topo.append(node)
            
            for i in adj[node]:
                indeg[i] -= 1
                if indeg[i] == 0:
                    q.append(i)
                    
        return topo if len(topo) == V else []


    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)

        unique_chars = set()
        for w in words:
            for c in w:
                unique_chars.add(c)

        char_to_idx = {c: i for i, c in enumerate(unique_chars)}
        k = len(unique_chars)

        adj = [[] for _ in range(k)]
        # topo = []
        
        for i in range(n - 1):
            s1 = words[i]
            s2 = words[i + 1]
            
            minlen = min(len(s1), len(s2))
            for j in range(minlen):
                if len(s1) > len(s2) and s1[:minlen] == s2[:minlen]:
                    return ""
                if s1[j] != s2[j]:
                    # adj[ord(s1[j]) - ord('a')].append(ord(s2[j]) - ord('a'))
                    adj[char_to_idx[s1[j]]].append(char_to_idx[s2[j]])
                    break
            
        topo = self.topoSort(k, adj)
        
        ans = ''
        # for i in topo:
        #     ans += chr(i + ord('a'))

        idx_to_char = {i: c for c, i in char_to_idx.items()}

        ans = ''.join([idx_to_char[i] for i in topo])    
        return ans