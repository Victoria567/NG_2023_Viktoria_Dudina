import math

# Вершины
vertices = ['A', 'B', 'C', 'D']
n = len(vertices)
print(n)

# Исходная матрица весов
W = [
    [0,     3,     math.inf, 7],
    [8,     0,     2,         math.inf],
    [5,     math.inf, 0,     1],
    [2,     math.inf, math.inf, 0]
]

# Функция алгоритма Флойда-Воршелла
def floyd_warshall(W):
    # Копируем матрицу W в D
    D = [line[:] for line in W]
    print (D)

    # Основной тройной цикл
    for k in range(n):
        print(f"\n--- Используем {vertices[k]} как промежуточную вершину ---")
        for i in range(n):
            for j in range(n):
                if D[i][j] > D[i][k] + D[k][j]:
                    print(f"Обновляем путь {vertices[i]} → {vertices[j]} через {vertices[k]}: {D[i][j]} → {D[i][k]} + {D[k][j]} = {D[i][k] + D[k][j]}")
                    D[i][j] = D[i][k] + D[k][j]

    return D

# Запуск алгоритма
distances = floyd_warshall(W)

# Вывод результата
print("\nКратчайшие расстояния между всеми парами вершин:")
for i in range(n):
    for j in range(n):
        dist = distances[i][j]
        if dist == math.inf:
            print(f"{vertices[i]} → {vertices[j]}: ∞")
        else:
            print(f"{vertices[i]} → {vertices[j]}: {dist}")
