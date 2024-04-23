class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        n = len(candidates)

        def helper(cur_arr, i, cur_sum):
            if cur_sum == target:
                res.append(cur_arr)
                return
            j = i
            while j < n and cur_sum + candidates[j] <= target:
                if j > i and candidates[j] == candidates[j - 1]:
                    j += 1
                    continue
                helper(cur_arr + [candidates[j]], j + 1, cur_sum + candidates[j])
                j += 1
        
        helper([], 0, 0)
        return res

