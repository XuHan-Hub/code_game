class Solution:
    def longestPalindrome(self, s: str) -> str:
            n = len(s)
            res = s[0]
            max_len = 1
            for i in range(1,n):
                if s[i] == s[i-1]:
                    p1 = i-2
                    p2 = i+1
                    while p1>= 0 and p2< n:
                        if s[p1]!=s[p2]:
                            break
                        p1 -= 1
                        p2 += 1
                    if max_len < p2-p1-1:
                        max_len = p2-p1-1
                        res = s[p1+1:p2]
                if i < n-1 and s[i-1] == s[i + 1]:
                    p1 = i - 2
                    p2 = i + 2
                    while p1 >= 0 and p2< n:
                        if s[p1] != s[p2]:
                            break
                        p1 -= 1
                        p2 += 1
                    if max_len < p2 - p1 - 1:
                        max_len = p2 - p1 - 1
                        res = s[p1 + 1:p2]
            return res


if __name__ == '__main__':
    s = Solution()


    print(s.longestPalindrome('bb'))