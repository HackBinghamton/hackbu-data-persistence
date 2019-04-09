# Le Basics 🐣🐥

#### Now that we know why we might want to use data persistence, let's get started with some basic knowledge!

<br>

**Data Persistence** literally just means that data is persistent. In other words, it means that data remains even after the program finishes running.

Normally, when programming, we'll store information in *variables*. Variables are cool and all, but they have one tragic flaw: once a program ends, they lose all of their information.

This means that once a program is done running, all of things we stored in variables will be gone *forever* (\*cue scary sound effect\*).

Let's look at an example of this:

```python
def print_some_data():

    some_data = input("Enter some data here: ")
    print(some_data)

```
This code takes information from the user and then prints it out. But once the program ends, the program forgets everything that it once held. This is why if you run the code several times with different inputs, the result will be different.

But what if the user already wrote some information in another file and we want to print the contents of that file instead of making them re-type everything all over again? Let's take a look at how we can do that:

```python
def printfile(filename):

    file = open(filename, "r") # open the file
    lines = list(file) # store all the lines in a list

    # Now print the list
    for line in lines:
        print(line)

```

The function `printfile` will take a string as a parameter. This string is the name of some real file stored in the same folder as the code. Once the function reads the filename, it will open it and read all the lines from the file into a list called `lines`. In the following `for` loop, we simply print out each line from that list and call it a day.

Congrats, you've just started your journey into the wonderful world of data persistence! 🚀🛰

Now go and check out `using-files.md` to get a bit more in-depth!

For more information on this stuff, there are plenty of web pages that talk about file I/O with python. [Here's a pretty good one](https://www.guru99.com/reading-and-writing-files-in-python.html#1), it is a source for some of the material in this very file! The python documentation is also very helpful, don't be afraid to check it out.
