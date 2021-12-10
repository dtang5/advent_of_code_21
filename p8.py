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

def splitBar(string_arr):
    """
    Splits on the bars in the input text file and takes the right side of each bar
    string_arr - text file split by lines
    returns an array of strings that are on the right side of each bar
    """
    return list(map(lambda x: x.split("|")[1], string_arr))

def join_arr(string_arr):
    """
    Does this in one line: 
        joined = ""
        for s in string_arr:
        joined += s
        return joined.split()

    Flattens the array of arrays

    string_arr - array of strings 
    returns an array of individual words
    """
    return [item for sub_array in string_arr for item in sub_array.split()]
    
def count_1478(string_arr):
    """
    Counts words of length 2,3,4,7 corresponding to 1,4,7, and 8
    string_arr - output from join_arr
    returns count of 1,4,7, and 8 numbers
    """
    return sum(map(lambda x: 1 if len(x) in [2,3,4,7] else 0, string_arr))
    
def main():
    fName = "./p8_input.txt"
    print("Answer to Part 1 of Day 1: " + str(count_1478(join_arr(splitBar(readFile("./p8_input.txt"))))))

if __name__ == "__main__":
    main()