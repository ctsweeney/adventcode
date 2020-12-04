#!/usr/bin/env python3
def read_map_file(filename: str):
    """Used to open the password file and pass back the contents

    Args:
        filename (str): filepath/filename of password file

    Returns:
        list: returns list of passwords to process
    """
    try:
        with open(filename, "r") as f:
            contents = f.read()
        return contents
    except FileNotFoundError:
        print("File %s not found" % filename)


MAP = read_map_file('map.txt')
treemap = MAP.split("\n")

map_width = len(treemap[0])
map_height = len(treemap)

pos = [0, 0]

trees = 0

while pos[0] < map_height:
    trees += treemap[pos[0]][pos[1]] == "#"
    pos[1] = (pos[1] + 3) % map_width
    pos[0] += 1

print(trees)
