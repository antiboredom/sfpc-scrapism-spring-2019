# April 18th


# Agenda

Downloading w/ Python
Manipulating images
Intro to OpenCV



# Misc

Manipulating audio with python

- Pydub
    http://pydub.com/




# Downloading images

Goal: Download all the images from a shutterstock search
https://www.shutterstock.com/search/money+rain?image_type=photo


1. Turn javascript off, make sure images are still loading
2. Right click > Inspect
3. See that images are in a div with weird class z_e_e z_e_f or something there’s the description
    But the images are in a different div z_e_h, with the image link and the description too

shutterscrape.py

    from requests_html import HTMLSession
    import requests
    
    session = HTMLSession()
    
    r = session.get("https://www.shutterstock.com/search/money+rain?image_type=photo")
    
    # tags separated by a period here means get all the img tags that has class z_e_h
    images = r.html.find("img.z_e_h")
    
    for image in images:
      # get the src attribute
      print(image.attrs.get("src"))
      # get the alt tag to get the description
      print(image.attrs.get("alt"))
      
      # To get the name of the image, we split the address into a list by a forward slash
      # and then get the last element of the list
      imagename = src.split("/")[-1]
      # we'll add an 'images' path before so our images save into a folder
      imagename = "images/" + imagename
      
      # To download the image data we use requests library
      # and the content attribute contains the actual data
      imagedata = requests.get(src).content
    
      # and we'll save it to a file, w for writing mode and b for binary
      open(imagename, 'wb').write(imagedata)  
    




## Making a script take arguments from the command line


    
    import sys
    
    # All the arguments when running the script are stored as a list 
    # in sys.argv
    # The first one is the name of the script
    print(sys.argv)
    
    sys.argv[1]
    


Our script, taking the search term from the command line

- **Usage: python3 shuttersearch_sys.py my_search_term**

shuttersearch_sys.py

    import sys
    from requests_html import HTMLSession
    import requests
    
    session = HTMLSession()
    
    search_term = sys.argv[1]
    
    r = session.get("https://www.shutterstock.com/search/?searchterm=" + search_term + "&image_type=photo")
    images = r.html.find("img.z_e_h")
    
    for image in images:
      imagename = src.split("/")[-1]
      imagename = "images/" + imagename
      
      imagedata = requests.get(src).content
    
      open(imagename, 'wb').write(imagedata)  





# Manipulating images

We’ll use imagemagick, to install, in the terminal:

    $ brew install imagemagick


Imagemagick documentation
https://www.imagemagick.org/script/command-line-processing.php#option

Note: There’s also a version of imagemagick made as a python library called Wand

    http://docs.wand-py.org/en/0.5.2/


## Using imagemagick’s commands
    
    // Convert from one format to another
    $ convert sample.jpg sample.gif
    
    // Use parameters to change the image
    $ convert sample.jpg -resize 10x10 sample_small.jpg
    $ convert sample.jpg -rotate 90 sample_rotated.jpg
    $ convert sample.jpg -negate sample_negated.jpg



## We can use "glob patterns” to apply commands to multiple files
    
    // Basic glob patterns
    
    // List files that start with *anything* and end with jpg
    $ ls *.jpg
    // List all files (start with * anything and end with * anything)
    $ ls *.*
    

So using that with imagemagick

    
    // Convert and take any jpg file in the images folder, and output as a single gif file
    $ convert images/*.jpg -delay 0 animation.gif


## Other uses
    
    // Take all jpg images from a folder and lay them out 
    $ montage images/*.jpg allimages.jpg
    
    // You can do for loops in the command line
    $ for f in images/*.jpg do echo "$f; done
    


# Using imagemagick from python to manipulate images

We’ll use subprocess to run a terminal command


    import subprocess
    
    # Every command in the terminal where there's a space needs to be 
    # separate items in a list.
    subprocess.call(["say", "-r", "600", "hello class"])
    
    # Now we can do fun python stuff
    
    for i in range(700, 800):
      # Won't work, because you need to pass strings
      subprocess.call(["say", "-r", i, "hello class"])
      # This'll work
      subprocess.call(["say", "-r", str(i), "hello class"])
    
    


Now let’s make our image downloader script convert the images it’s downloading

shuttersearch_and_convert.py

    import subprocess
    import sys
    from requests_html import HTMLSession
    import requests
    
    session = HTMLSession()
    
    search_term = sys.argv[1]
    
    r = session.get("https://www.shutterstock.com/search/?searchterm=" + search_term + "&image_type=photo")
    images = r.html.find("img.z_e_h")
    
    for image in images:
      imagename = src.split("/")[-1]
      imagename = "images/" + imagename
      imagedata = requests.get(src).content
      open(imagename, 'wb').write(imagedata)  
      
      # Call convert command, negate the image, set its output
      subprocess.call(["convert", imagename, "-negate", imagename + "_negated.jpg"])
      


# Using pillow to manipulate images inside python

Install:

    
    $ pip3 install pillow
    



    from PIL import Image
    
    img = Image.open("sample.jpg")


 Resize (respects the image aspect ratio), and replaces the original img object

    img.thumbnail((100, 100))

Resize to any dimension

    img = img.resize((500, 10))

Save the image

    img.save("sample_small.jpg") 

Rotate it

    img = img.rotate(30)



## With pillow we can create an empty canvas and draw things to it

make_bad_collage.py

    from PIL import Image
    import random
    import glob
    
    # We use glob to get all the jpg images from our images folder
    files = glob.glob("images/*.jpg")
    
    # Create a new canvas, specify the color space and dimensions
    canvas = Image.new("RGB", (1000, 1000))
    
    for filename in files:
      # Open the image
      img = Image.open(filename)
      
      # Now we can do anything to the image, e.g. resize it
      img.thumbnail((100,100))
      
      # get a random number between 0 and 1000
      x = random.randint(0, 1000)  
      y = random.randint(0, 1000)
    
      # Place the image onto the canvas, at a certain position
      canvas.paste(img, (x, y))
    
    # Save it
    canvas.save("bad_collage.jpg")





# Homework

--------- **Make a collage ---------**

(if you don’t want to make a collage and want to make something else to share that’s fine, just play around with these tools)


