# April 10th - Natural Language Processing
We’re in business


# Questions about homework

Amazon kicked me out

- They know you’re not a person
  - When your browser reads a website it sends data about what kind of browser it is. Whe you’re using requests_html it’s not sending that. 
  - The best thing to do is to tell amazon you’re a web browser. It’s called **User Agent Spoofing**
  - It sometimes helps if you have an Amazon account, and login as yourself and scrape as yourself that will frequently prevent them from blocking you. but if they block you they might block your account. **We’ll share how to do that**




# Today

How to scrape things when things are loaded with Javascript
How to deal with being blocked
Natural Language Processing


# How to not get blocked
## User Agent Spoofing
https://www.scrapehero.com/how-to-fake-and-rotate-user-agents-using-python-3/


A user agent is a string that a browser or app sends to each website you visit. A typical user agent string contains details like – the application type, operating system, software vendor or software version of the requesting software user agent. Web servers use this data to assess the capabilities of your computer, optimizing a page’s performance and display. User Agents are sent as a request header called “User-Agent”.

Looks like

    User-Agent: Mozilla/<version> (<system-information>) <platform> (<platform-details>) <extensions>

You just wanna copy and paste that string

**Actually requests_html is already doing this for you**


## Other ways to not get blocked

**cURL**

1. Go to your page
2. View > Developer Tools
3. Go to the Network tab
4. See what it’s actually being passed around between the browser and the website
  1. click around
  2. the network requests being made are going to show up in the Network tab (all the images being loaded, all the CSS, javascript, etc.)
  3. You can mouse over the requests, click on things, see more information and their contents
5. Go all the way to the top and the very first request is going to be the actual page that got loaded
  1. The URL is the same as in the browser URL
  2. The right side will show a Preview
  3. You can go to the **Headers** tab, and see what request the browser made, **including cookies.**
6. Right click on the URL > Copy > Copy as cURL
  1. **This will copy the address and all the cookies** 
  2. **If you’re logged into the website**, you’ll be copying the state of the browser with your login
    1. Makes it so it’s virtually impossible for the website to differentiate between a request from a browser or your script

To test, in the terminal, you can run “curl [paste your content]” and get the

You can convert that request into python

**Convert curl commands to python request:**
https://curl.trillworks.com/

cURL of a google search:

    curl 'https://www.google.com/search?ei=dgOuXPe1LqTH_QabyrrIBw&q=this+is+my+search&oq=this+is+my+search&gs_l=psy-ab.3..0i22i30.12005.13509..13797...0.0..0.317.3062.1j9j4j2......0....1..gws-wiz.......0i71j0i67j0i131j0j0i13.x3O6SI8NwLQ' -H 'authority: www.google.com' -H 'upgrade-insecure-requests: 1' -H 'dnt: 1' -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36' -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3' -H 'referer: https://www.google.com/' -H 'accept-encoding: gzip, deflate, br' -H 'accept-language: en-US,en;q=0.9,es;q=0.8' -H 'cookie: CGIC=InZ0ZXh0L2h0bWwsYXBwbGljYXRpb24veGh0bWwreG1sLGFwcGxpY2F0aW9uL3htbDtxPTAuOSxpbWFnZS93ZWJwLGltYWdlL2FwbmcsKi8qO3E9MC44LGFwcGxpY2F0aW9uL3NpZ25lZC1leGNoYW5nZTt2PWIz; NID=181=C71PGie0O4KzdtbxOyGsgukThOnT2ufa0DaXx5-5YMvMEBGJoHLSHJGYPCzA_E022skZcFgpVFiAPRgSolwEqHxnK4xmAqbRjtezgKAGvBtpz-4oSNBuCLhlmDlJsyFQ_Xg-_QLXgCjd1KxG_E9TZzL8eAMip9-MCG6uTocwjZI; 1P_JAR=2019-04-10-14; DV=83zs6xTNaAsk8D1GDcTKiA_jpdh7oFZ_Q3x9eM9c1wIAAAA' --compressed

