class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        candidates = list(filter(lambda x: x <= target, candidates))
        res = []

        def helper(cur_arr, i, cur_sum):
            if cur_sum == target:
                res.append(cur_arr)
            for j in range(i, len(candidates)):
                new_sum = cur_sum + candidates[j]
                if new_sum <= target:
                    helper(cur_arr + [candidates[j]], j, new_sum)
        
        helper([], 0, 0)
        return res

