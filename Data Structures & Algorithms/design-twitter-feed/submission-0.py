import heapq
class Twitter:

    def __init__(self):
        self.tweets={}
        self.following={}
        self.timestamp=0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId]=[]
        self.tweets[userId].append((self.timestamp,tweetId))
        self.timestamp+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap=[]
        feed=[]
        if userId not in self.following:
            self.following[userId]=set()
        self.following[userId].add(userId)
        for followeeid in self.following[userId]:
            if followeeid not in self.tweets:
                continue
            index=len(self.tweets[followeeid])-1
            if index==-1:
                continue
            time,tweetid=self.tweets[followeeid][index]
            heapq.heappush_max(heap,(time,tweetid,followeeid,index))
        
        while len(feed)<10:
            if not heap:
                return feed
            time,tweetid,userid,index=heapq.heappop_max(heap)
            feed.append(tweetid)
            index-=1
            if index<0:
                continue
            new_time,new_tweetid=self.tweets[userid][index]
            heapq.heappush_max(heap,(new_time,new_tweetid,userid,index))
        return feed
        


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId]=set()
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)

        
