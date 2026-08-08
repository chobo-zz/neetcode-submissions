class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list) # userId -> [tweets]
        self.followMap = defaultdict(set) # userId -> [followees]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count -= 1
        self.tweetMap[userId].append((tweetId, self.count))

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followMap[userId].add(userId)
        heap = []
        res = []
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                # get most recent tweet from this person
                # keep track of last index to get more tweets from this person
                lastIndex = len(self.tweetMap[followeeId]) - 1
                tweetId, count = self.tweetMap[followeeId][-1]
                heapq.heappush(heap, (count, tweetId, followeeId, lastIndex - 1))
        while heap and len(res) < 10:
            count, tweetId, followeeId, lastIndex = heapq.heappop(heap)
            res.append(tweetId)
            if lastIndex >= 0:
                tweetId, count = self.tweetMap[followeeId][lastIndex]
                heapq.heappush(heap, (count, tweetId, followeeId, lastIndex - 1))
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
