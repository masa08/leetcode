# Backtracking

## Core Idea

Backtracking = **Systematic trial and error**

When stuck → undo last choice → try different path

## The Pattern

```python
def backtrack(state):
    if is_complete(state):
        save_solution(state)
        return

    for choice in get_choices():
        make_choice(state, choice)      # Try
        backtrack(state)                 # Explore
        undo_choice(state, choice)       # Backtrack
```

## Mental Model

Think of it as exploring a maze:

```text
         Start
         /   \
       A       B     ← Choose path
      / \     / \
     C   D   E   F   ← Dead end? Go back
    /
   Goal!
```

## Classic Example: Generate All Subsets

```python
def subsets(nums):
    result = []

    def backtrack(start, path):
        result.append(path[:])  # Save current subset

        for i in range(start, len(nums)):
            path.append(nums[i])        # Include nums[i]
            backtrack(i + 1, path)       # Explore with it
            path.pop()                   # Exclude nums[i]

    backtrack(0, [])
    return result

# [1,2,3] → [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]
```

## Why It Works

1. **Complete Search**: Tries all possibilities
2. **Pruning**: Abandons bad paths early
3. **State Recovery**: Each recursive call has clean slate

## Common Patterns

### Finding All Solutions

```python
def find_all():
    def backtrack(state):
        if is_solution(state):
            results.append(state[:])
            return  # Keep searching
        # ... explore choices
```

### Finding One Solution

```python
def find_one():
    def backtrack(state):
        if is_solution(state):
            return True  # Stop immediately
        # ... explore choices
        if backtrack(new_state):
            return True
        return False
```

## Key Insight

Backtracking is essentially **DFS with state management**:

- DFS explores paths
- Backtracking undoes changes to reuse state

## When to Use

✅ Need all possible solutions
✅ Can eliminate bad paths early
✅ Solution has "build-up" structure

❌ Need just any/best solution → Use BFS/Greedy
❌ Overlapping subproblems → Use DP
