# Heap

## Core Concept

A heap is a **complete binary tree** where every parent follows a simple rule:

- **Max Heap**: parent ≥ children
- **Min Heap**: parent ≤ children

## Why Array?

Heap uses array representation for O(1) access:

```text
     0
    / \
   1   2
  / \ /
 3  4 5

Array: [0, 1, 2, 3, 4, 5]
```

Navigation formulas:

- Parent of i: `(i-1) // 2`
- Left child: `2i + 1`
- Right child: `2i + 2`

## Two Key Operations

### Insert - O(log n)

1. Add to end
2. Bubble up until heap property restored

### Extract - O(log n)

1. Take root (min/max)
2. Move last element to root
3. Bubble down until heap property restored

## Python Usage

```python
import heapq

# Min heap (default)
heap = [3, 1, 4]
heapq.heapify(heap)        # O(n) - build heap
heapq.heappush(heap, 2)     # O(log n)
min_val = heapq.heappop(heap)  # O(log n)

# Max heap trick - negate values
max_heap = [-x for x in [3, 1, 4]]
heapq.heapify(max_heap)
max_val = -heapq.heappop(max_heap)
```

## When to Use

- **Priority Queue**: Process highest/lowest priority first
- **Top K Problems**: Keep K best/worst elements efficiently
- **Streaming Median**: Maintain median as data arrives
