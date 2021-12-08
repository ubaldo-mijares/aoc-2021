import collections


def binary_to_decimal(binary: list):
    '''
        This function will accept a list containing the parts of a binary number and convert it to an integer.

        The decimal number is equal to the sum of binary digits times their power of 2

        For example:
        binary = ['1', '0', '1', '1', '0']
        indexes:   4    3    2    1    0

        decimal = 1 * (2 ** 4) + 0 * (2 ** 3) + 1 * (2 ** 2) + 1 * (2 ** 1) + 0 * (2 ** 0)
        decimal = 16 + 0 + 4 + 2 + 0 = 22

        inputs
            binary: list of the binary number split into indexes

        returns
            decimal: integer, decimal conversion from binary
    '''

    # have to flip the list, since python counts the indexes from 0 to n, rather than n to 0
    # then run the algorithm
    decimal_list = [int(val) * (2 ** index) for index, val in enumerate(list(reversed(binary)))]

    return sum(decimal_list)


def common_search(main_index, value_list):
    '''
        This function will look for the most common bit in the input index

        inputs
            value_list: list, the list of binary values we want to scan
        
        returns
            mcb: most common bits in 
    '''

    # create a dictionary to store the n-th bit from each item in the list
    bit_counting = {counter: [] for counter, item in enumerate(value_list[0])}

    # iterate through the list of items, and extract the bits from each position
    for item in value_list:

        for index, bit in enumerate(item):

            bit_counting[index].append(bit)

    # create lists for handling the most and least common bits (not accurately named, but whatever)
    mcb = list()
    lcb = list()

    # count the most common bit in the n-th list
    counter_check = collections.Counter(bit_counting[main_index]).most_common(2)

    if counter_check[0][1] > counter_check[1][1]:
        
        mcb.append(counter_check[0][0])
        lcb.append(counter_check[1][0])
    
    elif counter_check[0][1] == counter_check[1][1]:

        mcb.append('1')
        lcb.append('0')
        
    else:

        mcb.append(counter_check[1][0])
        lcb.append(counter_check[0][0])

    return mcb, lcb

def main():
    '''
        function to figure out how much power the sub consumes
    '''

    # ingest the list of items
    with open('Ubaldo/problem3.txt') as txt:
        puzzle_input = txt.read().splitlines()

    # initialize the o2_gen and co2_scrub lists
    o2_gen = puzzle_input
    co2_scrub = puzzle_input

    # determine the oxygen generator rating
    for index in range(0, len(o2_gen[0])):

        mcb, _ = common_search(index, o2_gen)

        o2_gen = [val for val in o2_gen if val[index] == mcb[0]]

        if len(o2_gen) == 1:
            # need to split the last remaining value into a list
            o2_gen = [val for val in o2_gen[0]]
            break
    
    # determine the co2 scrubber rating
    for index in range(0, len(co2_scrub[0])):

        _, lcb = common_search(index, co2_scrub)
    
        co2_scrub = [val for val in co2_scrub if val[index] == lcb[0]]

        if len(co2_scrub) == 1:
            # need to split the last remaining value into a list
            co2_scrub = [val for val in co2_scrub[0]]
            break

    # convert the o2_gen and co2_scrub values into decimal
    o2_gen = binary_to_decimal(o2_gen)
    co2_scrub = binary_to_decimal(co2_scrub)
    
    print(f'O2 Generator: {o2_gen}, CO2 Scrub: {co2_scrub}')
    print(f'The life support rating is: {o2_gen * co2_scrub}')


# run it
if __name__ == '__main__':

    main()