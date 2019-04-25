# April 25 - Video



# Today

how to get video
how to manipulate video (in cmd line and through python)

There’s new README files, with more information about topics from the class in the repo:
https://github.com/antiboredom/sfpc-scrapism-spring-2019/

e.g.
https://github.com/antiboredom/sfpc-scrapism-spring-2019/blob/master/readme-FFMPEG.md



# Video

If we go to Shutterstock.com > FOOTAGE

https://www.shutterstock.com/video/search/slow-motion-crying


you could write a scraper,
you can inspect the element that has the video and find that it’s an mp4/webm video

The problem is when you go to something like Youtube, and replicate that process we bump into hurdles, the source for the video is a weird blob, they change it all the time.
So **scraping video isn’t recommended using the tools we’ve learnt**

What’s recommended is to use **youtube-dl**
https://youtube-dl.org/

- Scrape videos from youtube and an infinite number of websites


## Installing youtube-dl
    $ brew install youtube-dl


## Basic usage

give it a URL to a video and it’ll download it

    $ youtube-dl https://www.youtube.com/watch?v=j2cSjf3gvvA

If it doesn’t work you might have an old version of youtube-dl, to update it:

    $ youtube-dl -U



By default, it’ll download what it perceives it to be the highest quality it can find of that video (maybe?)


## Downloading a specific format

If you want to select what version to download, add the **-F** parameter **to see what formats and resolutions are available**

    $ youtube-dl https://www.youtube.com/watch?v=j2cSjf3gvvA -F


