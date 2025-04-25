# дано (веса графа)
graph = {}
graph["start"] = {}
graph["start"]["пластинка"] = 5
graph["start"]["постер"] = 0
graph["пластинка"] = {}
graph["пластинка"]["гитара"] = 15
graph["пластинка"]["барабан"] = 20
graph["постер"] = {}
graph["постер"]["гитара"] = 30
graph["постер"]["барабан"] = 35
graph["гитара"] = {}
graph["гитара"]["пианино"] = 20
graph["барабан"] = {}
graph["барабан"]["пианино"] = 10
graph["пианино"] = {}

# изменения стоимости узлов
costs = {}
costs['пластинка'] = 5
costs['постер'] = 0
costs['гитара'] = float('inf')
costs['барабан'] = float('inf')
costs['пианино'] = float('inf')

# родительский граф
parents = {}
parents['пластинка'] = "start"
parents['постер'] = "start"
parents['гитара'] = None
parents['барабан'] = None
parents['пианино'] = None

# список для просмотренных узлов
processed = []

goal = "пианино"

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

# восстанавливаем путь по словарю
def find_path(parents, key, result=[]):
    result.append(key)
    if key == 'start': return result
    else:
        return find_path(parents, parents[key], result)

print(find_path(parents, goal))