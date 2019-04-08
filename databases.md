# Databases 📠 📟

#### So now you know what data persistence is and how to implement it with files. You're doing great!

<br>

Now imagine that you want to store specific information, let's say its for a phonebook and we want to store information about one person per file. We could do it like this:

```
Person1.text
------------

Michael G. Scott
55
Colorado

```

You might guess that the first line holds the person's full name, the second line holds their age, and that the final line is the state where the person lives, but this information isn't exactly obvious. This is the problem with only using files for data persistence. **Using them becomes difficult when you want to store very specific information.**

Recall that computers work best with specific instructions, and that they don't have "common sense" like us earthlings. So this type of ambiguity is not really good for our coding projects.

This is where databases come in.

#### The Beauty of Databases

Databases are really great because they allow us programmers to essentially make our own types (similar to the way classes and objects do). With a database we can use one file to hold a number of different objects, and these objects can contain any information that we want it to.

Different databases are implemented in different ways, but there is a basic structure to the way that we can use them.

In a database, the user (you) can create tables, and just like a regular table, each column represents a type of value. This sounds really simple, but it is actually a powerful way to make your data very specific.

In the spirit of our example above, we could easily make a table that is designed to hold a person's name, age, and state of residence (we can even extend the object to split name into first name, last name, and middle initial -- design choice).
