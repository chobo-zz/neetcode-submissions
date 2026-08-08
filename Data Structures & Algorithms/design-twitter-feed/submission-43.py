class Twitter:

    def __init__(self):
        self.tweetMap = defaultdict(list) # userId -> list of tweets
        self.followMap = defaultdict(set) # userId -> list of followees
        self.tweetTime = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetTime -= 1
        self.tweetMap[userId].append((tweetId, self.tweetTime))
        if len(self.tweetMap[userId]) > 10:
            self.tweetMap[userId].pop(0)
        

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followMap[userId].add(userId)
        heap = []
        maxHeap = []
        if len(self.followMap[userId]) >= 10:
            for followeeId in self.followMap[userId]:
                if self.tweetMap[followeeId]:
                    lastTweetIndex = len(self.tweetMap[followeeId]) - 1
                    lastTweetId, lastTweetTime = self.tweetMap[followeeId][lastTweetIndex]
                    heapq.heappush(maxHeap, (-lastTweetTime, lastTweetId, followeeId, lastTweetIndex - 1))
                    if len(maxHeap) > 10:
                        heapq.heappop(maxHeap)
            
            while maxHeap:
                time, tweetId, followeeId, index = heapq.heappop(maxHeap)
                heapq.heappush(heap, (-time, tweetId, followeeId, index))
                
        else:
            for followeeId in self.followMap[userId]:
                if self.tweetMap[followeeId]:
                    lastTweetIndex = len(self.tweetMap[followeeId]) - 1
                    lastTweetId, lastTweetTime = self.tweetMap[followeeId][lastTweetIndex]
                    heapq.heappush(heap, (lastTweetTime, lastTweetId, followeeId, lastTweetIndex - 1))


        res = []
        while len(res) < 10 and heap:
            tweetTime, tweetId, userId, lastTweetIndex = heapq.heappop(heap)
            res.append(tweetId)
            if lastTweetIndex >= 0:
                nextTweetId, nextTweetTime = self.tweetMap[userId][lastTweetIndex]
                heapq.heappush(heap, (nextTweetTime, nextTweetId, userId, lastTweetIndex - 1))
        return res
            

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
