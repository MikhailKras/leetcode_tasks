class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        wait_time = 0
        cur_arrival = customers[0][0]
        for arrival, time in customers:
            if cur_arrival < arrival:
                cur_arrival = arrival
            wait_time += time + cur_arrival - arrival
            cur_arrival += time
        return round(wait_time / len(customers), 5)

