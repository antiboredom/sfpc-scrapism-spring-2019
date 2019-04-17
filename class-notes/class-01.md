# March 21st


# Details

**Syllabus:**

https://github.com/antiboredom/sfpc-scrapism-spring-2019


Class will be live streamed into a youtube video

Office hours:

- Sam’s office hours are directly after class
- Fernando’s office hours are Tuesdays 2-6pm

Sam: splavigne@gmail.com
Fernando: fernando.ramallo@gmail.com

To schedule office hours add your name to a slot: [+Office Hours](https://paper.dropbox.com/doc/Office-Hours-AKwuLxtjyy6F4YmE3ZFQX) 

Slack channel #2019-spring-scrapism
https://sfpc.slack.com/messages/CGXFXB2GZ/

# Class notes

today’s agenda

- intro about sam
- intro to command line


Sam Lavigne
artist and teacher
taught at the New School and NYU in ITP
http://lav.io/

His practice is about taking material from the internet and repurpose it, find new insights.

Notable projects

- ICE propaganda videos https://lav.io/projects/ice-propaganda-videos/
- White collar crime risk zones https://lav.io/projects/white-collar-crime-risk-zones/
- 3 Degrees of Separation from the Military-Industrial-Prison-Data-Surveillance State https://lav.io/projects/3-degrees-of-separation/
- Patent Generator https://lav.io/projects/patent-generator/
- CSPAN-5 https://lav.io/projects/cspan-5/



# What is scrapism

Class questions:

- how do you make new content with existing information. 
- how do you speak with someone else’s work/images/voice
- how can we automate creative production?

We’ll use python.

Majority of the class will be about text, a bit about image and a bit about video.

We’ll look at image and video as if it was **text**. Understanding media as text allows the computer (and us) to manipulate it more easily.

Based on historical practices doing the same thing (but without computers).

What kind of things will we make?

- Critique, satire
- commentary
- poetry

Usual workflow for projects:

1. Find a good source material to work with / research project
  1. why is something a good source material? why is something else not
2. Figure out how to get it
3. Figure out how to parse it / transform it
4. Figure out how to represent it to the world
  1. we give it new context

Investigation > collection > presentation

Scrapism is a word we made up. 
Looking to create an archive / find archives in the world / speak with them.


## Scrapist examples from other people

Allison Parrish
https://www.decontextualize.com/

- Favorite project https://twitter.com/everyword
  - bot tweeted every single word

Everest Pipkin
http://everest-pipkin.com/

- Cloud OCR
![](https://d2mxuefqeaa7sj.cloudfront.net/s_B4AD6204D93D9D5F1C07BC5CC6FD5C03917BB44939DDE0611372EF0C4E040602_1553179378270_image.png)

  - https://twitter.com/everestpipkin/status/646553843812200449
  - Computer generates a poem for a cloud


Anti-CAPTCHA
https://anti-captcha.com/mainpage

- Stories of exploited workers https://kolostories.com/contents/list

Daniel Temkin
http://danieltemkin.com/
- Internet Directory http://danieltemkin.com/InternetDirectory

National Novel Generation Month
https://nanogenmo.github.io/

- Plot to poem
  http://static.decontextualize.com/plot-to-poem.html
  Each sentence from the Wikipedia plot summary of these works has been replaced with the line of poetry from Project Gutenberg that is closest in meaning. 

Jenny Odell
http://jennyodell.com/

- http://www.jennyodell.com/satellite.html
  “In all of these prints, I collect things that I've cut out from Google Satellite View-- parking lots, silos, landfills, waste ponds. The view from a satellite is not a human one, nor is it one we were ever really meant to see. But it is precisely from this inhuman point of view that we are able to read our own humanity, in all of its tiny, repetitive marks upon the face of the earth. From this view, the lines that make up basketball courts and the scattered blue rectangles of swimming pools become like hieroglyphs that say: people were here.”

The Clock (2010 film)
https://en.wikipedia.org/wiki/The_Clock_(2010_film)

- 24 hour movie, each scene shows you what time it is
  The Clock is an art installation by video artist Christian Marclay. It is a looped 24-hour video supercut (montage of scenes from film and television) that feature clocks or timepieces. The artwork itself functions as a clock: its presentation is synchronized with the real time, resulting in the time shown in a scene being the actual time.
  - **How do we automate this? Is doing that good? What new things are possible if something like this could be automated?**



# The command line

It’s a text-based interface for interacting with your computer. You can use it to:

- launch programs
- open files
- manipulate your system
- etc etc etc anything really

On **Windows**, you’re gonna need to install:

https://docs.microsoft.com/en-us/windows/wsl/install-win10


To open on Mac:

- Applications > Utilities > Terminal
- or Cmd+Space, type Terminal

Some people prefer iterm2 https://iterm2.com/ it’s a terminal replacement with more features.

First thing you see is the **prompt**

![](https://d2mxuefqeaa7sj.cloudfront.net/s_B4AD6204D93D9D5F1C07BC5CC6FD5C03917BB44939DDE0611372EF0C4E040602_1553181599856_image.png)


by default you’ll see

- the name of your computer (in the image, my computer is named ‘computer’)
- a colon
- the folder you’re in. By default it’s a tilde ~ (the home folder)
- your username (in the image, my username is ‘fernantastic’)
- a dollar sign
- what you’re typing

To use it

- you type a command
- hit return
- see the output of the command

The home folder, in the Finder, is under /Users/yourusername

![](https://d2mxuefqeaa7sj.cloudfront.net/s_B4AD6204D93D9D5F1C07BC5CC6FD5C03917BB44939DDE0611372EF0C4E040602_1553181731001_image.png)



## Some useful commands

**pwd - To see where you are**

    $ pwd
    // returns the folder you're in
    /Users/sam

**ls - To list the directories and files in the folder you’re in**

    $ ls
    // returns a list of all the files
    
![](https://d2mxuefqeaa7sj.cloudfront.net/s_B4AD6204D93D9D5F1C07BC5CC6FD5C03917BB44939DDE0611372EF0C4E040602_1553181800063_image.png)


**cd - Change Directory**

    $ cd Desktop
    // goes to the Desktop folder (if there is any)
![](https://d2mxuefqeaa7sj.cloudfront.net/s_B4AD6204D93D9D5F1C07BC5CC6FD5C03917BB44939DDE0611372EF0C4E040602_1553181868617_image.png)

    $ cd ..
    // goes one level up

**mkdir - Make a folder**

    $ mkdir cool_project
    // a folder named cool_project was created
    
    $ cd cool_project
    // enter the new cool_project folder

**mv - Move files from one folder to the other (or Rename)**

    $ mv cohen.mp4 cohen_hearing.mp4
    // the file gets renamed, stays in the same folder

**cp - Copy a file**

    $ cp cohen.mp4 cohen_copy.mp4
    // Makes a copy 
    
    $ cp cohen.mp4 Desktop/another_cohen.mp4
    // Makes a copy but places it in the Desktop folder
    
    // To copy a directory, add the flag -r
    $ cp -r my_directory my_new_directory
    

**rm - Remove / delete files — !!! Careful !!!**

    $ rm trump2.mp4
    // Deletes trump2.mp4. Won't ask for confirmation nor move it to the Trash! It's gone
    
    // Add -r to delete a directory
    $ rm -r cool_directory
    


## More commands

https://en.wikipedia.org/wiki/List_of_Unix_commands (thanks Stefan)


## Folder structure

Shortcuts

- **/** (forward slash) - the root folder (the top folder in the hard drive)
- **~** (tilde) - your user folder (equal to /Users/yourusername)

You can navigate your hard drive on the Terminal using absolute or relative paths

- **Absolute path**: the full path to a folder or file
    $ open /Users/fernantastic/Desktop/myfile.mp4
- **Relative path**: the path to the file relative to what folder you are in
    // if I’m in my user folder:
    computer:~ $ open Desktop/myfile.mp4
  

You can use relative paths by going **up and down** the folders

- .. (double period) - the folder above
    // assuming we're three levels down inside the desktop folder
    // we find the file by indicating three levels up ../../../
    $ open ../../../Desktop/trump.mp4


# Manipulating Text


## Good sources for corpuses

**Project gutenberg**

http://gutenberg.org/ebooks/2701


**gutenberg-damnit**
https://github.com/aparrish/gutenberg-dammit
Project gutenberg, but nicely formatted for text manipulation

**libgen.io**
ebooks of questionable sources
http://libgen.io/

We saved moby dick in **Plain Text format**


## Seeing the contents of a file

We use the **cat** command to print out the contents of the file

    $ cat moby_dick.txt
    // Quickly prints out all of the content (too fast)
    

A more useful way to look at text files, is the command **more**

    $ more moby_dick.txt
    // Go up and down with arrows

To exit the viewer hit **q**

Sort a file with **sort**

    $ sort moby_dick.txt
    // Outputs the lines of the file in alphabetical order

Search in files with **grep**

    $ grep "Dick" mobydick.txt
    // Print out the lines of the file that contain the word Dick



## All commands have optional parameters


    $ sort -r moby_dick.txt
    // -r tells the sort command to sort the file in reverse
    
    $ sort -u mobydick.txt
    // sorts it but removes repeats


## Saving the output of the command line

the “redirect” tag, with the greater than character, saves the output of the left side command into the right side output file

    
    $ sort -r mobydick.txt > sorted_moby_dick.txt
    // saves all lines of moby dick, sorted in reverse, into a text file
    


## Combining commands

With a “pipe” ( this character: | ), we can do commands in sequence, sending the output from one command into another command

    
    $ grep "Dick" mobydick.txt | sort -u
    // First, get all the lines that contain the word dick
    // Send it to the sort command as an input
    // output the sorted, unique, ones
    
    $ grep "Dick" mobydick.txt | sort -u > sorted_dicks.txt
    // Output it all to a file
    

You can combine as many commands as you want


## Cutting out portions of a text file

Cut out a portion of each line and splits it out according to a delimiter

    $ cut -d " " mobydick.txt
    // breaks up each line into words (by splitting lines by the space characters)
    
    $ cut -d " " -f mobydick.txt
    // -f outputs the first word of each line
    
    $ cut -d " " -f 2 mobydick.txt
    // -f outputs the second word of each line
    
    $ cut -d " " -f 1 mobydick.txt | sort -u | grep '!'
    // get all the words, output only the first, then sort it all, then get the ones that have exclamation marks on it
    


## Finding and replacing

**tr** command (translate), give it a series of input characters and a series of characters to replace those with

    $ tr -s "e" "a" < mobydick.txt
    // look for the letter e, replace it with a
    // (we use < lesser than, as an inverse of the > to output to a file: instead we input from mobydick.txt )
    
    $ tr -s "e" "a" < mobydick.txt | more
    // we pipe it to the more command, to look at the output with the arrows
    
    $ tr -s "e" "a" < mobydick.txt > modified_mobydick.txt
    // we save the output to a new file
    
    $ tr -s "eou" "a" < mobydick.txt
    // Replace more than one character. Every e, o, u, turns into an a

a more complete find and replace
the **sed** command (can be complicated)

    $ sed 's/e/aaaaa/g'
    // s stands for search, give it something to look for and something to replace
    // find the letter e
    // replace it with aaaaa
    // g means do it globally


# Make the computer talk

the **say** command is fun

    $ say < mobydick.txt
    // Say all of moby dick
# When you can’t remember a command

Google it! it’s ok
https://duckduckgo.com/?q=print+first+word+text+file+unix+bash&atb=v125-5__&ia=web

**tldr** gives you what the most common uses of a command are
requires brew

    $ tldr sort
    // "Sort lines of text files", shows examples ... 
# Installing python 3

easiest is using brew
https://brew.sh/

To install brew, run this in the terminal:

    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

To install python:

    brew install python3


# For next class

Readings:
Intro to the command line 
https://github.com/antiboredom/sfpc-scrapism/blob/master/reader-01-the-command-line.md

Non-technical reading
https://selforganizedseminar.files.wordpress.com/2011/08/bishop-claire-artificial-hells-participatory-art-and-politics-spectatorship.pdf

come prepared to have a conversation about the Claire Bishop reading

## Assignment

Create a poetic text using only command line tools
(full description will go on github, will replace current one)

what are the things that these tools allow you to do to text that you would not be able to do on your own
how can you start to think about producing meaningful new content / context / using these very simple tools
Most of the class we’ll be doing sorting, filtering, finding and replacing, 
think broadly about what those techniques actually are, 

- sorting , e.g. radicalization in social media in a way because of how videos are sorted, not chronologically but by an algorithm
- think of these techniques as windows to other topics

five volunteers will read their text

