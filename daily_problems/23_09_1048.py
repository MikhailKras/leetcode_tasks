from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def is_pred(parent, child):
            l1, l2 = 0, 0
            counter = 0
            while l1 < len(parent) and l2 < len(child):
                if parent[l1] != child[l2]:
                    counter += 1
                    if counter > 1:
                        return False
                else:
                    l1 += 1
                l2 += 1
            return True

        len_counter = {}
        for word in words:
            n = len(word)
            if n not in len_counter:
                len_counter[n] = [word]
            else:
                len_counter[n].append(word)

        memo = {}
        for start in sorted(words, key=lambda x: len(x)):
            if start in memo:
                continue
            memo[start] = 1
            stack = [start]
            while stack:
                cur_node = stack.pop()
                for neighbor in len_counter.get(len(cur_node) + 1, []):
                    if is_pred(cur_node, neighbor) and neighbor not in memo:
                        stack.append(neighbor)
                        memo[neighbor] = memo[cur_node] + 1
        return max(memo.values())
