class Solution:
    def dayOfYear(self, date: str) -> int:
        num_days = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31,
        }
        date = date.split('-')
        year, month, day = int(date[0]), int(date[1]), int(date[2])
        res = 0
        for num in range(1, month):
            res += num_days[num]
        res += day

        if month > 2:
            if year % 4 == 0 and not (year % 100 == 0 and year % 400 != 0):
                res += 1

        return res

