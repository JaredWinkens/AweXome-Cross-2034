import time


def main():
    def parse_input():
    N = int(input().strip())
    grid = [input().strip() for _ in range(N)]
    return N, grid

def count_colors(grid):
    from collections import Counter
    counts = Counter(c for row in grid for c in row if c.isdigit())
    return counts

def flood_fill(grid, visited, x, y, color):
    # BFS/DFS to calculate the size of a component or mark it
    pass

def count_buildings(grid):
    # Use flood_fill to count connected components of each color
    pass

def find_courtyards(grid):
    # Identify and count fully enclosed empty spaces
    pass

def tallest_building(grid):
    # Simulate the cube stacking logic
    pass

def main():
    N, grid = parse_input()
    
    # Solve each problem
    most_common_color = count_colors(grid)
    num_buildings = count_buildings(grid)
    num_courtyards = find_courtyards(grid)
    # Add other solutions here

    # Print results
    print(most_common_color)
    print(num_buildings)
    print(num_courtyards)
    # More results here

if name == "main":
    main()