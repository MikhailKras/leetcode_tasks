class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
        seen = {}
        for i in range(len(s)):
            if s[i] in vowels:
                if s[i] not in seen:
                    seen[s[i]] = [i]
                else:
                    seen[s[i]].append(i)
        
        vowels_ids = []
        queue = deque()
        for key, value in sorted(seen.items(), key=lambda x: ord(x[0])):
            vowels_ids.extend(value)
            queue.extend(deque([key] * len(value)))
        s = list(s)
        for i in sorted(vowels_ids):
            s[i] = queue.popleft()
        return ''.join(s)

