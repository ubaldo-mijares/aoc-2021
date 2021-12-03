# ingest the list of items
with open('Ubaldo/problem2.txt') as txt:
    puzzle_input = txt.read().splitlines()

# create 2 counters
horizonal_pos = 0
depth = 0

# iterate through all items and increment the counters based on the plan
for index, item in enumerate(puzzle_input):

    # split the item between direction and units
    direction, units = item.split(" ")

    # update the horizonal position
    if direction == 'forward':

        horizonal_pos += int(units)
        continue

    # update depth
    elif direction == 'up':

        depth -= int(units)
        continue

    else:

        depth += int(units)
        continue

print(f'The horizontal position multiplied by final depth is: {horizonal_pos * depth}')