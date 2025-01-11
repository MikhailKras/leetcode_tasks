class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"

        counter = {}
        for rank in ranks:
            counter[rank] = counter.get(rank, 0) + 1
            if counter[rank] == 3:
                return "Three of a Kind"
        else:
            if 2 in counter.values():
                return "Pair"
                
        return "High Card"

