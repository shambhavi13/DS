# Traversing a graph
def bfs_connected_component(graph, start):

    explored = []
    queue = [start]
    while queue:
        # pop first node from queue
        node = queue.pop(0)
        if node not in explored:
            # add to the list of visited node
            explored.append(node)
            # get the neighbours
            neighbours = graph[node]
            for neighbour in neighbours:
                # add to queue
                queue.append(neighbour)
    return explored

# find shortest distance from one node to another

def bfs_shortest_path(graph, start, end):

    explored = []
    queue = [[start]]  # queue = [['G']]
    while queue:
        path = queue.pop(0)  # path = [G]
        node = path[-1]  # node = G
        if node not in explored:
            neighbours = graph[node] # neighbour = [C]
            for neighbour in neighbours:
                new_path = list(path) # new_path = [G]
                new_path.append(neighbour)  # new_path = [G,C]
                queue.append(new_path)  # queue = [[G,C]]
                if neighbour == end:
                    return new_path
            explored.append(node)
    return "No connected path found"

if __name__== "__main__":

    graph = {'A': ['B', 'C', 'E'],
             'B': ['A', 'D', 'E'],
             'C': ['A', 'F', 'G'],
             'D': ['B'],
             'E': ['A', 'B', 'D'],
             'F': ['C'],
             'G': ['C']}
    print(bfs_connected_component(graph, 'A'))
    print(bfs_shortest_path(graph, 'G', 'D'))