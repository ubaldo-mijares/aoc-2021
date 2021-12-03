# ingest the list of items
with open('puzzle_input.txt') as txt:
    puzzle_input = txt.read().splitlines()

# create a counter
counter = 0

# iterate through all items and check if the diff is postitive. count each instance
for index, item in enumerate(puzzle_input):

    if index + 3 == len(puzzle_input):
        print(counter)
        break

    # gather data
    first_set = int(puzzle_input[index]) + int(puzzle_input[index + 1]) + int(puzzle_input[index + 2])
    second_set = int(puzzle_input[index + 1]) + int(puzzle_input[index + 2]) + int(puzzle_input[index + 3])

    if second_set - first_set > 0:
        counter += 1


