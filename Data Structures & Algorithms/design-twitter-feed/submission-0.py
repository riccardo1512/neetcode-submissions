import heapq
from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list)    # userId -> list di (time, tweetId)
        self.followMap = defaultdict(set)   # userId -> set di followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Decrementiamo per simulare un max-heap (più recente = valore minore)
        self.time -= 1
        self.tweetMap[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        # L'utente deve vedere i tweet dei seguiti + i propri
        users = self.followMap[userId] | {userId}

        # Inseriamo nell'heap solo l'ultimo tweet di ogni utente rilevante
        for u in users:
            if self.tweetMap[u]:
                idx = len(self.tweetMap[u]) - 1
                time, tweetId = self.tweetMap[u][idx]
                minHeap.append((time, tweetId, u, idx - 1))

        heapq.heapify(minHeap)

        # Estraiamo i 10 più recenti
        while minHeap and len(res) < 10:
            time, tweetId, u, next_idx = heapq.heappop(minHeap)
            res.append(tweetId)
            
            # Se l'utente ha altri tweet precedenti, spingiamo il successivo
            if next_idx >= 0:
                next_time, next_tweetId = self.tweetMap[u][next_idx]
                heapq.heappush(minHeap, (next_time, next_tweetId, u, next_idx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)