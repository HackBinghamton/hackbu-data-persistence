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

#### But How Though?! 🧐

Databases are so common that there's a whole language dedicated to manipulating them! It's called __SQL__, which stands for Structured Query Language. However, most languages (including python) have APIs (Application Program Interfaces) that allow you to create objects that handle database creation for you! From there, all you have to do is create such an object, and pass single SQL instructions into it. You still have to know a bit of the language, but you still get to use your favorite language for the majority of the project (unless you're writing a very database-have proggram, which is cool too!)!

#### So Many Choices, So Little Time ⏰

So now that you've gotten your feet wet with the basics of data persistence and a quick overview of databases, you're ready to start thinking about using this stuff in your own code.

Here are some nice database frameworks that you can start using whenever you want:

* [MySQL](https://www.mysql.com/)
* [SQLite](https://www.mysql.com/)
* [mongoDB](https://www.mongodb.com/)

SQLite is very simple and easy to use, so that might be the best choice. But if you're advanced or adventurous go ahead and try MySQL! mongoDB is a NoSQL language, which means that you get the beauty of databases without having to learn SQL, it is most commonly used with JavaScript web apps, as it represents the "M" in *__MEAN__* stack (*__M__*ongo, *__E__*xpress, *__A__*ngular, *__N__*ode.js). *____*

Congratulations, hacker!! You now know the basics of data persistence! You even know a bit about using databases to make computers remember things for you! This is an exciting time. Remember to use your new powers for good, we can't wait to see what cool things you do. As you continue to explore this new frontier, feel free to ask an organizer for help.

Have fun!

-- Le HackBU Crew
