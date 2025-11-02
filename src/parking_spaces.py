"""
HW02 — Parking Spaces: Minimum Spots Needed

Implement min_parking_spots(intervals) -> int

Behavior:
- Given a list of (start, end) times, return the minimum number of parking spots
  so that no car waits. If a car leaves at time t and another arrives at time t,
  the same spot can be reused.
"""
import heapq
def min_parking_spots(intervals):
    # TODO Steps:
    # 1) Understand: we need peak overlap count.
    # 2) Re-phrase: track earliest end; reuse when end <= start.
    # 3) Identify: inputs list of pairs; output int; vars heap, rooms.
    # 4) Break down: sort by start; pop ends <= start; push end; track max size.
    # 5) Pseudocode above; implement with heapq.
    # 6) Write code.
    # 7) Debug with small examples.
    # 8) Confirm O(n log n).
    if not intervals:
        return 0

    intervals.sort()

    end_time_heap = []
    max_spots = 0

    for (start, end) in intervals:
        
        while end_time_heap and end_time_heap[0] <= start:
            heapq.heappop(end_time_heap)

        heapq.heappush(end_time_heap, end)

        max_spots = max(max_spots, len(end_time_heap))

    return max_spots
