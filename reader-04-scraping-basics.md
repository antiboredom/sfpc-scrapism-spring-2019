# Reader 04 - Web Scraping Basics

In this reader we'll cover the very basics of web scraping with Python.

Although it's possible to use Python's standard library to scrape the web, it's much easier to use a third-party web scraping package. There are a number of these available and all have merits. For the sake of this tutorial we will use a package called [requests_html](http://html.python-requests.org/) which I like because it is relatively easy to use for simple scraping tasks and builds on the work of many other high-quality projects.

## Installing Python packages with `pip`

To install a python package, open up your terminal and navigate to the folder where your project lives.

You can either install packages globally on your system, or you can set up a per-project "virtual environment". 

In this case we are installing a package called `requests_html`.

To install it globally just type:

```
pip3 install requests_html
```

`requests_html` will now be installed on your system and available to all your python scripts. Note: you may need to type `sudo pip3 install requests_html` if your computer complains about permissions.

You can also install it locally in your project folder. This is the recommended practice.

To do this, you must first create a virtual environment: a folder where all your project packages will live. Every time you start a new project you will first create a virtual environment using the command line tool `virtualenv`. Type:

```
virtualenv -p python3 env
```

Note: the `-p python3` tells virtualenv that you want to use python3, and the `env` names the folder to be created. 

You will now see a folder called `env` in your project. You may name this whatever you like.

Then you must "activate" your virtualenv:

```
source env/bin/activate
```

You should see that your prompt has changed, and now begins with `(env)`. This indicates that you have successfully activated the virtual environment.

Finally you can install the library:

```
pip install requests_html
```


## Basics

The basic workflow for most scraping projects is:

1. Download html from a url
2. Identify what elements you are interested in extracting
3. Extract text or attributes via CSS selectors

To use `requests_html`, first import the library and create an HTMLSession object

```python
# import the requests library
from requests_html import HTMLSession

# create a session object
session = HTMLSession()
```

Then use `session.get` to request the content of a url:

```python
# get the front page of the New York Times website
response = session.get('https://nytimes.com/')
```

Now you can use css selectors to pull out certain elements with the `find` method, which takes a css selector and returns a list of matching elements.

```python
# get a list of all h1 tags based on css selectors
titles = response.html.find("h1")
for t in titles:
	print(t.text)
```

The `find` method can take any css selector. For example:

```python
all_header_tags = response.html.find("h1,h2,h3,h4,h5,h6")

links_with_a_classname = response.html.find("a.cool-link")

images_inside_divs_inside_main = response.html.find("#main div img")
```

If you just want a single element rather than a list of them, add `first=True` to `find`

```python
# the first headline
title = response.html.find("h1", first=True).text
```

You can extract text with from elements using the `text` keyword, or you can extract html attributes with the `attrs` dictionary. For example:

```python
# get all urls linked to from the page
links = response.html.find('a')
for link in links:
	print(link.attrs.get("href"))
	
# get all image urls
images = response.html.find('img')
for image in images:
	print(image.attrs.get("src"))
```

### Nested elements

You can also call `find` on other elements. For example, imagine the following HTML structure:

```html
<article>
	<h2>Near the Wild Heart</h2>
	<span>Clarice Lispector</span>
</article>

<article>
	<h2>The Man Without Qualities</h2>
	<span class="author">Robert Musil</span>
</article>

<article>
	<h2>Orlando</h2>
	<span class="author">Virginia Woolf</span>
</article>
```

To extract titles and authors, you might do something like this:

```python
books = response.html.find('article')
for article in articles:
	title = article.find('h2', first=True).text
	author = article.find('.author', first=True).text
	print(title, author)
```


## Javascript

Quite frequently you'll find that `requests_html` fails to find the elements that are visible on the screen when you load a page up in a browser. This is typically (but not always) because the page is loading content with Javascript **after** the initial HTML is loaded. This is extremely common, but fortunately, requests_html has the ability to load pages with Javascript using the `render` function. Please note that this literally downloads an entire new version of Chrome to your home folder the first time you call it.

```python
from requests_html import HTMLSession

session = HTMLSession()

response = session.get('https://www.nytimes.com/')
response.html.render()
```

## Pagination

to come!



