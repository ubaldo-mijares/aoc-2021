import statistics
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


def main():
    '''
        function to figure out how much power the sub consumes
    '''

    # ingest the list of items
    with open('Ubaldo/problem3.txt') as txt:
        puzzle_input = txt.read().splitlines()

    # create a dictionary to store the n-th bit from each item in the list
    bit_counting = {counter: [] for counter, item in enumerate(puzzle_input[0])}

    # iterate through the list of items, and extract the bits from each position
    for item in puzzle_input:

        for index, bit in enumerate(item):

            bit_counting[index].append(bit)

    mcb = list()
    lcb = list()

    # count the most common bit in each list
    for item in bit_counting:

        counter_check = collections.Counter(bit_counting[item]).most_common(2)

        if counter_check[0][1] > counter_check[1][1]:
            
            mcb.append(counter_check[0][0])
            lcb.append(counter_check[1][0])
            
        else:

            mcb.append(counter_check[1][0])
            lcb.append(counter_check[0][0])


    # send the list to the binary converting function
    mcb = binary_to_decimal(mcb)
    lcb = binary_to_decimal(lcb)
    

    print(f'gamma: {mcb}, epsilon: {lcb}')
    print(f'The power consumption is: {mcb * lcb}')


# run it
if __name__ == '__main__':

    main()