
def writeToFile(filename, listOfLines):

    file = open(filename, "w")
    #print(listOfLines)

    for line in listOfLines:

        print(line)
        #print("\n")
        file.write(line)
        file.write("\n")

def main():

    # This is just some code to initialize listOfLines
    # There are likely better ways of doing this,
    # but the purpose of this example is just to show
    # what writeToFile(...) does!

    listOfLines = [None] * 5
    listOfLines[0] = "Segmentation Faults: A Haiku"
    listOfLines[1] = "---------"
    listOfLines[2] = "Segmentation Fault"
    listOfLines[3] = "Please no segmentation fault"
    listOfLines[4] = "Dang! I still got one"

    filename = "segfault_poem.txt"
    writeToFile(filename, listOfLines)




main()