![](https://paper-attachments.dropbox.com/s_0E6ABDF55DFC40959A226E0630075CF52F5B96C879B792C7284A2FB84C9D48DB_1556203336847_image.png)


and find the **code** for the version you want
**some are just the audio**

To pick a specific format, add -f (lowercase) and the code for the specific version

    $ youtube-dl https://www.youtube.com/watch?v=j2cSjf3gvvA -f 22



## Downloading to a specific file name or folder
    # add -o [filename]
    # - you can add a path to it (e.g. “videos/baby.mp4”)
    
    $ youtube-dl https://www.youtube.com/watch?v=j2cSjf3gvvA -f 22 -o baby.mp4


## Just getting the URL of the video file
    # add --get-url
    $ youtube-dl https://www.youtube.com/watch?v=j2cSjf3gvvA -f 22 --get-url


## Downloading entire channels
    # just use the URL for the channel
    $ youtube-dl https://www.youtube.com/user/whitehouse


## For all the options available

See the documentation for youtube-dl

https://github.com/ytdl-org/youtube-dl/blob/master/README.md#readme


Other useful options:

- --match-title  to only download videos with a description that matches a search or word
- --min-views only videos with certain views



# Getting text


    
    # Use --write-auto-sub --skip-download
    # To get the subtitles and not download the video
    # Only works with 
    $ youtube-dl https://www.youtube.com/watch?v=bLx5hLag6WQ --write-auto-sub --skip-download




# FFMPEG

Note: Working with smaller videos will be faster

**FFMPEG is a command line tool for manipulating video.**
It’s extremely complicated and you can do a lot of things with it.
But there’s also very simple things to do with it.

The documentation gives you an overview of what you can do
https://ffmpeg.org/documentation.html

To install

    $ brew install ffmpeg


## Usage
    
    # ffmpeg -i \[video file name\] [output video name]
    
    # Converts an mp4 video to a .mov
    $ ffmpeg -i baby.mp4 baby.mov
    
    # converting to an .mp3 extracts the audio
    $ ffmpeg -i baby.mp4 baby_audio.mp3
    


## GIF Making

A useful thing to do is making GIFs out of videos (although they might be large files)

    $ ffmpeg -i baby.mp4 baby.gif

To make it better, we can add options to it

- -r to lower the framerate
    $ ffmpeg -i baby.mp4 -r 3 baby.gif

More info from GIPHY on how to make Gifs with ffmpeg https://engineering.giphy.com/how-to-make-gifs-with-ffmpeg/

    $ ffmpeg -ss 61.0 -t 2.5 -i StickAround.mp4 -filter_complex "\[0:v] fps=12,scale=480:-1,split [a\][b];\[a] palettegen [p];[b\][p] paletteuse" SmallerStickAround.gif


## FFMPEG TIP

**don’t bother figuring out how to do stuff with it just google it**


## Extracting frames as a folder of images
- adding %d to the output means: %d gets replaced by the frame number
- %04d adds zeros before behind the frame number for better ordering
    $ ffmpeg -i baby.mp4 babyframes/frame-%04d.jpg


## We can turn images back into a video


    $ ffmpeg -f image2 -i babyframes/frame-%04d.jpg newbaby.mp4



## Use -t to get a section of a clip
    # get the first second
    $ ffmpeg -i baby.mp4 -t 1 1secbaby.mp4
    
    # start at a certain part (at 2 seconds) and get 1 second
    $ ffmpeg -i baby.mp4 -ss 2 -t 1 1secbaby.mp4


## Getting information about a video

e..g to get the frames per second, duration, encoding, etc 

    $ ffprobe baby.mp4


## Using filters

https://ffmpeg.org/ffmpeg-filters.html


## See more uses in the reader
- chroma key
- record the webcam
- stitch mp4s together
- slow down videos
https://github.com/antiboredom/sfpc-scrapism-spring-2019/blob/master/readme-FFMPEG.md



- you can get timestamps for each shot of a video




# Moviepy

**a Python module for video editing**
https://zulko.github.io/moviepy/

Sam also made a video library
https://antiboredom.github.io/vidpy/


## Install
    $ pip3 install moviepy



## Usage

We’ll get a video (of a specific quality)

    $ youtube-dl https://www.youtube.com/watch?v=iMJTAMOakCw -f 18 -o sunset.mp4

and in python:
someclips.py

    # We can import a whole submodule, or just what we need
    # But now we'll just import it whole
    import moviepy.editor as mp
    
    # We make clip objects, can contain videos, images, text or colors
    # And you assemble them together into a final video
    # it's a bit like Premiere but without a graphic interface
    
    video1 = mp.VideoFileClip("baby.mp4")
    video2 = mp.VideoFileClip("sunset.mp4")
    
    clips = [video1, video2]
    finalclip = mp.concatenate_videoclips(clips) # takes a list of clips
    
    # Save it to a file
    finalclip.write_videofile("sunsetbaby.mp4")
    

Tips:

- it’s pretty slow
- Use [VLC](https://www.videolan.org/vlc/)
- use the compose method
    # We can add parameters to change the behavior of how it handles multiple videos
    mp.concatenate_videoclips(clips, method="compose")



## Getting certain parts of videos
    
    # Gets a sub clip from second 1 to second 2.5
    video1 = mp.VideoFileClip("baby.mp4").subclip(1, 2.5)
    


    
    # We can also load the whole video first and then get subclips, to do editing
    
    video1 = mp.VideoFileClip("baby.mp4")
    video2 = mp.VideoFileClip("sunset.mp4")
    clips = [ video1.subclip(1,2), video2.subclip(1, 2), video1.subclip(3,4) ]
    



## Doing more interesting things: getting random segments


    import moviepy.editor as mp
    import random
    
    
    video1 = mp.VideoFileClip("baby.mp4")
    video2 = mp.VideoFileClip("sunset.mp4")
    
    clips = []
    for i in range(0, 10):
      # Get a random starting point
      start = random.randrange(0, 5)
      # Get an ending point that's one second after the start point
      end = start + 1
      # Get a sub clip
      c = video1.subclip(start, end)
      # Add it to the list
      clips.append(c)
    
    finalclip = mp.concatenate_videoclips(clips)
    finalclip.write_videofile("randombaby.mp4")
    



## Compositing videos together


    import moviepy.editor as mp
    import random
    
    video1 = mp.VideoFileClip("baby.mp4")
    video2 = mp.VideoFileClip("sunset.mp4")
    
    clip1 = video1.subclip(0, 3)
    clip2 = video2.subclip(0, 5)
    
    # We can resize the video
    clip1 = clip1.resize(width=200)
    # And position it
    clip1 = clip1.set_pos((200, 100))
    # Don' t play the baby until the first second
    clip1 = clip1.set_start(1)
    
    clips = [clip1, clip2]
    
    # We'll use composite
    finalclip = mp.CompositeVideoClip(clips)
    
    finalclip.write_videofile("randombaby.mp4")
    



# Videogrep
https://github.com/antiboredom/videogrep


Get video cuts by searching text from a video


    $ pip3 install videogrep

the video file needs to have a subtitle 

- an .srt or .vtt file
- get subtitles for movies / tv shows https://subscene.com/ https://www.yifysubtitles.com/ 
- from youtube, download subtitles using youtube-dl
    - $ youtube-dl [URL] —write-auto-sub

You can also detect words from a video, installing:

    $ brew install pocketsphinx


- If your subtitles are .vtt, add
    - **--use-vtt**


## Usage
    # Basic usage:
    $ videogrep --input path/to/video_or_folder --search 'search phrase'
    
    $ videogrep -i video.mp4 -s 'letter' --use-vtt

You can use -n to see the ngrams, how many times each word appears in the video

    $ videogrep -i video.mp4 --use-vtt -n

By default it’ll extract the whole sentence where the word you’re searching for is in, but you can also extract just the word. (only works for .vtt subtitles)

    $ videogrep -i -s 'letter' --use-vtt --search-type word

**Demo mode**
You can see what the output will be without exporting the video by adding --demo

**Regular expressions**
The input for the word also takes **regular expressions** (a way to search in text using a codified little string)

    
    # letter|vowel  searches for letter OR vowel
    # ^a            searches for words that begin with the letter a
    # ing$          words that end with ing
    $ videogrep -i video.mp4 -s 'letter|vowel' --use-vtt --search-type word
    


- For more info and help with regular expressions:
    - https://regex101.com/

**Multiple videos**
The input can be multiple videos, e.g *.mp4 matches all the mp4 files in the folder the script is in

    
    # Find all the sentences with the word what across all the mp4 videos in this folder
    $ videogrep -i *.mp4 'what'
    



## Transcribing the video yourself

If there’s no .vtt file, we can use the transcribe parameter

- Takes a bit to do it
- accuracy is very bad
- by default only works in English
    $ videogrep -i video.mp4 --transcribe

and then to use the transcript, use --use-transcript

    $ videogrep -i video.mp4 -s 'hello' --use-transcript



# Etc

Get precise transcripts with timestamps per word

- https://lowerquality.com/gentle/



# Assignment

Make a video (or series of videos)

