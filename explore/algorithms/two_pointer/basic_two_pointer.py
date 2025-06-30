"""
Two Pointer Pattern: 基本的なテクニック集

Two pointerは2つのポインタを使って配列や文字列を効率的に走査するテクニックです。
主に以下のパターンがあります：
1. 対向型（両端から中央へ）
2. 同方向型（両方が同じ方向へ）
3. スライディングウィンドウ型
"""


def two_sum_sorted(nums: list[int], target: int) -> list[int]:
    """
    ソート済み配列でのTwo Sum問題
    
    Time: O(n), Space: O(1)
    
    Args:
        nums: ソート済み配列
        target: 目標値
    
    Returns:
        合計がtargetになる2つのインデックス（1-indexed）
    """
    left, right = 0, len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        
        if current_sum == target:
            return [left + 1, right + 1]  # 1-indexed
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []


def remove_duplicates(nums: list[int]) -> int:
    """
    ソート済み配列から重複を除去（インプレース）
    
    Time: O(n), Space: O(1)
    
    Returns:
        重複除去後の要素数
    """
    if not nums:
        return 0
    
    # slow pointerは次にユニークな要素を配置する位置
    slow = 1
    
    # fast pointerは配列を走査
    for fast in range(1, len(nums)):
        if nums[fast] != nums[fast - 1]:
            nums[slow] = nums[fast]
            slow += 1
    
    return slow


def move_zeros(nums: list[int]) -> None:
    """
    配列内の0を全て末尾に移動（順序保持）
    
    Time: O(n), Space: O(1)
    """
    # slow pointerは次に非ゼロ要素を配置する位置
    slow = 0
    
    # fast pointerで非ゼロ要素を探す
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1


def container_with_most_water(heights: list[int]) -> int:
    """
    最大の水を保持できるコンテナを見つける
    
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(heights) - 1
    max_area = 0
    
    while left < right:
        # 現在の面積を計算
        width = right - left
        height = min(heights[left], heights[right])
        area = width * height
        max_area = max(max_area, area)
        
        # より低い側のポインタを移動
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    
    return max_area


def three_sum(nums: list[int]) -> list[list[int]]:
    """
    配列から合計が0になる3つの数の組み合わせを全て見つける
    
    Time: O(n²), Space: O(1) - 出力を除く
    """
    nums.sort()
    result = []
    n = len(nums)
    
    for i in range(n - 2):
        # 重複をスキップ
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Two pointerで残りの2つを探す
        left, right = i + 1, n - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # 重複をスキップ
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return result


def is_subsequence(s: str, t: str) -> bool:
    """
    sがtの部分列かどうかを判定
    
    Time: O(n), Space: O(1)
    """
    if not s:
        return True
    
    s_pointer = 0
    
    for char in t:
        if char == s[s_pointer]:
            s_pointer += 1
            if s_pointer == len(s):
                return True
    
    return False


# 使用例とテスト
if __name__ == "__main__":
    # Two Sum (ソート済み)
    print(f"Two Sum [2,7,11,15], target=9: {two_sum_sorted([2,7,11,15], 9)}")
    
    # 重複除去
    nums = [0,0,1,1,1,2,2,3,3,4]
    length = remove_duplicates(nums)
    print(f"Remove duplicates: {nums[:length]}")
    
    # ゼロの移動
    nums = [0,1,0,3,12]
    move_zeros(nums)
    print(f"Move zeros: {nums}")
    
    # 最大水量
    heights = [1,8,6,2,5,4,8,3,7]
    print(f"Max water area: {container_with_most_water(heights)}")
    
    # 3Sum
    nums = [-1,0,1,2,-1,-4]
    print(f"3Sum: {three_sum(nums)}")
    
    # 部分列判定
    print(f"Is 'ace' subsequence of 'aec'? {is_subsequence('ace', 'aec')}")