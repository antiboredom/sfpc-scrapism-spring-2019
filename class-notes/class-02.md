# March 28th - Intro to Python

How to use python
Libraries

- SpaCy
- TextBlob (easier to use)


# Python

A programming language
it’s not compiled before you run, you just run it
it’s also a command line tool
Python command line tool is called “python”

We’ll use **python 3**. The command might be called “python3”

## Python shell

If we type just python3 you’ll get the **interactive shell**
It lets you write python code, one line at a time, and prints the output


    $ python3
    Python 3.6.5 (default, Apr 25 2018, 14:26:36) 
    [GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.39.2)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 
    
    

We’re not usually going to be using it, unless for quickly testing a command out.

To exit, use exit()
or Ctrl + D


## Making and running a Python file

We’ll usually write python files and execute them using “**python3 filename.py**”
****
One way to make a file is using the **touch** command.
Then we use **open** to edit it.

    $ touch hello.py
    // Creates a hello.py file if it doesn't exist. 
    // Note: If the file exists, it just updates its modified date
    
    $ open hello.py
    // Opens hello.py in the default editor
    

**To change the default editor**
Right click on the file > Get Info

![](https://paper-attachments.dropbox.com/s_F926F96F73EB3F06102EEFEAECD148D9B98E76E1A2ED2E94A7184B1208ABD9B0_1553787640917_image.png)


Change this setting

![](https://paper-attachments.dropbox.com/s_F926F96F73EB3F06102EEFEAECD148D9B98E76E1A2ED2E94A7184B1208ABD9B0_1553787664864_image.png)



**Good* code editors**
* use whatever you want there’s no good or bad editors 

- Sublime
  https://www.sublimetext.com/
- Visual studio code
https://code.visualstudio.com/



## Editing python

In python

- You *don’t* finish a line with a semicolon ;
- Spaces matter
  - code gets separated by how many spaces there are at the start of a line

Call a function regularly

    print("hello")
    # Output: hello
    
    print(1 + 1)
    # Output: 2

Declare a variable without any types

- variables have types, you just don’t declare them
    // In Javascript
    var name = "Sam";
    
    # In python:
    name = "Sam"
    


## Different kinds of variables
    
    # integers (round numbers)
    an_integer = 1
    
    # floats (numbers with decimals)
    a_float = 5.5
    
    # strings (collection of characters)
    some_string = "a collection of characters"
    
    # booleans (True/False) - NOTE: They're capitalized
    a_boolean = True
    
    # lists (called arrays in other languages)
    a_list_of_numbers = [5, 6, 7]
    a_list_of_strings = ["this", "are", "strings"]
    a_combination = ["strings", 2, 3, 4, 5.5]
    


## Using variables
    
    # you can print variables out
    print(a_float)
    # Output: 5.5
    


## Other details about python
- You usually use “snake case” rather than “camel case” (you don’t have to)
  - years_to_mass_extinction
    instead of yearsToMassExtinction


## Strings and lists

We’re gonna be mostly working with **strings** and **lists**


    
    first_name = "Karl"
    second_name = "Marx"
    
    # You can join strings together
    full_name = first_name + last_name 
    # results in "KarlMarx"
    
    # We'll add a space in between
    full_name = first_name + " " + last_name
    # results in "Karl Marx"
    
    # You can access particular characters in a string by their numerical index (begins with zero)
    first_character = first_name[0]
    # results in "K"
    
    # Getting the length of a string, use len()
    print( len(first_name) )
    # Output: 4
    

**More interesting ways of using strings (and lists)**

    
    # you can access an index from the back by using negative numbers
    # -1 means the last character
    print( full_name[-1] )
    # Output: x
    
    # get a slice of a string, between x and y characters
    print( full_name[0:2] )
    # gets the first two characters (from #0 to #2)
    # Output: Ka
    # If you skip the left side of the colon, it starts from the beginning
    # If you skip the right side, goes on until the end
    print( full_name[:3] )
    
    # I can determine if a string contains a character
    sentence = "A specter is haunting Europe"
    print( "spectre" in sentence )
    # value is True or False, if the string is in the variable
    # Output: False
    
    




## Flow control: IF Statements
- if [condition]:
  - and two spaces (or one tab) determine the chunk of code belongs to that conditional statement
    // In Javascript
    if (myVariable == 1) {
      // do thing
    }
    
    # in Python:
    if my_variable == 1:
      # do thing, inside the if statement
    # other code outside of it...
    
    if "spectre" in sentence:
      print("it's being haunted!")
    else:
      print("it's NOT being haunted")
    



## Manipulating strings

Make a string upper case (A SPECTER IS)

    print ( sentence.upper() )

Make a string lower case (a specter is)

    print ( sentence.lower() )

Make a string camel case ( A Specter Is Haunting… )

    print ( sentence.title() )

Cleans up white space from beginning and end of a sentence

    print ( sentence.strip() )

**These don’t change the original string**, to modify the string:

    sentence = sentence.upper()

You can see all the methods
https://docs.python.org/3/library/stdtypes.html#string-methods

Or you can see all the methods inside python:

    dir("")
    # get all the methods for a string
    


**Replace**

    # replace one part of a string with another
    sentence = sentence.replace("Europe", "this classroom")
    
    


## Lists

Lists are ordered collection of values.


    
    # Create a list
    my_list = []
    
    # Add to a list
    my_list.append("A")
    my_list.append("specter")
    my_list.append(20)
    
    print(my_list)
    # Output: ['A', 'specter', 20]

Strings and lists are very similar, use similar methods

    # Length of a list
    print( len(my_list) )
    
    # Obtain an item
    print( my_list[0] )
    # Get a list made out of the first to the second-to-last items
    print( my_list[:-2] )
    

**Iterating through a list’s values**

    // In Javascript:
    for(int i = 0; i < my_list.length; i++) {
      print(my_list[i]);
    }
    
    # in Python
    for word in my_list:
      print(word)

Pro tip: to iterate with an index value

    # Another way of iterating, using the range(min, max) function to get 
    # a number in a sequence to access the list
    for i in range(10):
      print(my_list[i])
    
    # More 'correct' way to do it, with the enumerate() function
    for index, word in enumerate(my_list):
      print(word + " is in index " + index)
    


## Converting strings to lists and back

We can switch between lists and strings

- convert a list to a string, with split()
- convert a string to a list with join()
    
    sentence = "A specter is haunting Europe"
    
    # transform the sentence into a list, split by the character I provide
    words = sentence.split(" ")
    
    # take a list and turn it back into a single string
    # You give it a joining character, and call the join([list]) function on it
    new_sentence = " ".join(words)
    


## Reading a file
    
    # Use the open() function, with a path to the file. If the file is in the same folder 
    # we can just use the name
    content = open("manifesto.txt").read()
    
    # that's actually two commands in one
    # open() returns a file object
    file_object = open("manifesto.txt")
    # read() reads that file object into a string
    my_string = file_object.read()
    
    # You can also read the file line by line
    lines = file_object.readlines()
    lines = open("manifesto.txt").readlines()
    for line in lines:
      print(line)



Now we can manipulate it

    
    words = content.split(" ")
    
    for word in words:
      word = word.replace("e", "eee")
      print(word)
    



## Saving the output + command line functions

Anything from the command line lesson, we can apply to the output of a python file

    
    // pipe the output of python
    $ python3 reading.py | say
    
    // save the output of python to a file
    # python3 reading.py > reading_output.txt
    


## Creating a file


    
    content = open("manifesto.txt").read()
    
    content = content.replace(" ", "!")
    
    # We create an output file
    # we use the open() function, but for writing
    # and write the contents
    open("new_manifesto.txt", "w").write(content)
    



## Randomness
- See the random module documentation here:
  https://docs.python.org/3/library/random.html
    # import the "random" module, to access its functions
    import random
    
    words = ["These", "are", "a", "lot", "of", "words"]
    
    # reorder our words list into a random order. NOTE: it modifies the original list
    random.shuffle(words)
    
    # get a random item
    random_item = random.choice()
    


## For later

**TextBlob**
https://textblob.readthedocs.io/en/dev/


- Library to extract extra meaning from text
- Tokenize a text and extract information from it
  - get only sentences, smartly
  - tag each word with its part-of-speech
    - e.g. get all the phrases with nouns in it, get all the adjectives, get only sentences

**SpaCy**
https://spacy.io/

- It’s better at detecting part of speech
- Advanced features
- bad: slightly less user friendly

To install libraries, the easiest way:

    $ pip3 install textblob
    
    // might need to type
    $ sudo pip3 install textblob
# Next week

Transform a text using Python

- have some input text, do some stuff to it, produce a new kind of output

The text that you’re transforming doesn’t necessarily have to be text that you **find** but you can produce it yourself.




# Bonus content

Kenneth Goldsmith
Discussion about
[https://twitter.com/kg_ubu/status/1109475202252050432](https://twitter.com/kg_ubu/status/1109475202252050432)


