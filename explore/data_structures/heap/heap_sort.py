from typing import List


class MaxHeap:
    """
    最大ヒープ（MaxHeap）の実装

    ヒープ性質：
    - 完全二分木構造を配列で表現
    - 各ノードは子ノード以上の値を持つ（最大ヒープ性質）
    - ルート（インデックス0）が最大値

    配列表現のインデックス関係：
    - 親ノード: (i-1)//2
    - 左の子: 2*i+1
    - 右の子: 2*i+2
    """

    @staticmethod
    def parent(i: int) -> int:
        """
        指定インデックスの親ノードのインデックスを取得

        Args:
            i: 子ノードのインデックス

        Returns:
            親ノードのインデックス

        例: i=3の親は(3-1)//2 = 1
        """
        return (i - 1) // 2

    @staticmethod
    def left_child(i: int) -> int:
        """
        指定インデックスの左の子ノードのインデックスを取得

        Args:
            i: 親ノードのインデックス

        Returns:
            左の子ノードのインデックス

        例: i=1の左の子は2*1+1 = 3
        """
        return 2 * i + 1

    @staticmethod
    def right_child(i: int) -> int:
        """
        指定インデックスの右の子ノードのインデックスを取得

        Args:
            i: 親ノードのインデックス

        Returns:
            右の子ノードのインデックス

        例: i=1の右の子は2*1+2 = 4
        """
        return 2 * i + 2

    @staticmethod
    def push(heap: List[int], value: int) -> None:
        """
        ヒープに新しい値を挿入

        アルゴリズム：
        1. 配列末尾に新しい値を追加（完全二分木の性質を保つ）
        2. bubble_upで親と比較しながら適切な位置まで上昇

        Args:
            heap: ヒープを表す配列
            value: 挿入する値

        時間計算量: O(log n) - ヒープの高さ分の比較
        空間計算量: O(1)
        """
        heap.append(value)  # まず末尾に追加
        MaxHeap._bubble_up(heap, len(heap) - 1)  # ヒープ性質を回復

    @staticmethod
    def pop(heap: List[int]) -> int:
        """
        ヒープから最大値（ルート）を取り出す

        アルゴリズム：
        1. ルート（最大値）を保存
        2. 末尾要素をルートに移動（完全二分木を保つ）
        3. sift_downで適切な位置まで下降

        Args:
            heap: ヒープを表す配列

        Returns:
            取り出した最大値

        Raises:
            IndexError: 空のヒープからpopしようとした場合

        時間計算量: O(log n)
        空間計算量: O(1)
        """
        if not heap:
            raise IndexError("pop from empty heap")

        max_val = heap[0]  # 最大値（ルート）を保存

        if len(heap) == 1:
            heap.pop()  # 最後の要素なら単純に削除
        else:
            # 末尾要素をルートに移動してから削除
            heap[0] = heap.pop()
            # ヒープ性質を回復
            MaxHeap._sift_down(heap, 0, len(heap))

        return max_val

    @staticmethod
    def heapify(arr: List[int]) -> None:
        """
        任意の配列を最大ヒープに変換（in-place）

        アルゴリズム（ボトムアップ方式）：
        1. 最後の非葉ノード（n//2-1）から開始
        2. 各ノードに対してsift_downを実行
        3. ルートまで順次処理

        効率性の理由：
        - 葉ノード（配列の後半）は既にヒープ性質を満たす
        - 下層ほどノード数が多いが、sift_downの作業量は少ない

        Args:
            arr: ヒープ化する配列

        時間計算量: O(n) - 数学的に証明可能
        空間計算量: O(1) - in-place変換
        """
        # 最後の非葉ノードから逆順に処理
        # n//2-1は最後の葉ノードの親
        for i in range(len(arr) // 2 - 1, -1, -1):
            MaxHeap._sift_down(arr, i, len(arr))

    @staticmethod
    def _bubble_up(heap: List[int], idx: int) -> None:
        """
        指定インデックスの要素を親と比較しながら上昇させる

        ヒープ性質の回復：
        - 子が親より大きければ交換
        - 交換後、さらに上の親と比較を続ける
        - 親以下になるか、ルートに達したら停止

        Args:
            heap: ヒープを表す配列
            idx: 上昇させる要素のインデックス

        実装の意図：
        - whileループで再帰を回避（スタックオーバーフロー防止）
        - インデックス0（ルート）まで到達可能
        """
        while idx > 0:
            parent_idx = MaxHeap.parent(idx)

            # 親より大きければ交換
            if heap[idx] > heap[parent_idx]:
                heap[idx], heap[parent_idx] = heap[parent_idx], heap[idx]
                idx = parent_idx  # 親の位置から続行
            else:
                break  # ヒープ性質が満たされたら終了

    @staticmethod
    def _sift_down(arr: List[int], idx: int, size: int) -> None:
        """
        指定インデックスの要素を子と比較しながら下降させる

        アルゴリズム：
        1. 現在ノード、左の子、右の子の中で最大を見つける
        2. 最大が現在ノードでなければ交換
        3. 交換後、新しい位置から続行
        4. 葉ノードに達するか、ヒープ性質が満たされたら停止

        Args:
            arr: ヒープを表す配列
            idx: 下降させる要素のインデックス
            size: 処理対象のヒープサイズ（heap_sortで部分的に使用）

        実装の意図：
        - sizeパラメータでheap_sortの部分配列処理をサポート
        - 3要素（親、左の子、右の子）の最大値を効率的に特定
        - 無限ループ + break で再帰を回避
        """
        while True:
            left = MaxHeap.left_child(idx)
            right = MaxHeap.right_child(idx)
            largest = idx  # 最大値のインデックスを追跡

            # 左の子が存在し、現在の最大より大きいか確認
            if left < size and arr[left] > arr[largest]:
                largest = left

            # 右の子が存在し、現在の最大より大きいか確認
            if right < size and arr[right] > arr[largest]:
                largest = right

            # 現在ノードが最大ならヒープ性質を満たす
            if largest == idx:
                break

            # 最大の子と交換して続行
            arr[idx], arr[largest] = arr[largest], arr[idx]
            idx = largest


def heap_sort(arr: List[int]) -> None:
    """
    ヒープソートアルゴリズムでin-placeソート

    アルゴリズムの2段階：
    1. Build Phase: 配列全体を最大ヒープに変換
    2. Extract Phase: 最大値を順次取り出して後方に配置

    動作原理：
    - 最大ヒープの性質を利用（ルートが常に最大）
    - ルートと末尾を交換→ヒープサイズを縮小→sift_down
    - これを繰り返すことで昇順にソート

    Args:
        arr: ソートする配列（in-place変更）

    時間計算量: O(n log n)
        - heapify: O(n)
        - n-1回のsift_down: O(n log n)
    空間計算量: O(1) - in-placeアルゴリズム

    実装の意図：
    - 安定性は保証されない（同じ値の順序が変わる可能性）
    - 最悪時でもO(n log n)を保証（クイックソートより予測可能）
    - キャッシュ効率は良くない（離れた要素を頻繁に交換）
    """
    # エッジケース：要素が1個以下なら既にソート済み
    if len(arr) <= 1:
        return

    # Phase 1: 配列全体を最大ヒープに変換
    MaxHeap.heapify(arr)

    # Phase 2: 最大値を順次取り出して配列後方に配置
    for i in range(len(arr) - 1, 0, -1):
        # 現在の最大値（ルート）を配列の未ソート部分の末尾と交換
        arr[0], arr[i] = arr[i], arr[0]
        # 新しいルートをsift_downで適切な位置へ
        # サイズをiに制限することで、ソート済み部分を保護
        MaxHeap._sift_down(arr, 0, i)


def _verify_heap(heap: List[int]) -> None:
    """
    最大ヒープ性質を検証する内部テスト用関数

    検証内容：
    - 各非葉ノードが子ノード以上の値を持つことを確認
    - assertionエラーでヒープ性質違反を検出

    Args:
        heap: 検証するヒープ配列

    実装の意図：
    - テスト中にヒープ操作の正当性を保証
    - push/pop操作後の整合性チェック
    - デバッグとテストの信頼性向上
    """
    for i in range(len(heap) // 2):  # 非葉ノードのみチェック
        left = MaxHeap.left_child(i)
        right = MaxHeap.right_child(i)
        # 左の子が存在する場合、親以下であることを確認
        assert left >= len(heap) or heap[i] >= heap[left]
        # 右の子が存在する場合、親以下であることを確認
        assert right >= len(heap) or heap[i] >= heap[right]


def test_heap_operations():
    """
    MaxHeapクラスの各操作を包括的にテスト

    テスト項目：
    1. push/pop操作の正当性
    2. heapify関数の動作
    3. エッジケース（空のヒープからのpop等）
    4. 単一要素の処理

    実装の意図：
    - 各操作後にヒープ性質を検証
    - 降順での要素取り出しを確認
    - エラーハンドリングの動作確認
    """
    print("\n=== Testing MaxHeap ===")

    # Test 1: push操作とpop操作の連携テスト
    heap = []
    values = [3, 1, 4, 1, 5, 9, 2, 6]

    # 各値をpushし、毎回ヒープ性質を検証
    for val in values:
        MaxHeap.push(heap, val)
        _verify_heap(heap)  # 各push後の整合性確認

    # 全要素をpopし、降順で取り出されることを確認
    popped = []
    while heap:
        popped.append(MaxHeap.pop(heap))
        _verify_heap(heap)  # 各pop後の整合性確認

    # 最大ヒープから降順で取り出されたことを検証
    assert popped == sorted(values, reverse=True)

    # Test 2: heapify関数のテスト
    arr = [1, 5, 8, 0, 2, 6, 3, 9, 10, 4, 7, 11]
    MaxHeap.heapify(arr)
    _verify_heap(arr)  # heapify後のヒープ性質確認

    # Test 3: エッジケース - 空のヒープからのpop
    try:
        MaxHeap.pop([])
        assert False  # エラーが発生しなければテスト失敗
    except IndexError:
        pass  # 期待通りのエラー

    # Test 4: 単一要素の処理
    heap = []
    MaxHeap.push(heap, 42)
    assert MaxHeap.pop(heap) == 42
    assert heap == []  # popで空になることを確認

    print("✓ All heap tests passed")


def test_heap_sort():
    """
    ヒープソートの網羅的なテスト

    テストケース：
    1. ランダムな配列
    2. 重複要素を含む配列
    3. エッジケース（空、単一要素、2要素）
    4. 既にソート済み/逆順の配列
    5. 全要素が同じ配列
    6. 負の数を含む配列
    7. 大規模配列（100要素）

    実装の意図：
    - 様々なパターンで正確性を検証
    - エッジケースでの堅牢性確認
    - パフォーマンスの安定性確認
    """
    print("\n=== Testing Heap Sort ===")

    test_cases = [
        ([7, 3, 2, 5, 6, 10, 9, 8, 1], "random"),
        ([3, 1, 4, 1, 5, 9, 2, 6, 5], "duplicates"),
        ([], "empty"),  # エッジケース：空配列
        ([42], "single"),  # エッジケース：単一要素
        ([2, 1], "two elements"),  # エッジケース：2要素
        ([1, 2, 3, 4, 5], "sorted"),  # 既にソート済み
        ([5, 4, 3, 2, 1], "reverse"),  # 逆順
        ([7, 7, 7, 7], "all same"),  # 全要素同じ
        ([-3, 0, 2, -1, 5, -2], "negative"),  # 負の数を含む
        (list(range(100, 0, -1)), "large")  # 大規模テスト
    ]

    for arr, desc in test_cases:
        original = arr.copy()  # 元の配列を保存（デバッグ用）
        expected = sorted(arr)  # 期待される結果
        heap_sort(arr)
        # 結果が正しいことを検証
        assert arr == expected, f"{desc}: Expected {expected}, got {arr}"

    print("✓ All sort tests passed")


def main():
    """
    メインエントリーポイント：全テストを実行

    実行順序：
    1. ヒープ操作の基本機能テスト
    2. ヒープソートアルゴリズムの包括的テスト

    実装の意図：
    - すべてのテストが通過することで実装の正確性を保証
    - エラーメッセージで失敗箇所を特定しやすくする
    """
    test_heap_operations()
    test_heap_sort()


if __name__ == "__main__":
    main()
