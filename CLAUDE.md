# CLAUDE.md

Claude Code guidelines for LeetCode solutions repository.

## Repository Structure

```text
leetcode/
├── solutions/       # Managed by problem number (e.g., 1_two_sum.py)
├── model/           # Common data structures (ListNode, TreeNode)
├── utils/           # Helper functions
└── explore/         # Pattern abstractions
    ├── algorithms/  # Algorithm techniques
    └── data_structures/  # Data structure implementations
```

## Coding Principles

### Top 5 Core Principles

#### 1. **UMPIRE Method** - Systematic Problem Solving

```text
U - Understand: Comprehend problem, enumerate edge cases
M - Match: Match with known patterns
P - Plan: Explain approach, analyze complexity
I - Implement: Clean implementation
R - Review: Code walkthrough
E - Evaluate: Verify time/space complexity
```

💡 Clear thought process, questioning ability, edge case consideration

#### 2. **Edge Cases First** - Defensive Programming

```python
def solve(nums: List[int]) -> int:
    # Handle edge cases first
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    # Main logic
    # ...
```

💡 Robustness, production-ready code

#### 3. **Progressive Optimization** - From Correctness to Efficiency

```python
# Step 1: Brute Force O(n²)
def twoSum_v1(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# Step 2: Optimized O(n)
def twoSum_v2(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
```

💡 Optimization skills, understanding trade-offs

#### 4. **Pattern Recognition** - High-Frequency Techniques

- **Two Pointers**: Sorted arrays, pair searching
- **Sliding Window**: Subarrays, substrings
- **Hash Map**: O(1) lookup
- **DFS/BFS**: Graph and tree traversal
- **Dynamic Programming**: Optimization problems

💡 Problem-solving efficiency, pattern application skills

#### 5. **Clarity First** - Readability and Communication

```python
# Bad example
def fn(a, n):
    i, j = 0, n-1
    while i < j:
        # ...

# Good example
def findPair(arr: List[int], target: int) -> List[int]:
    left, right = 0, len(arr) - 1
    while left < right:
        # Search for target pair using two pointers
```

💡 Team collaboration skills, maintainability focus

### Implementation Guidelines

```python
class Solution:
    def methodName(self, params) -> ReturnType:
        # 1. Edge case handling (Edge Cases First)
        if not params:
            return default_value

        # 2. Choose approach (Pattern Recognition)
        # e.g., Two Pointers, Hash Map, etc.

        # 3. Main logic (clear variable names)
        result = self.helper(params)

        # 4. Return result
        return result

    def helper(self, data):
        """Helper functions should have clear responsibilities"""
        pass

def main():
    # Test cases (basic, edge, large scale)
    solution = Solution()

    # Basic cases
    assert solution.methodName([1,2,3]) == expected

    # Edge cases
    assert solution.methodName([]) == default
    assert solution.methodName([1]) == single_element_result

    print("All tests passed!")
    
if __name__ == "__main__":
    main()
```

## Interview Communication Strategy

- **Don't answer directly** - Provide hints to encourage thinking
- **Time/Space complexity** - Always discuss
- **Edge cases** - Point out overlooked cases
- **Optimization** - Explore possibilities for better solutions

## Problem-Solving Flow

1. **Understand** - Verify input/output examples, enumerate edge cases
2. **Design** - Explain approach, analyze complexity
3. **Implement** - Write simple and clear code
4. **Improve** - Consider optimization opportunities

## Key Decision Criteria

- **Readability > Cleverness** - Understandability is crucial in interviews
- **Standard libraries** - Basic ones are OK to use (Counter etc. with explanation)
- **Trade-offs** - Be clear about time vs space, implementation complexity vs efficiency
