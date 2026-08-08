class Twitter:

    def __init__(self):
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count -= 1
        self.tweetMap[userId].append((tweetId, self.count))

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followMap[userId].add(userId)
        heap = []
        res = []

        for followeeId in self.followMap[userId]:
            if self.tweetMap[followeeId]:
                lastIndex = len(self.tweetMap[followeeId]) - 1
                tweetId, tweetTime = self.tweetMap[followeeId][lastIndex]
                heapq.heappush(heap, (tweetTime, tweetId, followeeId, lastIndex - 1))
        
        while heap and len(res) < 10:
            tweetTime, tweetId, followeeId, lastIndex = heapq.heappop(heap)
            res.append(tweetId)

            if lastIndex >= 0:
                tweetId, tweetTime = self.tweetMap[followeeId][lastIndex]
                heapq.heappush(heap, (tweetTime, tweetId, followeeId, lastIndex - 1))
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
