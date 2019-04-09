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

```python
def printfile(filename):

    file = open(filename, "r")  # line a
    lines = list(file)          # line b

    # Now print the list
    for line in lines:          # line c
        print(line)             # line d

```

Let's dissect this program to see what's going on.

In line `a`, we use the `open(...)` function to open up a
file. For simplicity, we store the file in a variable
called `file`, but you can name the variable anything
you want. We pass 2 arguments into the function:
* The first argument is a string that holds the name of
  the file we want to read. In the case above the string `filename` is the parameter passed into the function.
* The second argument is another string. This string
  represents the mode that we are opening the file in.
  The mode in which we open the file determines what we
  are allowed to do to the file. If we pass in "r", then
  we are opening the file in read mode (hence the `"r"`)

Once we've opened a file in read mode there are several
ways that we can read from it and use its information.
One of those ways is in the very code snippet that we're
observing!

In line `b`, we store all of the lines of `file`
in a list. The way shown in this code snippet is
a very simple way of doing this, and there are ways
of doing the same exact thing.

Lines `c` and `d` use a `for` loop to iterate (in other words to go thru) each line in the list that we stored and print each line.

### Writing to Files

Reading files is really useful, but what happens if we want to generate our own data and store that in files of our own? Well thankfully, python let's us do this too! And even better, we get to use the same `open(...)` function! The only difference is that now, we have to pass in the string `"w"` into the second parameter to denote that we're opening the file in `write` mode! Let's take a look at some
code:

```python
def write(filename, listOfLines):

    # filename is the name of the file to write to
    # listOfLines is a list of lines to write
    #   - assume plain text (alphanumeric) in listOfLines

    file = open(filename, "w")  # line a

    for line in listOfLines:    # line b

        file.write(line)        # line c
        file.write("\n")        # line d

```

Once again, let's dissect this code.

In line `a`, we open the file. This is no different from the way that we did it to read the file **except** that we pass in `"w"` to write instead of `"r"` for reading. We can now refer to `file` as the file that we have opened.

:warning: Note that passing `"w"` in for the mode will *__always__* create a new file. This means that if the file doesn't exist, it will be created. *__If the file already exists, your code will write over the existing file, thus deleting all the previous contents of the existing file.__* Please be careful when using this function in write mode.

In line `b`, we start using a `for` loop. We are going to iterate thru `listOfLines` and write each line to our file.

In line `c`, we use the `write()` function to (you guessed it) write to the file. The argument is a string, and line represents a line from listOfLines.

In line `d`, we write a newline to the file as well. This won't be interpreted as text, instead it will put a line break after the contents of `line` (which we previously wrote to the file in the line above).

### How is this useful? 🤔

When we read and write to files, we have a whole world of possibilities! Now we can store information in files by writing them! Once those file are written, we can use them in later runs of the program or even in completely different programs! And since most languages support file I/O (fie input/output), your files can be used by completely different programming languages (as long as the programmer knows the format of the contents of the file).

Now you can take these concepts and expand them in your code to make your programs do even more than before! Cool!

But what happens when we need to store information that is a bit more specific than what a simple text file allows?
Well fellow hacker, do we have an answer for you!

The answer would be to consider using **databases**! Go to [`databases.md`](./databases.md) to learn a bit more about what they are and how to use them.

## Table of Contents
1. [`motivation.md`](./motivation.md)
2. [`basics.md`](./basics.md)
3. [`using-files.md`](./using-files.md)
4. [`datbases.md`](./datbases.md)
