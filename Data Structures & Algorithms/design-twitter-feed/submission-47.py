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
        for followeeId in self.followMap[userId]:
            tweets = self.tweetMap[followeeId]
            if tweets:
                tweetId, tweetCount = tweets[-1]
                nextTweetIndex = len(tweets) - 2
                
                heapq.heappush(heap, (tweetCount, tweetId, followeeId, nextTweetIndex))
        
        res = []
        while len(res) < 10 and heap:
            tweetCount, tweetId, followeeId, nextTweetIndex = heapq.heappop(heap)
            res.append(tweetId)
            if nextTweetIndex >= 0:
                tweets = self.tweetMap[followeeId]
                tweetId, tweetCount = tweets[nextTweetIndex]
                nextTweetIndex -= 1
                heapq.heappush(heap, (tweetCount, tweetId, followeeId, nextTweetIndex))
        return res
            



    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
