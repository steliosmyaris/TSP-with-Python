import itertools

# function to calculate the distance between two points
def distance(city1, city2):
    return ((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2) ** 0.5

# backtracking function to find the shortest path
def tsp_backtracking(cities):
    # Generate all possible permutations of cities except the first one (to avoid equivalent cycles)
    permutations = itertools.permutations(cities[1:])
    min_path = None
    min_distance = float('inf')

    for perm in permutations:
        current_path = [cities[0]] + list(perm)
        current_distance = sum(distance(current_path[i], current_path[i+1]) for i in range(len(current_path) - 1))
        current_distance += distance(current_path[-1], cities[0])  # returning to the start city

        if current_distance < min_distance:
            min_distance = current_distance
            min_path = current_path

    return min_path, min_distance

# function to get coordinates from the user
def get_coordinates(num_cities):
    cities = []
    for i in range(num_cities):
        x, y = map(float, input(f"Enter coordinates for city {i+1} (format: x y): ").split())
        cities.append((x, y))
    return cities

def main():
    num_cities = 10
    cities = get_coordinates(num_cities)

    path, distance = tsp_backtracking(cities)

    print("The shortest path is:")
    for city in path:
        print(city)
    print(f"With a total distance of: {distance}")

if __name__ == "__main__":
    main()
