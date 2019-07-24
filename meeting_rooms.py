"""
Meeting rooms
Given an array of meeting time intervals
consisting of start and end times
[[s1,e1],[s2,e2],.....]
find the minimum number of conference rooms required
input : [[0,30], [5,10], [15,20]]
output: 2

input: [[7,10], [2,4]]
output: 1
"""


def min_meeting_rooms(intervals):

    # intervals are list of list
    # interval: [[0, 30], [5, 10], [15, 20]]

    # assign initial values
    meeting, rooms, max_rooms = [], 0, 0

    # loop through intervals
    # when meeting starts it adds a room
    # when it ends it subtracts a room
    for start, end in intervals:
        # creating something like
        # [[0, 1], [30, -1]]
        # [[0, 1], [30, -1], [5, 1], [10, -1]]
        # [[0, 1], [30, -1], [5, 1], [10, -1], [15, 1], [20, -1]]
        meeting.extend([[start, 1], [end, -1]])

    # sort based on timings
    # [[0, 1], [5, 1], [10, -1], [15, 1], [20, -1], [30, -1]]
    for t, r in sorted(meeting):
        # r is 1 ,1, -1, 1, -1, -1
        # r+ will give 1, 2, 1 , 2, 1, 1
        rooms += r
        # max(1, 0) --> 1
        # max(2, 1) --> 2
        max_rooms = max(rooms, max_rooms)
        print(max_rooms)

    return max_rooms


if __name__ == "__main__":
    meetings = [[0,30], [5,10], [15,20]]
    min_meeting_rooms(meetings)










