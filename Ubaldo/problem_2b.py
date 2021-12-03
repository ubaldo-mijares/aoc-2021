# ingest the list of items
with open('Ubaldo/problem2.txt') as txt:
    puzzle_input = txt.read().splitlines()

# create 3 counters
horizonal_pos = 0
depth = 0
aim = 0

# iterate through all items and increment the counters based on the plan
for index, item in enumerate(puzzle_input):

    # split the item between direction and units
    direction, units = item.split(" ")

    # update the horizonal position
    if direction == 'forward':

        horizonal_pos += int(units)
        depth += aim * int(units)

        continue

    # due to new instructions, the depth changes only
    # when we move forward, depending on how we aim, 
    # so we only update the aim here:
    elif direction == 'up':

        aim -= int(units)

        continue

    else:

        aim += int(units)

        continue

print(f'The horizontal position multiplied by final depth is: {horizonal_pos * depth}')
