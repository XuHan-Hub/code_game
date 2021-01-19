from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort
        n = len(nums)

        i = 0
        j =  n - 1
        count = 0

        while i < j:
            if nums[i] + nums[j] == k:
                count+=1
                j-=1
            elif nums[i] + nums[j] > k:
                j-=1
            else:
                i+=1
        return count






        # nums_link = [i for i in range(1, n+1)]
        # count,i=0,0
        # while i <n:
        #     count1 = 1
        #     count2 = 0
        #     tmp = k-nums[i]
        #     j = nums_link[i]
        #     pp=i
        #     while j<n:
        #         if nums[i]==nums[j]:
        #             nums_link[pp] = nums_link[j]
        #             count1+=1
        #         elif nums[j] == tmp:
        #             nums_link[pp] = nums_link[j]
        #             count2 += 1
        #             if count1 ==1:
        #                 break
        #
        #         else:
        #             pp=j
        #         j = nums_link[j]
        #     if k/2==nums[i]:
        #         count+=count1//2
        #         # print(count1//2)
        #     else:
        #         count += min(count2,count1)
        #         # print(count2,count1)
        #     i = nums_link[i]
        # return count



if __name__ == '__main__':
    s = Solution()
   




    # nums = [3,1,2,3,4,2,2,5]
    print(s.maxOperations(nums, 114552585 ))