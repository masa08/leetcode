import heapq

# minHeap
minHeap = []

heapq.heapify(minHeap)

heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 1)
heapq.heappush(minHeap, 2)

print("minHeap: ", minHeap)

peekNum = minHeap[0]
print("peek number: ", peekNum)

popNum = heapq.heappop(minHeap)
print("pop number: ", popNum)

print("peek number: ", minHeap[0])
print("minHeap: ", minHeap)

# maxheap
maxHeap = []
heapq.heapify(maxHeap)

heapq.heappush(maxHeap, -1 * 1)
heapq.heappush(maxHeap, -1 * 3)
heapq.heappush(maxHeap, -1 * 2)

print("manHeap: ", maxHeap)

print("peekNumber: ", maxHeap[0] * -1)

print("pop number: ", heapq.heappop(maxHeap) * -1)

print("peekNumber: ", maxHeap[0] * -1)
