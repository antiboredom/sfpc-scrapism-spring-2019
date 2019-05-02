# May 2nd - Functions

aubio
easy audio library for python
https://aubio.org/


# Functions

We’ll make a simple program to overlay text on a video

    
    import moviepy.editor as mp
    
    text= "A specter is haunting these dolphins"
    
    clip1 = mp.VideoFileClip("dolphins.mp4").subclip(29, 32)
    clip2 = mp.TextClip(text, size=clip1.size, font="Arial", color="white").set_duration(3)
    
    composition = mp.CompositeVideoClip([clip1, clip2])
    composition.write_videofile("dolphin_words.mp4")
    

And now we’ll turn it into a function we can reuse

    import moviepy.editor as mp
    
    def dolphin(text):
      clip1 = mp.VideoFileClip("dolphins.mp4").subclip(29, 32)
      clip2 = mp.TextClip(text, size=clip1.size, font="Arial", color="white").set_duration(3)
      
      composition = mp.CompositeVideoClip([clip1, clip2])
      composition.write_videofile("dolphin_words.mp4")
    
    # And we call the function
    dolphin("Helloo!")

What we actually wanna do with this is be able to use it from other files, but also be able to runit from the command line

We’re gonna add

    if __name__ == "__main__":
      dolphin(sys.argv[1])

This is weird but

- python has a secret variable called '__name__' and its value  is '__main__' if the python script got executed in the command line
- sys.argv is a list that contains all the command lines that happened after the word python (as in '$ python myscript.py firstargument secondargument')


So now our script looks like

    import moviepy.editor as mp
    import sys
    
    def dolphin(text):
      clip1 = mp.VideoFileClip("dolphins.mp4").subclip(29, 32)
      clip2 = mp.TextClip(text, size=clip1.size, font="Arial", color="white").set_duration(3)
      
      composition = mp.CompositeVideoClip([clip1, clip2])
      # And write a gif instead of an mp4
      composition.write_gif("dolphin_words.gif", fps=10)
    
    if __name__ == "__main__":
      dolphin(sys.argv[1])
    


with this now we could:

- make a website that overlays text on videos
- a bot that reads a list of files and figures out a new phrase to put on the video and tweet it
- a bot that emails us periodically with a new video

We’re gonna make another .py file in the same folder and:

- add import vidbot
    - it’ll find any file in the same folder called **vidbot** and we can use its functions

Make sure the emails package is installed

    $ pip3 install emails

We’re gonna write a script that 

1. Creates an email
2. Attaches the GIF created by our vidbot.py script
3. sends it
    import vidbot
    import emails
    
    vidbot.dolphin("whatever you want")
    
    message = emails.html(
      html="Hello from class!",
      subject="A specter is haunting your email",
      mail_from=("Scrap Ism", "scrapism.sfpc@gmail.com")
    )
    
    message.attach(data=open("dolphin_words.gif", "rb"), filename="dolphin_words.gif")
    
    message.send(
      to=("Sam", "splavigne@gmail.com"),
      # we have to use an 'SMTP' server, putting an actual
      # email account and password
      smt={
        "host": "smtp.gmail.com",
        "port": 465,
        "ssl": True,
        "user": "scrapism.sfpc@gmail.com",
        "password": "scrapismscrapism"
      }
    )



We’ll add data from corpora, and turn it into a bot using cron

https://github.com/dariusk/corpora/

    import vidbot
    import emails
    
    isms = [
      "abstract expressionism",
      "academic",
      "action painting",
      "aestheticism",
      "art deco",
      "art nouveau",
      "avant-garde",
      "barbizon school",
      "baroque",
      "bauhaus",
      "biedermeier",
      "caravaggisti",
      "carolingian",
      "classicism",
      "cloisonnism",
      "cobra",
      "color field painting",
      "conceptual art",
      "cubism",
      "cubo-futurism",
      "dada",
      "dadaism",
      "de stijl",
      "deformalism",
      "der blaue reiter",
      "die brücke",
      "divisionism",
    ]
    
    ism = random.choice(isms)
    vidbot.dolphin(ism)
    
    message = emails.html(
      html="Hello from class!",
      subject="A specter is haunting your email",
      mail_from=("Scrap Ism", "scrapism.sfpc@gmail.com")
    )
    
    message.attach(data=open("dolphin_words.gif", "rb"), filename="dolphin_words.gif")
    
    message.send(
      to=("Sam", "splavigne@gmail.com"),
      # we have to use an 'SMTP' server, putting an actual
      # email account and password
      smt={
        "host": "smtp.gmail.com",
        "port": 465,
        "ssl": True,
        "user": "scrapism.sfpc@gmail.com",
        "password": "scrapismscrapism"
      }
    )



