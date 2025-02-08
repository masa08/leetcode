def main():
    args = [[1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3]
    solution = Solution()
    result = solution.merge(*args)
    print(result)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[:] = sorted(nums1[:m] + nums2[:n])
        
if __name__ == '__main__':
    main()