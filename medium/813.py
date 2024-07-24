class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        
        @lru_cache(None)
        def helper(i, count_k):

            if count_k == 1:
                return sum(nums[i:]) / len(nums[i:])

            max_avg = 0
            cur_sum = nums[i]
            cur_len = 1
            for j in range(i + 1, len(nums)):
                avg = cur_sum / cur_len
                cur_sum += nums[j]
                cur_len += 1

                subarray_avg = avg + helper(j, count_k - 1)

                max_avg = max(max_avg, subarray_avg)

            return max_avg

        return helper(0, k)
        
