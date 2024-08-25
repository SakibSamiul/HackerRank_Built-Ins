N, X = map(int, input().split())
marks = [list(map(float, input().split())) for _ in range(X)]
averageScore = [sum(Student_marks) / X for Student_marks in zip(*marks)]

for mark in averageScore:
    print(f"{mark:.1f}")