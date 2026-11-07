class Twitter:

    def __init__(self):
        self.time = 0
        self.userTweet = defaultdict(list)
        self.userFollow = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userTweet[userId].append((self.time, tweetId))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []

        self.userFollow[userId].add(userId)

        for followeeId in self.userFollow[userId]:
            for tweet in self.userTweet[followeeId]:
                heapq.heappush(minHeap, tweet)
                if len(minHeap) > 10:
                    heapq.heappop(minHeap)
            
        return [x[1] for x in sorted(minHeap, reverse = True)]


    def follow(self, followerId: int, followeeId: int) -> None:
        self.userFollow[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userFollow[followerId]:
            self.userFollow[followerId].remove(followeeId)
        
