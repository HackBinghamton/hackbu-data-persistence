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

This is where databases come in.

#### The Beauty of Databases
