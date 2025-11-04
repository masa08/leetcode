"""
Binary Search - Visual Pattern Reference

This file provides visual diagrams to help understand different binary search patterns.
Run this file to see interactive examples!
"""


def print_pattern(title: str, array: str, condition: str, description: str):
    """Helper to print formatted patterns"""
    print(f"\n{'='*70}")
    print(f"Pattern: {title}")
    print(f"{'='*70}")
    print(array)
    print(condition)
    print(f"\nDescription: {description}")
    print()


def visualize_all_patterns():
    """Comprehensive visual guide to binary search patterns"""

    print("\n" + "="*70)
    print(" BINARY SEARCH VISUAL PATTERN GUIDE ".center(70))
    print("="*70)

    # Pattern 1: Basic Search (Unique Array)
    print_pattern(
        "1. Basic Search (Unique Values)",
        """
    idx:  0  1  2  3  4  5  6
    val:  1  3  4 19 20 33 53
                ↑
          target = 4, answer = index 2

    Using left/right:
    Step 1: [1  3  4 |19| 20 33 53]  mid=19 > 4, search left
    Step 2: [1 |3| 4  19  20 33 53]  mid=3  < 4, search right
    Step 3: [1  3 |4| 19  20 33 53]  mid=4 == 4, found!
        """,
        "left/right works fine for UNIQUE values",
        "Returns exact index or -1. Time: O(log N)"
    )

    # Pattern 2: Lower Bound (Duplicates)
    print_pattern(
        "2. Lower Bound (First Occurrence)",
        """
    idx:  0  1  2  3  4  5  6  7  8
    val:  1  3  3  4  4  4  4  4 19
                   ↑
         target = 4, answer = 3 (first 4)

    Condition: nums[i] >= 4
    val:  1  3  3  4  4  4  4  4 19
    cond: F  F  F  T  T  T  T  T  T
          |--ng--| |------ok-------|
                   ↑
              boundary (leftmost T)

    Why not left/right?
    - left/right might find index 4, 5, or 6
    - We need the FIRST occurrence (index 3)
    - OK/NG guarantees the boundary!
        """,
        "ok/ng pattern finds the LEFTMOST True",
        "Condition: nums[i] >= target, ok=N-1, ng=0"
    )

    # Pattern 3: Upper Bound (Last Occurrence)
    print_pattern(
        "3. Upper Bound (Last Occurrence)",
        """
    idx:  0  1  2  3  4  5  6  7  8
    val:  1  3  3  4  4  4  4  4 19
                               ↑
         target = 4, answer = 7 (last 4)

    Condition: nums[i] <= 4
    val:  1  3  3  4  4  4  4  4 19
    cond: T  T  T  T  T  T  T  T  F
          |------ok-------| |-ng-|
                            ↑
                   boundary (rightmost T)

    Symmetry with Lower Bound:
    - Lower: >= target, ok starts right
    - Upper: <= target, ok starts left
        """,
        "ok/ng pattern finds the RIGHTMOST True",
        "Condition: nums[i] <= target, ok=0, ng=N-1"
    )

    # Pattern 4: OK/NG Direction Guide
    print_pattern(
        "4. OK/NG Initialization Guide",
        """
    Question: Where should ok and ng start?

    Rule:
    - ok = value that DEFINITELY satisfies condition
    - ng = value that DEFINITELY does NOT satisfy condition

    Example 1: Condition "nums[i] >= target"
        F F F F T T T T T
        |--ng--| |--ok--|
        ng=0, ok=N-1 (or ng=-1, ok=N)

    Example 2: Condition "nums[i] <= target"
        T T T T T F F F F
        |--ok--| |--ng--|
        ok=0, ng=N-1 (or ok=-1, ng=N)

    Example 3: Age <= 23
        age:  0 ... 23  24 ... 150
        cond: T ... T   F  ... F
              |--ok--| |---ng---|
        ok=150 (always true), ng=-1 (impossible)

    Example 4: Age < 23 → use NOT condition!
        Original:  T ... T  F ... F
        Negated:   F ... F  T ... T
                   |-ng-| |-ok-|
        """,
        "Think about CONDITION, not position!",
        "Use abs(ok - ng) > 1 to handle both directions"
    )

    # Pattern 5: Common Mistakes
    print_pattern(
        "5. Common Mistakes & How to Avoid",
        """
    ❌ Mistake 1: Using left/right for duplicates
       nums = [1,3,3,4,4,4], find first 4
       → left/right might return any 4
       ✓ Use lower_bound with ok/ng

    ❌ Mistake 2: Off-by-one errors
       while ok < ng:  # Wrong! Infinite loop possible
       ✓ while abs(ok - ng) > 1:

    ❌ Mistake 3: Not handling edge cases
       nums = [1,2,3], target = 0 or 10
       → Can't initialize ok or ng!
       ✓ Check range first, handle nums[0] specially

    ❌ Mistake 4: Wrong condition
       Want: first occurrence
       Used: nums[i] > target  # Wrong direction!
       ✓ Use: nums[i] >= target

    ❌ Mistake 5: Returning ng when answer should be ok
       ✓ NEGATE the condition to put answer in ok
        """,
        "Most bugs come from boundary conditions!",
        "Always test: empty, single element, not found, duplicates"
    )

    # Pattern 6: Decision Tree
    print_pattern(
        "6. Which Pattern Should I Use?",
        """
    START: I need to search a sorted sequence
      |
      ├─ Values are UNIQUE?
      │    └─ Yes → Use basic binary search (left/right is fine)
      │         Example: [1,3,5,7,9], find 5
      │
      └─ Values have DUPLICATES or need boundary?
           |
           ├─ Need FIRST occurrence (leftmost)?
           │    └─ Use LOWER BOUND
           │         Condition: nums[i] >= target
           │         ok=N-1, ng=0
           │         Example: [1,3,3,4,4,4], find first 4
           │
           └─ Need LAST occurrence (rightmost)?
                └─ Use UPPER BOUND
                     Condition: nums[i] <= target
                     ok=0, ng=N-1
                     Example: [1,3,3,4,4,4], find last 4

    REMEMBER: The pattern is about WHAT boundary you need,
              not about the data structure!
        """,
        "Choose based on what boundary you're finding",
        "ok/ng pattern works for ANY monotonic condition"
    )


