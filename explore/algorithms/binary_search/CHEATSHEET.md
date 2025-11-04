# 二分探索 Cheat Sheet

## 📊 3パターン比較

| パターン | 条件 | 初期化 | 用途 |
|---------|------|--------|------|
| Basic | `== target` | `left=0, right=N-1` | 値がユニーク |
| Lower Bound | `>= target` | `ok=N-1, ng=0` | 最初の出現 |
| Upper Bound | `<= target` | `ok=0, ng=N-1` | 最後の出現 |

## 💡 視覚イメージ

```text
nums = [1,3,3,4,4,4,4,4,19], target = 4

Lower (>=): F F F T T T T T T  → index 3 (最初)
Upper (<=): T T T T T T T T F  → index 7 (最後)
```

## 📝 テンプレート

### 1. Basic Search

```python
left, right = 0, len(nums) - 1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
return -1
```

### 2. Lower Bound（最頻出）

```python
N = len(nums)
if not (nums[0] <= target <= nums[N-1]):
    return -1
if nums[0] == target:
    return 0

ok, ng = N - 1, 0
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if nums[mid] >= target:
        ok = mid
    else:
        ng = mid
return ok if nums[ok] == target else -1
```

### 3. Upper Bound

```python
N = len(nums)
if not (nums[0] <= target <= nums[N-1]):
    return -1
if nums[N-1] == target:
    return N - 1

ok, ng = 0, N - 1
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if nums[mid] <= target:
        ok = mid
    else:
        ng = mid
return ok if nums[ok] == target else -1
```

## 🐛 よくあるバグ

| バグ | ❌ Wrong | ✅ Fix |
|------|----------|--------|
| 無限ループ | `while ok < ng:` | `while abs(ok - ng) > 1:` |
| 条件ミス | `if nums[mid] > target:` | `if nums[mid] >= target:` |
| 最後チェック忘れ | `return ok` | `return ok if nums[ok] == target else -1` |

## ✅ チェックリスト

- [ ] 条件は正しい？（`>=`, `<=`, `==`）
- [ ] ok/ng正しく初期化？
- [ ] エッジケース処理（範囲外、境界値）？
- [ ] `abs(ok - ng) > 1`使用？
- [ ] 最後に`nums[ok] == target`チェック？

---

詳細: [README.md](README.md) | 演習: [QUICKSTART.md](QUICKSTART.md)