# Scheduling our script to run automatically

We’ll schedule our script with **cron**
cron uses a special syntax:

- https://crontab.guru/

numbers of stars

mycrontab.

    0 * * * * /Users/sam/.pyenv/shims/python3 /Users/sam/Desktop/bots/emailbot.py

Means

- every first minute of the hour (e.g. once an hour)
- run python3 (with the exact path to your python3 install)
    - find it with “$ which python3”
    - 
- and open my python file (with an exact path)

And we run the scheduled script on the terminal

    $ crontab mycrontab

cron runs

- when the computer is on 
- you can set this up on a server



# Running our scripts on the web


    from flask import Flask
    
    # Make a Flask object
    app = Flask(__name__)
    
    # This is a 'function decorator'
    # wraps a function that comes after in another function
    # 'when the user visits this path (/, the root path)
    # then execute this function
    # don't worry about it 
    @app.route("/")
    def home():
      return "Hello class"
    
    if __name__ == "__main__":
      app.run(debug=True)

Start the web server

    $ python mywebapp.py

Now we can open our browser to http://127.0.0.1:5000 (or whatever the terminal window says)


- Note: if we change the script we need to restart the script
    - we can add debug=True to app.run() to do this automatically
- 127.0.0.1 is the same thing as ‘localhost’, it means the address to your own computer
    - http://localhost:5000 would also work
- We can add more routes:
    @app.route("/bye")
    def bye():
      return "goodbye"
    - and we can now go to http://localhost:5000/bye



## We can read data from the URL bar


    from flask import Flask, request
    
    # Make a Flask object
    app = Flask(__name__)
    
    @app.route("/")
    def home():
      text = request.args.get("text")
      return "you typed " + text
    
    if __name__ == "__main__":
      app.run(debug=True)

now we can test it by pointing our browser to

- http://localhost:5000/?text=hello



## Now we’ll turn this into a web server that generates the dolphin GIF


1. We’ll make a folder called static. 
    1. By default Flask will try and look for files in this folder and see if it finds it.
    2. user can access that file with a path to it in the browser
2. We’ll add an outputname parameter to our vidbot function to determine where the file is saved


    from flask import Flask, request
    import vidbot
    
    # Make a Flask object
    app = Flask(__name__)
    
    @app.route("/")
    def home():
      text = request.args.get("text")
      if text == None:
        text = "Nothing"
      vidbot.dolphin(text, "static/" + text + ".gif")
      return "<img src='static/" + text + ".gif'>"
    
    if __name__ == "__main__":
      app.run(debug=True)

final vidbot.py

    import moviepy.editor as mp
    import sys
    
    def dolphin(text, outputname):
      clip1 = mp.VideoFileClip("dolphins.mp4").subclip(29, 32)
      clip2 = mp.TextClip(text, size=clip1.size, font="Arial", color="white").set_duration(3)
      
      composition = mp.CompositeVideoClip([clip1, clip2])
      # And write a gif instead of an mp4
      composition.write_gif(outputname, fps=10)
    
    if __name__ == "__main__":
      dolphin(sys.argv[1])


For running scripts on a web server:

- https://www.digitalocean.com/
- https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps
- https://aws.amazon.com/

To make a twitter bot with python:

- twython https://twython.readthedocs.io/en/latest/
- instagram https://github.com/instabot-py/instabot.py
- instagram et. al https://buffer.com/



# For the showcase

Send Sam your favourite thing you made in the class (or finish it if it’s not done)
and he’ll figure out

format:

- some kind of output that can be an image or a text or a video or a website, etc. 
- the source material that you used (a link to it, where it came from)
- the source code
- little description if you want

Sam can come for office hours next week

Due Wednesday

