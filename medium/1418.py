class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        dct = {}
        all_foods = set()
        for name, table_num, food in orders:
            table_num = int(table_num)
            all_foods.add(food)
            if table_num not in dct:
                dct[table_num] = {food: 1}
            else:
                dct[table_num][food] = dct[table_num].get(food, 0) + 1
        all_foods = sorted(all_foods)
        res = [["Table", *all_foods]]
        for table_num in sorted(dct):
            foods = [str(dct[table_num].get(food, 0)) for food in all_foods]
            res.append([str(table_num), *foods])
        return res

