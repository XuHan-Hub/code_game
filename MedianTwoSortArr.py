from typing import List




class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        end = (m+n)//2 + 1
        res = []
        p1, p2 = 0,0
        while p1+p2 != end:

            if p1<m and p2<n:
                if nums1[p1]<nums2[p2]:
                    res.append(nums1[p1])
                    p1+=1
                else:
                    res.append(nums2[p2])
                    p2+=1
            elif p1==m:
                res.append(nums2[p2])
                p2 += 1
            elif p2 ==n:
                res.append(nums1[p1])
                p1 += 1

        if (m+n)%2==0:
            return (res[-1]+res[-2])/2
        else:
            return res[-1]

if __name__ == '__main__':
    nums1 = [3]
    nums2 = [2,7]
    s = Solution()
    ans = s.findMedianSortedArrays(nums1,nums2)
    print(ans)