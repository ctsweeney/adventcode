#!/usr/bin/env python3
def read_map_file(filename: str):
    """Used to read the map data passed

    Args:
        filename (str): filepath/filename of password file

    Returns:
        list: returns contents of map file to process
    """
    try:
        with open(filename, "r") as f:
            # Return list of passwords to perform password logic on
            contents = f.read()
        return contents
    except FileNotFoundError:
        print("File %s not found" % filename)


MAP = read_map_file('map.txt')
tmap = MAP.split("\n")

width = len(tmap[0])
height = len(tmap)


def count_trees(xslope: int, yslope: int) -> int:
    """Work out the number of trees from the x and y movements passed

    Args:
        xslope (int): The amount to move the sleigh on the x axis
        yslope (int): The amount to move the sleigh on the y axis

    Returns:
        int: The amount of trees encountered on this slope run
    """
    pos = [0, 0]
    trees = 0

    while pos[0] < height:
        trees += tmap[pos[0]][pos[1]] == "#"
        pos[1] = (pos[1] + xslope) % width
        pos[0] += yslope

    return trees


# Define our sleigh movements as list of tuples
slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]

# Initialise our product to multiply by our returned trees
prod = 1

# Loop through our slopes
for xslope, yslope in slopes:
    prod *= count_trees(xslope, yslope)

# Print the product of all the trees for all slope runs
print(prod)
