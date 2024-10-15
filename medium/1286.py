class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = sorted(characters)
        self.combinationLength = combinationLength
        self.combinations = self.__get_combinations()

    def __get_combinations(self) -> List[str]:
        res = deque([])
        def helper(cur: str, start: int):
            print(cur, start)
            if len(cur) == self.combinationLength:
                res.append(cur)
                return
            for j in range(start, len(self.characters)):
                helper(cur + [self.characters[j]], j + 1)
        helper([], 0)
        return res
        

    def next(self) -> str:
        if self.combinations:
            return ''.join(self.combinations.popleft())

    def hasNext(self) -> bool:
        return bool(self.combinations)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
