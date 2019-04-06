
def readfile(filename):

    file = open(filename, "r")
    lines = list(file)

    return lines

def printfile(lines):

    for line in lines:

        print(line)

def main():

    lines = readfile("test.txt")
    printfile(lines)

main()
