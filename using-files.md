# Using Files 📄 📃

In the words of the legendary beet farmer Dwight K. Schrute...
>There are basically two schools of thought...

He couldn't have said it any better! The 2 prominent
ideas in data persistence are as follows:
1. Using Files (the topic of this page)
2. Using databases (the topic of an upcoming page)

Aaaaaand...that's mostly it!

If you read the previous page (`basics.md`), then you saw
as little bit of what you can do by reading in files. Let's
look at more ways to do this and the world of possibilities
that are opened.

### Reading files

Python let's us read from existing files so that we can take
the data from them and use them in our programs. We saw an
example of this in `basics.md`. Let's look at that one more
time.

```
def printfile(filename):

    file = open(filename, "r")  # line a
    lines = list(file)          # line b

    # Now print the list
    for line in lines:          # line c
        print(line)             # line d

```

Let's dissect this program to see what's going on.

In line `a`, we use the `open(...)` function to open up a
file. We pass 2 arguments into the function:
* The first argument is a string that holds the name of the file we
  want to read. In the case above the string `filename`
  is the parameter passed into the function.
* The second argument is another string. This string
  represents the mode that we are opening the file in.
  The mode in which we open the file determines what we
  are allowed to do to the file. If we pass in "r", then
  we are opening the file in read mode (hence the `"r"`)


### Writing to Files

more super cool text

### How is this useful? 🤔

you guessed it. even more super cool text!
