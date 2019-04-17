# Reader 05 - Natural Language Processing

Natural language processing (or NLP) describes the field of computer science dealing with human language. In very brief, NLP encompasses a series of techniques by which computers can make "sense" of text. Common NLP tasks include: tagging words with different parts of speech, extracting "named entities" (people/places/countries/brands etc) from text, splitting text into words and sentences, and categorizing text. And propaganda bots!

There are a number of natural language processing libraries available for Python, like NLTK, TextBlob, Pattern, pyText, and Spacy.

In this reader we'll be using Spacy, but feel free to explore the other libraries (each as its own benefits and drawbacks).

## Installing Spacy

To install spacy, you must install both the library itself as well as a language model (the data spacy uses).

First, install the library:

```
pip install spacy
```

Then, you can choose what language model you'd like to use. At the time of writing, Spacy provides language models in English, German, French, Portugese, Italian, Dutch and Greek. These models have typically been trained on written text from news sites and the internet.

Each language may also have multiple model options which vary by size and accuracy. In this tutorial we'll install the small-sized English model (10mb), but feel free to experiment, as each model will likely yield different results. For a full list see [Spacy Models](https://spacy.io/models/).

To download the model:

```
python -m spacy download en_core_web_sm
```

To use Spacy in your python scripts, just import the library and load the model:

```python
import spacy
nlp = spacy.load("en_core_web_sm")
```

## Sentences and Words

A very basic NLP task is to break a text up into sentences and individual words.  To do this in Spacy, we create a Spacy `Doc` object. 

```python
import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("A specter is haunting Europe. The specter of NLP!")

# sentences live in the .sents attribute
for sentence in doc.sents:
	print(sentence.text) # .text is the actual text of the sentence
```

We can also easily extract individual words, or in NLP parlance "tokens". 

```python
import spacy
nlp = spacy.load("en_core_web_sm")

doc = nlp("A specter is haunting Europe. The specter of NLP!")
for token in doc:
	print(token.text)
```

## Parts of Speech

As you may recall from early childhood, words may be categorized into different parts of speech based usage. Nouns, verbs, adjectives, adverbs, and so on. Each token (word) in Spacy will have a `.pos_` attribute that describes its part of speech tag and a `.tag_` attribute (which is more specific)

```python
import spacy
nlp = spacy.load("en_core_web_sm")

doc = nlp("A specter is haunting Europe. The specter of NLP!")
for token in doc:
	print(token.text, token.pos_, token.tag_)

```

Using a list comprehension, one could easily extract all words of a particular category:

```python	
nouns = [t.text for t in doc if t.pos_ == "NOUN"]
```

We can also extract larger connected chunks of words out of a text, for example phrases with nouns:


```python
for chunk in doc.noun_chunks:
	print(chunk.text)
```


## Entities

You may also be interested in extracting person, place, product or brand names from text. These are called "named entities" and can be accessed through the `.ents` attribute.


```python
for entity in doc.ents:
	print(entity.text, entity.label_)
```

## Similarity

You can compare `Doc` and `Token` objects to each other to determine how similar they are to each other.

```python
import spacy

nlp = spacy.load('en_core_web_md')  # make sure to use larger model!
doc = nlp("A specter is haunting Europe. The specter of communism.")

for token1 in doc:
    for token2 in doc:
        print(token1.text, token2.text, token1.similarity(token2))
```
