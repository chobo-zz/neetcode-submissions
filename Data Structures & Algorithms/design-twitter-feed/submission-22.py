class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((tweetId, self.count))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followMap[userId].add(userId)
        heap = []
        res = []

        for userId in self.followMap[userId]:
            if userId in self.tweetMap:
                lastIndex = len(self.tweetMap[userId]) - 1
                tweetId, count = self.tweetMap[userId][lastIndex]
                heapq.heappush(heap, (count, tweetId, lastIndex - 1, userId))

        while heap and len(res) < 10:
            count, tweetId, index, userId = heapq.heappop(heap)
            res.append(tweetId)

            if index >= 0:
                tweetId, count = self.tweetMap[userId][index]
                heapq.heappush(heap, (count, tweetId, index - 1, userId))
        return res
            

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