Converted to python:

    import requests
    
    headers = {
        'authority': 'www.google.com',
        'upgrade-insecure-requests': '1',
        'dnt': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'referer': 'https://www.google.com/',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9,es;q=0.8',
        'cookie': 'CGIC=InZ0ZXh0L2h0bWwsYXBwbGljYXRpb24veGh0bWwreG1sLGFwcGxpY2F0aW9uL3htbDtxPTAuOSxpbWFnZS93ZWJwLGltYWdlL2FwbmcsKi8qO3E9MC44LGFwcGxpY2F0aW9uL3NpZ25lZC1leGNoYW5nZTt2PWIz; NID=181=C71PGie0O4KzdtbxOyGsgukThOnT2ufa0DaXx5-5YMvMEBGJoHLSHJGYPCzA_E022skZcFgpVFiAPRgSolwEqHxnK4xmAqbRjtezgKAGvBtpz-4oSNBuCLhlmDlJsyFQ_Xg-_QLXgCjd1KxG_E9TZzL8eAMip9-MCG6uTocwjZI; 1P_JAR=2019-04-10-14; DV=83zs6xTNaAsk8D1GDcTKiA_jpdh7oFZ_Q3x9eM9c1wIAAAA',
    }
    
    params = (
        ('ei', 'dgOuXPe1LqTH_QabyrrIBw'),
        ('q', 'this is my search'),
        ('oq', 'this is my search'),
        ('gs_l', 'psy-ab.3..0i22i30.12005.13509..13797...0.0..0.317.3062.1j9j4j2......0....1..gws-wiz.......0i71j0i67j0i131j0j0i13.x3O6SI8NwLQ'),
    )
    
    response = requests.get('https://www.google.com/search', headers=headers, params=params)

Then you can change the params to manipulate pages, or searches, etc.


## When things load with Javascript

e.g. a page has “show more” that doesn’t reload the page


1. Use the Network tab
2. click show more, and see what new things appear
3. click on one of them
4. go to the Preview tab
  1. one of them will have a mess of text 
  2. by opening them you can see your data coming in
  3. The format will be a **dictionary** (keys and values)

Getting it in python:

1. Copy the request as cURL, convert it to python


    import requests
    
    headers = {
     # bla bla bla
    }
    data = "..... a mess"
    
    print(response.text) # Output: a dictionary with all the data
    
    # Convert to a python dictionary
    data = response.json()
    
    # Access the data you need by following the path to your data from the Preview tab
    items = data\["data"\]["legacyCollection"]\["stream"\]["edges"]
    for item in items:
      print(item\["node"\]["summary"])


# About dictionaries

Lists are ordered lists of items
Dictionaries are lists of items but they’re not indexed numerically, but with strings


    
    # Making a new empty dictionary
    a_list = []
    a_dict = {}
    
    # Making a dictionary and assign its values
    person = {
      "first_name": "Karl",
      "last_name": "Marx",
      "alive": False,
      "favorite_books": ["something by Hegel", "the wealth of nations?"]
      "best_friend": {
        "name": "Engels",
        "alive": False
      },
      # keep adding as many as you want
    }

Access a value by its string name

    print(person["first_name"])  # Output: Karl
    print(person\["favorite_books"\][0]) # Output: something by Hegel

You can set values

    person["first_name"] = "KARL@!!" # Overwrites the name
    person["favorite_beverage"] = "Coke" # Adds a new key
    
    # Accessing a value from a key that doesn't exist will throw an ERROR 
    # and stop the program.
    person["asegdfgds"]
    # A safe way to access values is
    person.get("asegdfgds") # Tries to find the value but won't throw an error 
    

You can iterate through the keys and values

    
    # for .. in dict iterates through the *keys*
    for key in person:
      print(key)         # Output: first_name
      print(person[key]) # Output: Karl
    



# NLP

Natural Language Processing
gives you information about

- Parts of speech
  - is the word a noun, an adjective, an adverb
- to categorize text
  - is this sentence positive, negative
  - is this porn or not?
- and more!


We’re gonna be using spacy

https://spacy.io/


There’s other ones
https://textblob.readthedocs.io/en/dev/
https://www.clips.uantwerpen.be/pages/pattern

NLP tends to be english focused


## Install spacy
    $ pip3 install spacy

You also need to install a language module
https://spacy.io/models/

each one has different training data, with pros and cons, accuracy and file sizes (that determine how fast it is to use)

We’ll use **en_core_web_sm** for now

    $ python3 -m spacy download en_core_web_sm


## Using spaCy
    import spacy
    
    nlp = spacy.load("en_core_web_sm")
    
    text = "A specter is haunting SFPC. The specter of chocolate dessert."
    
    # we add text to spacy
    doc = nlp(text) # returns a spacy Doc object