def interactive_demo():
    """Interactive demonstration of binary search"""
    print("\n" + "="*70)
    print(" INTERACTIVE DEMO ".center(70))
    print("="*70)

    nums = [1, 3, 3, 4, 4, 4, 4, 4, 19]
    target = 4

    print(f"\nArray: {nums}")
    print(f"Target: {target}")

    # Lower bound demo
    print("\n--- LOWER BOUND (First 4) ---")
    print("Condition: nums[i] >= 4")
    ok, ng = len(nums) - 1, 0
    step = 1

    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        print(f"Step {step}: ok={ok}, ng={ng}, mid={mid}, nums[mid]={nums[mid]}")

        if nums[mid] >= target:
            print(f"  → {nums[mid]} >= {target}, set ok={mid}")
            ok = mid
        else:
            print(f"  → {nums[mid]} < {target}, set ng={mid}")
            ng = mid
        step += 1

    print(f"Final: ok={ok}, ng={ng}")
    print(f"Answer: index {ok} (nums[{ok}] = {nums[ok]})")

    # Upper bound demo
    print("\n--- UPPER BOUND (Last 4) ---")
    print("Condition: nums[i] <= 4")
    ok, ng = 0, len(nums) - 1
    step = 1

    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        print(f"Step {step}: ok={ok}, ng={ng}, mid={mid}, nums[mid]={nums[mid]}")

        if nums[mid] <= target:
            print(f"  → {nums[mid]} <= {target}, set ok={mid}")
            ok = mid
        else:
            print(f"  → {nums[mid]} > {target}, set ng={mid}")
            ng = mid
        step += 1

    print(f"Final: ok={ok}, ng={ng}")
    print(f"Answer: index {ok} (nums[{ok}] = {nums[ok]})")


def main():
    """Run all visualizations"""
    visualize_all_patterns()
    interactive_demo()

    print("\n" + "="*70)
    print(" KEY TAKEAWAYS ".center(70))
    print("="*70)
    print("""
    1. Binary search finds BOUNDARIES, not just values
    2. Use ok/ng to track condition satisfaction
    3. Think: "What condition creates the right boundary?"
    4. Lower bound: first True  (condition: >=)
    5. Upper bound: last True   (condition: <=)
    6. Always handle edge cases: empty, start, end
    7. Use abs(ok - ng) > 1 for flexibility
    8. NEGATE condition if answer ends up in ng
    """)


if __name__ == "__main__":
    main()
