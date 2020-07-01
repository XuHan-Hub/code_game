import string as str
# A sliding window
# hint 只需要考虑单字符

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        if N ==0:
            return 0
        ans,i,j =  1, 0,1

        while j<N:
            tmp = s[i:j].find(s[j])
            if tmp >=0 :
                ans = max(ans, j - i)
                i=i+tmp+1
            j += 1
        return max(ans, j - i)

if __name__ == '__main__':
    s = Solution()
    str = "abcabcbb"
    print(str.find("abc"))
    print(s.lengthOfLongestSubstring(str))
