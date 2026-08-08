class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, startTime: int, endTime: int) -> bool:

        # Find first interval whose start >= startTime
        left = 0
        right = len(self.events) - 1

        idx = len(self.events)  # default insertion at the end

        while left <= right:
            mid = (left + right) // 2

            if self.events[mid][0] >= startTime:
                idx = mid          # potential insertion position
                right = mid - 1    # try to find an even earlier one
            else:
                left = mid + 1

        # Check previous interval
        if idx > 0 and self.events[idx - 1][1] > startTime:
            return False

        # Check next interval
        if idx < len(self.events) and self.events[idx][0] < endTime:
            return False

        self.events.insert(idx, (startTime, endTime))
        return True