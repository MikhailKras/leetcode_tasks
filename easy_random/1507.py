class Solution:
    def reformatDate(self, date: str) -> str:
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        date_list = date.split()
        day = '0' + date_list[0][:1] if len(date_list[0]) == 3 else date_list[0][:2]
        month = str(months.index(date_list[1]) + 1)
        month = '0' + month if len(month) == 1 else month
        return f"{date_list[2]}-{month}-{day}"

