n = int(input("Введите количество отрезков: "))
segments = []
points=[]
print("Введите отрезки в формате: левый_конец правый_конец")
for _ in range(n):
    left, right = map(int, input().split())
    segments.append((left, right))
for segment in segments:
    covered = False
    for point in points:
        if segment[0] <= point <= segment[1]:
            covered = True
            break
    if not covered:
        points.append(segment[1])

print("Минимальное количество точек:", len(points))
