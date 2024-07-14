class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cur_seq = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > cur_seq[-1]:
                cur_seq.append(nums[i])
            else:
                l, r = 0, len(cur_seq) - 1
                while l < r:
                    mid = (l + r) // 2
                    if cur_seq[mid] > nums[i]:
                        r = mid
                    elif cur_seq[mid] < nums[i]:
                        l = mid + 1
                    else:
                        cur_seq[mid] = nums[i]
                        break
                else:
                    cur_seq[l] = nums[i]
        return len(cur_seq)

