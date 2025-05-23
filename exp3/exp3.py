
import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan distance

def astar(grid, start, goal):
    open_set = [(0 + heuristic(start, goal), start)]
    g_score = {start: 0}
    came_from = {}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            neighbor = (current[0] + dx, current[1] + dy)

            if (
                0 <= neighbor[0] < len(grid) and
                0 <= neighbor[1] < len(grid[0]) and
                grid[neighbor[0]][neighbor[1]] == 0
            ):
                tentative_g = g_score[current] + 1

                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    heapq.heappush(open_set, (
                        tentative_g + heuristic(neighbor, goal),
                        neighbor
                    ))

    return None

# Define the grid (0 = walkable, 1 = obstacle)
grid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]

start = (0, 0)
goal = (2, 2)

path = astar(grid, start, goal)

if path:
    print("Path found:", path)
else:
    print("No path found.")
