import sys
import os
import heapq

class Node:
    def __init__(self, x, y, cost, heuristic):
        self.x = x
        self.y = y
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def read_maze(file_path):
    maze = []
    with open(file_path, 'r') as file:
        for line in file:
            row = [int(cell) for cell in line.split()]
            maze.append(row)
    return maze

def heuristic(node, goal):
    return abs(node.x - goal[0]) + abs(node.y - goal[1])

def is_valid(x, y, maze):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0

def astar_search(maze, start, goal):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    start_node = Node(start[0], start[1], 0, heuristic(Node(start[0], start[1], 0, 0), goal))
    priority_queue = [start_node]
    visited = set()

    while priority_queue:
        current_node = heapq.heappop(priority_queue)

        if (current_node.x, current_node.y) == goal:
            return 'YES'

        visited.add((current_node.x, current_node.y))

        for dx, dy in directions:
            next_x, next_y = current_node.x + dx, current_node.y + dy

            if is_valid(next_x, next_y, maze) and (next_x, next_y) not in visited:
                next_node = Node(next_x, next_y, current_node.cost + 1, heuristic(Node(next_x, next_y, 0, 0), goal))
                heapq.heappush(priority_queue, next_node)

    return 'NO'

if __name__ == "__main__":
    MAZE_FILE_PATH = os.path.join('resources', 'maze.txt')

    if len(sys.argv) != 5:
        print("Usage: python script.py start_x start_y goal_x goal_y")
        sys.exit(1)

    start = (int(sys.argv[1]), int(sys.argv[2]))
    goal = (int(sys.argv[3]), int(sys.argv[4]))

    result = astar_search(read_maze(MAZE_FILE_PATH), start, goal)
    print(result)
