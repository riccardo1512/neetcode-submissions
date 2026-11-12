class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        adj = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i + 1:]
                adj[pattern].append(word)


        queue = deque([beginWord])
        visited = set()
        res = 1

        while queue:

            for i in range(len(queue)):
                node = queue.popleft()

                if node == endWord:
                    return res
                
                for j in range(len(node)):
                    pattern = node[:j] + '*' + node[j + 1:]

                    for nei in adj[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            queue.append(nei)

            res += 1
        return 0
