# Le Basics 🐣🐥

#### Now that we know why we might want to use data persistence, let's get started with some basic knowledge!

<br>
**Data Persistence** literally just means that data is persistent. In other words, it means that data stays even after the program finishes running.

Normally, when programming, we'll store information in *variables*, and variables are cool and all, but they have one tragic flaw: once a program ends, variables lose all of their information.

This means that once a program ends, all of things we stored in variables will be gone *forever* (\*scary sound effect\*).

Let's look at an example of this:

```
def print_some_data():

    some_data = input("Enter some data here: ")
    print(some_data)

```
This code takes information from the user and then prints it out. But once the program ends, the program forgets everything that it once held. This is why if you run the code several times with different inputs, the result will be different.

But what if the user already wrote some information in another file and we want to print the contents of that file instead of making them everything all over again? Let's take a look at how we can do that:

```
def printfile(filename):

    file = open(filename, "r") # open the file
    lines = list(file) # store all the lines in a list

    # Now print the list
    for line in lines:
        print(line)

```
