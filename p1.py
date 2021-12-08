def readFile(fileName):
    """
    Converts a txt file of \n separated values into an array of those values
    filename - filename of txt file
    returns array of values separated by \n in txt file
    """
    f = open(fileName, "r")
    numbers = f.read().splitlines()
    f.close()
    return numbers

def array_string_2_int(str_arr):
    """
    Converts an array of strings to an array of ints
    str_arr - array of strings
    returns array of ints
    """
    return list(map(lambda x: int(x), str_arr))

def compare_and_count(int_arr):
    """
    Zips adjacent array values together, maps to 1 if latter value in 
    tuple is greater and 0 otherwise. Sums up all instances where latter value is greater

    int_arr - array of integers
    returns number of instances where the number of times a value increases
    """

    int_arr_tuples = zip(int_arr, int_arr[1:])
    return sum(map(lambda x: 1 if x[0] < x[1] else 0, int_arr_tuples))

def main():
    fName = "p1_input.txt"
    input = array_string_2_int(readFile("p1_input.txt"))
    print("Answer to Part 1 of Day 1: " + str(compare_and_count(input)))

if __name__ == "__main__":
    main()
