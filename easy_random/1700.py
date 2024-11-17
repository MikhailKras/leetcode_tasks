class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students, sandwiches = deque(students), deque(sandwiches)
        misses = 0
        while students and sandwiches:
            student = students.popleft()
            sandwich = sandwiches[0]
            if student == sandwich:
                misses = 0
                sandwiches.popleft()
            else:
                students.append(student)
                misses += 1
                if misses > len(students):
                    return len(students)
        return len(students)

