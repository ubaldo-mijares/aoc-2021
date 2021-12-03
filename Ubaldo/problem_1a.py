# ingest the list of items
with open('puzzle_input.txt') as txt:
    puzzle_input = txt.read().splitlines()

# create a counter
counter = 0

# iterate through all items and check if the diff is postitive. count each instance
for index, item in enumerate(puzzle_input):

    if index + 1 == len(puzzle_input):
        print(counter)
        break

    if int(puzzle_input[index + 1]) - int(item) > 0:
        counter += 1


