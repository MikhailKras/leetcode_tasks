class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def construct(cur, wordDict, memo={}):
            if cur in memo:
                return memo[cur]

            if not cur:
                return True

            for word in wordDict:
                if cur.startswith(word):
                    new_current = cur[len(word):]
                    memo[cur] = True
                    if construct(new_current, wordDict, memo):
                        return True

            memo[cur] = False
            return False

        return construct(s, set(wordDict))
