from bisect import bisect_left

class MyCalendar:
    def __init__(self):
        self.events = []
    def book(self, startTime: int, endTime: int) -> bool:
        i = bisect_left(self.events, startTime, key=lambda e:e[0])
        ok_before = (i==0) or self.events[i-1][1] <= startTime 
        ok_after = (i==len(self.events)) or self.events[i][0] >= endTime
        if ok_before and ok_after:
            self.events.insert(i, (startTime, endTime))
            return True
        return False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
