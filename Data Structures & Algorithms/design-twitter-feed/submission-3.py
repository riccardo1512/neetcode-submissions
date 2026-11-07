class Twitter:

    def __init__(self):
        self.count = 0
        self.userTweet = defaultdict(list)
        self.userFollow = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userTweet[userId].append((self.count, tweetId))
        self.count -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        res = []

        users = self.userFollow[userId] | {userId} # union |

        # Let's push in the heap the last post of each friend
        for followeeId in users:
            if followeeId in self.userTweet and self.userTweet[followeeId]:
                index = len(self.userTweet[followeeId]) - 1
                count, tweetId = self.userTweet[followeeId][index]
                heapq.heappush(minHeap, (count, tweetId, followeeId, index))

        # dynamic extraction
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)

            res.append(tweetId)

            if index > 0:
                count, tweetId = self.userTweet[followeeId][index - 1]
                heapq.heappush(minHeap, (count, tweetId, followeeId, index - 1))

        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.userFollow[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userFollow[followerId]:
            self.userFollow[followerId].remove(followeeId)
        
