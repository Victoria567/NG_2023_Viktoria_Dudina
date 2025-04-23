edges = [
    ('A', 'B', 1),
    ('A', 'C', 4),
    ('B', 'C', -3),
    ('C', 'D', 2),
    ('D', 'B', 1)
]

vertices = ['A', 'B', 'C', 'D']

def initialize_single_source(start):
    d = {v: float('inf') for v in vertices}
    parent = {v: None for v in vertices}
    d[start] = 0
    print ("прошла функция initialize_single_source")
    return d, parent

def relax(u, v, w, d, parent):
    if d[u] + w < d[v]:
        print(1)
        old = d[v]
        d[v] = d[u] + w
        parent[v] = u
        print(f"Обновляем: {v} через {u}, старое расстояние = {old}, новое = {d[v]}")

def bellman_ford(edges, vertices, start):
    print ("Началась функция алгоритм")
    print ("Прошёл вызов функция initialize_single_source")
    d, parent = initialize_single_source(start)

    for i in range(len(vertices) - 1):
        print(f"\nИтерация {i + 1}")
        for u, v, w in edges:
            relax(u, v, w, d, parent)

    print("\nПроверка на отрицательный цикл:")
    for u, v, w in edges:
        if d[v] > d[u] + w:
            print("Найден цикл отрицательного веса!")
            return None, None

    return d, parent

# Запуск
print("запуск алгоритма")
distances, parents = bellman_ford(edges, vertices, 'A')

# Вывод результата
if distances:
    print("\nКратчайшие расстояния от A:")
    for v in vertices:
        print(f"{v}: {distances[v]} (через {parents[v]})")
