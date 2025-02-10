def main():
    args = [[1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3]
    solution = Solution()
    result = solution.merge(*args)
    print(result)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Brute force
        # for i in range(n):
        #     nums1[i+m] = nums2[i]
        
        # nums1.sort()

        # three pointer
        nums1Copy = nums1[:m]
        p1 = 0
        p2 = 0

        for p in range(m+n):
            print(p1, p2)
            if p1 >= m or (p2 < n and nums1Copy[p1] > nums2[p2]):
                nums1[p] = nums2[p2]
                p2 += 1
            else:
                nums1[p] = nums1Copy[p1]
                p1 += 1
            p += 1

        
if __name__ == '__main__':
    main()