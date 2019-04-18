# Books shared illegally on PirateBay

__Goal__: To explore the sensitivity of Machine learning and its misuse when looking at models trained on different languages.

Scrapped Source data is a 1000 of the most popularly ebook titles that are shared illegally on PirateBay (https://thepiratebay.org).

I’m partially interested in the fragility and mis-use of machine learning. We are purposely using data that the models have not been trained on and comparing what this means in terms of output.

## Nouns through many language models

Turning book titles into nouns and then feeding that back into the next language model. So the output is nouns processed by every single language model:

__Effectively which words are recognised as nouns in all the language models.__

Sorted by frequency.


```
   ['Duryodhanization', 'Delusion', 'Version', 'Presidents', 'Burning', 'Religion', 'Cryptocurrency']
```

## Book Similarity across Corpus

For each, based on titles finding the most similar books for each language training model.

__Effectively which book title has most in common with all the other book titles in different languages.__


    # *English* - en_core_web_md
    * The Fall of Crazy House by James Patterson - (similar to 111 books)
    * All That You Leave Behind by Erin Lee Carr - (similar to 81 books)
    * War! What Is It Good For by Ian Morris - (similar to 73 books)

    # *Deutsch* - de_core_news_md
    * Venit S. Prelude to Programming. Concepts and Design 6ed - (similar to 409 books)
    * Martha Stewart's New Pies and Tarts-Martha Stewart - (similar to 405 books)
    * Spence L. Elementary Linear Algebra. A Matrix Approach 2ed (similar to 405 books)

    # *French* - fr_core_news_md
    * The Electrical Menagerie by Mollie E. Reeder - (similar to 776 books)
    * The Endless King by Dave Rudden - (similar to 775 books)
    * Erased: The Untold Story of the Panama Canal - Marixa Lasso 2019 - (similar to 769 books)

    # *Spanish* - es_core_news_md
    * Surprisingly Down to Earth, and Veryny- Brian Limond - (similar to 50 books)
    * Venit S. Prelude to Programming. Concepts and Design 6ed - (similar to 50 books)
    * Serway R. Principles of Physics.A Calculus-Based Text 5ed - (similar to 50 books)

    # *Portuguese* - pt_core_news_md
    * Bolder: Making the Most of Our Longer Lives by Carl Honore (similar to 543 books)
    * Bruce Springsteen's Born in the USA by Geoffrey Himes - (similar to 538 books)
    * Stevie Wonder's Songs in the Key of Life by Zeth Lundy- (similar to 537 books)

    # *Italian* - it_core_news_md
    * They Were Her Property: White Women As Slave Owners in the Ameri - (similar to 218 books)
    * Anton Elementary Linear Algebra.Applications Version 11ed - (similar to 217 books)
    * Dutch Girl: Audrey Hepburn and World War II-Richard Matzen  2019 - (similar to 217 books)

    # *Greek* - el_core_news_md
    * The Devil's Dice by Roz Watkins
    * Late Bloomers by Rich Karlgaard
    * All My Colors by David Quantick

    # *Dutch* - nl_core_news_md
    * The Death Gap: How Inequality Kills - David A. Ansell, Peter Ber - (similar to 168 books)
    * Dutch Girl: Audrey Hepburn and World War II-Richard Matzen  2019 - (similar to 167 books)
    * Erased: The Untold Story of the Panama Canal - Marixa Lasso 2019 - (similar to 167 books)


## Python Source Code:
```
import spacy
import torch
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from matplotlib import pyplot

def clean(str):
    return str.replace('\n','').strip()

def scrubTitles(str):
    return str.replace("EPUB", "").replace("(epub)","")


def runSimilarity(doc, lines):
    match = {}
    for book in lines:
        base_sentence = nlp(book)
        match[book] = []
        for sent in doc.sents:
            sim = sent.similarity(base_sentence)
            if((sim > 0.8) and (sent.text.strip() != book.strip())):
                match[book].append(clean(sent.text))

    sorted_matches = sorted(match.items(), key=lambda x: len(x[1]), reverse=True)

    for k,v in sorted_matches:
        if v:
            file.write(clean(k)+"\n")
            print(clean(k))
            for v in v:
                file.write("  *  "+clean(v)+"\n")
                print("  *  "+clean(v))
    file.write("\n")
    file.close()


def runNounChain(doc):
    nouns = []
    for word in doc:
        if word.pos_ == "NOUN":
            nouns.append(word.text)
    return nouns


raw_text = scrubTitles(open("torrented_books.txt", "r").read())
raw_lines = raw_text.split("\n")
lines = [line.strip() for line in raw_lines]
text = [line.split(" ") for line in raw_lines]

nlps = ['en_core_web_md',
        'fr_core_news_md',
        'de_core_news_md',
        'el_core_news_md',
        'es_core_news_md',
        'it_core_news_sm',
        'nl_core_news_sm',
        'pt_core_news_sm']

nouns = []

for lang in nlps:
    file = open("resources/"+lang+".txt",'w')
    file.write(lang +"\n")
    nlp = spacy.load(lang)
    doc = nlp(raw_text)

    nouns = runNounChain(doc)
    print("\n")
    print(nouns)

    raw_text = ' '.join(nouns).replace("n.","")
    #runSimilarity(doc, lines)

nouns = set(sorted(nouns, key = nouns.count, reverse=True))
print(nouns)

```
