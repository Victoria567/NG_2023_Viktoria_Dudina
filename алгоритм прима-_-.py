import heapq

# Алгоритм Прима для поиска минимального остовного дерева
def prim_mst(graph, start):
    # Инициализация
    key = {v: float('inf') for v in graph} # key[v] = бесконечность
    print(key)
    parent = {v: None for v in graph} # предок[v] = None
    print(parent)
    key[start] = 0 # key[r] = 0
    print(key)
    
    # Очередь с приоритетами (ключ - значение key[v])
    priority_queue = [(0, start)]  # (ключ, вершина)
    print('priority_queue - ', priority_queue)
    in_queue = set(graph.keys())   # Множество вершин, ещё в очереди
    print(in_queue)

    while priority_queue:
        # Вытягиваем вершину с минимальным ключом
        current_key, u = heapq.heappop(priority_queue)
        print(' current_key, u - ', current_key, u)
        
        if u not in in_queue:
            continue  # Если вершина уже обработана, пропустить
        
        in_queue.remove(u)  # Убираем вершину из очереди
        
        # Для каждой смежной вершины
        for v, weight in graph[u]:
            print(v, weight, 'Хуй знает чё')
            if v in in_queue and weight < key[v]:
                parent[v] = u       # Обновляем предка
                key[v] = weight     # Обновляем ключ
                heapq.heappush(priority_queue, (key[v], v))  # Переобновляем очередь
        
        print("В конце цикла", parent, key)        

    return parent, key

# Пример графа: список смежности
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 4)],
    'D': [('B', 1), ('C', 4)]
}

# Запуск
start_vertex = 'A'
parent, key = prim_mst(graph, start_vertex)

# Вывод результата
print("Минимальное остовное дерево:")
for vertex in graph:
    if parent[vertex] is not None:
        print(f"{parent[vertex]} - {vertex} (вес: {key[vertex]})")
