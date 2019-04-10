# April 4 - HTML



# Bigrams

unigrams: single words

- “a”
- “specter”
- “is”

bigrams: every two word combination

- “a specter”
- “specter is”
- “is haunting”

trigrams: etc.

- “A specter is”
- “specter is haunting”

can be used as words or as characters
useful to find common phrasing



# HTML

All websites share their source code by default

In Chrome, you can go to View > Developer > View Source, to see the source code of any website
Or hit Right Click > View Source

HTML is made of **elements** and **tags**

- tags are in between < and >
- we open a tag <tagname> and close it with </tagname>
    <tagname>content</tagname>

e..g the p tag denotes a paragraph

    <p>This is a paragarph</p>

a link is the **a** tag, and contains an **attribute** href and its value is the link

    <a href="http://www.google.com">Go to google</a>

Other common tags:

- **div** is an arbitrary division, useful later
- **h1** is a header, also **h2, h3, h4** are smaller headers


Tags can have **attributes**

- some are exclusive to their tags, href only works on **a** tag
- some can be applied to any tag, the one’s we’ll mostly use are
  - id
  - class
    
    <!-- This paragraph now is uniquely identifiable by its id -->
    <p id="a-very-important-paragraph">This is a paragraph</p>
    
    <!-- A class can be applied to more than one tag -->
    <p class="a-normal-paragraph">This is another paragraph</p>
    

The basic structure of an HTML page is

    <html>
      <head>
        <!-- This is where tags that define properties for the page go -->
      </head>
      <body>
        <!-- This is where the part of the page that'll be rendered is -->
      </body>
    </html>


# CSS

HTML is the structure and content of a page
CSS defines how it **looks like**.

CSS can be embedded inside an HTML page, or be a separate file that’s linked to the page.

We can embed it in HTML using the <style> tag

    
    <style>
    
    </style>

in CSS we define a selector, and properties that apply to it:

- Make all the p tags (paragraphs) have a font color that’s red:
    p {
      color: red;
    }

You can have tags inside tags, and in CSS target them:

- a selector followed by another one targets all the tags inside the parent tag
- e.g.: all the bold tags inside paragraph, color them orange
    
    <p>This is a <b>paragraph</b><p>
    
    <style>
    p {
      color:red;
    }
    p b {
      color: orange;
    }
    </style>

You can access a specific **class** with period

    <p class="weird-paragraphs">This is a weird paragraph</p>
    <p class="weird-paragraphs">This is another weird paragraph</p>
    
    <style>
    .weird-paragraphs {
      color:red;
    }
    </style>

You can access a specific **id** with numeral

    
    <p id="a-specific-paragraph">This is a specific paragraph</p>
    <p>This is a normal paragraph</p>
    
    <style>
    #a-specific-paragraph {
      color:red;
    }
    </style>


# Using the chrome Inspect feature

To find a specific element on a page, on chrome you can Right Click > **Inspect**

- Hovering over the HTML will highlight those parts on the page
- You can edit the HTML text and it’ll change the page

Useful:

- [Toggle Javascript](https://chrome.google.com/webstore/detail/toggle-javascript/cidlcjdalomndpeagkjpnefhljffbnlo) chrome extension, turn Javascript off

IF we wanted to, say, open the New York Times and change the headlines

- We inspect the part of the page we want to target (e.g. a headline)
- We analyze the structure
  - the headline is in an <h2> tags. therefore most h2 tags will probably be headlines
- We open the Console tab, to try and find it
  - This is in javascript, but the function inside the function is a CSS selector
  - we’re gonna do this in python in our script, this is for testing if we find the text that we want
    
    > var headlines = document.querySelectorAll("h2");
    
    > headlines
    // prints out all the elements with an h2 tag
    
    // we can iterate on them
    > for (var i =0 ; i < headlines.length; i++) { 
      console.log(headlines[i].textContent);
    } 
    
    // and change them
    > for (var i =0 ; i < headlines.length; i++) { 
      headlines[i].textContent = "Lol capitalism";
    } 


If we wanted to find elements by its class

    > document.querySelectorAll(".title");



# Doing this in python

We’re gonna use a python library to parse HTML easily

requests-html: https://github.com/kennethreitz/requests-html
Documentation: https://html.python-requests.org/


## Install

on the terminal:

    $ pip3 install requests_html


## Use
    
    # Import the part of the library we'll use
    from requests_html import HTMLSession
    # Make a session object
    session = HTMLSession()
    # Tell the session object to download a website
    response = session.get("https://nytimes.com")
    
    # e.g. Print out the source of the page
    print(response.html.html)
    
    # Find something on the page
    # find() is the equivalent of the Inspect console function we used
    # Find all the h2 tags
    titles = response.html.find("h2")
    for t in titles:
      print(t) # prints out the actual python object element
      print(t.text) # prints out the text content



## Parsing craigslist
1. Find titles
2. For each one, get the URL of its link
  1. We use the **attrs** property to access the “href” link attribute
3. Open the URL and get the post content
    
    from requests_html import HTMLSession
    session = HTMLSession()
    r = session.get("https://newyork.craigslist.org/d/volunteers/search/vol")
    
    # find the titles by their class
    titles = r.html.find(".result-title")
    for t in titles:
      print(t.text)
      post_title = t.text
      # find the url in the <a> tag
      post_url = t.attrs.get("href")
      # make another session (we can override the old one)
      r = session.get(post_url)
      # find the post description by its tag's id
      # .  we add the first=True parameter to only get the first match, instead of a list
      body = r.html.find("#postingbody", first=True)
    



Don’t get banned

- import the time module to make the script wait between server calls and avoid rate limiters and not overload their servers
    import time
    
    time.sleep(0.5)



## When we need javascript
- we use r.html.render() to load up the page fully, in an invisible version of Chrome
    
    from requests_html import HTMLSession
    session = HTMLSession()
    r = session.get("")
    
    # render the full page, including javascript scripts
    r.html.render()
    
    articles = r.html.find('article')
    
    for a in articles:
      # Find the h2 tag
      title = a.find('h2', first=True)
      # Find the part that stores the comment count
      comments = a.find('.byC', first=True)
    
      print(comments.text, title.text)
    



## Bonus: using CURL to scrape a page including your cookies

For pages like instagram, facebook, etc. Chrome lets you monitor the network and get a 
https://curl.trillworks.com/

  




# Homework

Make a big list

- if you look at the requests html documentation there’s a few really easy ways of using pagination to get several pages, or go through all the results of a search
  - e.g. by clicking the “next” button
  - find the next button, tell requests_html to get that url, OR you can use the pagination feature to automatically get all the results of a search
  - works sometimes
![](https://paper-attachments.dropbox.com/s_AD45F3265395457B5C981140E6626B079633CB7A6499178E7BD35638D0145DA7_1554396968170_image.png)


Use python to make a giant list, whatever list you wanna make
The point is to try out some web scraping and think about the creation of a list or an archive as itself a work.
why do you pick one material over another
Ideally thousands of things.

Some websites are extremely difficult to scrape, or extremely easy. If one’s too hard try an easier one.



