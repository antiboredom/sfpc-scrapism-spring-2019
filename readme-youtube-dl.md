# youtube-dl

[youtube-dl](https://rg3.github.io/youtube-dl/) is a great command line program that you can use to download video from a bunch of different sources (YouTube, Vimeo, Facebook, and many more).

### Installation

```
brew install youtube-dl
```

### Basic Usage

To download a video, just type youtube-dl and the url of the video you want
```
youtube-dl http://youtube.com.com/somevideo
```

For example:

```
youtube-dl https://www.youtube.com/watch?v=3TuwN0DmNeU
```

You can also download an entire user, channel or playlist. For example this will download the entire whitehouse channel (it will take a long time).

```
https://www.youtube.com/user/whitehouse/
```

### File formats

Websites like youtube and vimeo will store videos in multiple file formats and sizes. To get a list of all of them for a video, simply add the `-F` option:

```
youtube-dl [URL] -F
```
 
You can choose a specific format with `-f` and the code for that format

```
youtube-dl [UDL] -f 22
```

Some formats let you download only the video, or only the audio


### Change the output

By default youtube-dl will automatically select a filename to save to. To override this, add the `-o` flag.

```  
youtube-dl [URL] -o whatever.mp4
```    



### Always save mp4s

```    
youtube-dl [URL] --merge-output-format mp4
``` 



### Download subtitles

```    
youtube-dl [URL] --write-auto-sub --skip-download
``` 

### Get the URLS of the video and audio

```    
youtube-dl [URL] --get-url
``` 


