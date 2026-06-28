class TimeMap:

    def __init__(self):
        self.tm={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.tm:
            self.tm[key]=[]
        self.tm[key].append((timestamp,value))
        return None

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tm:
            return ""
        best=-1
        values=self.tm[key]
        l,r=0,len(values)-1
        while l<=r:
            m=(l+r)//2
            if values[m][0]<=timestamp:
                best=m
                l=m+1
            if values[m][0]>timestamp:
                r=m-1
        if best==-1:
            return ""
        return values[best][1]