We can iterate through each word of the text (**tokenization**)

    for word in doc:
      print(word)

or the sentences

    for sentence in doc.sents:
      print(sentence)
      for word in sentence:
        print(word)


## Using Part Of Speech to determine what kind of word it is
- word.pos_ returns the **part of speech**
- word.tag . is more speficic than part of speech, with a different syntax
    for word in doc:
      print(word) # Output is each word
      print(word.pos_) # NOUN / VERB / PUNCT / etc etc
      print(word.tag) 
    

**Full list of tags and what they mean**
https://spacy.io/api/annotation#pos-tagging

![](https://paper-attachments.dropbox.com/s_0CE8D24B10EDC3B5D2F303C16C90A7C93163C4314D1475F0139EFD097E35D2A7_1554911989977_image.png)


Tags follow the Penn Treebank scheme
https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html

e.g. you can **collect all the nouns or verbs**

    nouns = []
    verbs = []
    gerunds = [] # verbs ending in -ing
    for word in doc:
      if word.pos_ == "NOUN":
        nouns.append(word)
      if word.pos_ == "VERB":
        verbs.append(word)
      # using the tag (using penn treebank)
      if word.tag_ == "VBG":
        gerunds.append(word)
      

You can get the **lemma** of a word (whatever’s the most basic version of a word)

    for word in doc:
      print(word.lemma_)


## Entities

*A named entity is a “real-world object” that’s assigned a name – for example, a person, a country, a product or a book title*
https://spacy.io/usage/linguistic-features#named-entities


    for entity in doc.ents:
      print(entity.text)
      print(entity.label_)
![](https://paper-attachments.dropbox.com/s_0CE8D24B10EDC3B5D2F303C16C90A7C93163C4314D1475F0139EFD097E35D2A7_1554912908741_image.png)



## Using it all together

Get unique chunks

    import spacy
    nlp = spacy.load("en_core_web_sm")
    
    text = open("manifesto.txt", "r").read()
    
    chunk = []
    for chunk in doc.noun_chunks:
      chunks.append(chunk.text)
    
    # Make the list unique (remove duplicates)
    chunks = set(chunks)

**Using the Counter library to get information about a list**
automatically counts up all the items of a list

    import spacy
    from collections import Counter
    
    nlp = spacy.load("en_core_web_sm")
    
    text = open("manifesto.txt", "r").read()
    
    chunk = []
    for chunk in doc.noun_chunks:
      chunks.append(chunk.text.lower()) # turn word to lower case version
    
    counts = Counter(chunks)
    print(counts)
    # { 'word1': 5, 'word2': 3 }
    
    # Get the 10 most common noun chunks (returns a list of tuples)
    counts.most_common(10)
    
    # or process them like
    for word, count in counts.most_common(20):
      print(word + " appears " + count + " times.")
    


## Using vectors

Basically, words can be represented as vectors (giant numbers) for the sake of comparing them

To use word vectors you’ll need to install at least a medium-sized model

    $ python3 -m spacy downlad en_core_web_md



    import spacy
    nlp = spacy.load("en_core_web_md")
    
    text = "A specter is haunting this classroom. The specter of summer"
    doc = nlp(text)
    
    word2 = nlp("ghost")
    # Compare our word to each word in the text and see which one is the 
    # most statistically similar to it
    for word1 in doc:
      similarity = word1.similarity(word2) # a number from 0..1 
      


## Avoiding certain words
    
    ignore_words = ["hello", "bad", "word"]
       
    for chunk in doc.noun_chunks:
      if chunk.text.lower() in ignore_words:
        continue
      print(chunk + " is an allowed word")
    


## Processing sentences instead of words


    words = nlp("this is a sentence")
    for sentence in doc.sents:
      similarity = sentence.similarity(words)

Print only very similar sentences

    import spacy
    nlp = spacy.load("en_core_web_sm")
    text = open("manifesto.txt", "r").read()
    doc = nlp(text)
    
    base_sentence = nlp("Death to capitalists!")
    
    for sent in doc.sents:
      sim = sent.similarity(base_sentence)
      if sim > 0.7:  
        print(sent.text)
    


## Cleaning up the source text and removing line breaks so it’s easier to analyze
    # get rid of line breaks
    text = text.replace("\n", " ")


# Homework

TBD


