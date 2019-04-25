# Binary Poem

It kind of failed but the idea was to discover sentences in binary data representing poetry. It takes an image of poetry text, converts the image binary data into string content, extracts any dictionary words from within the binary and displays them in the order they occur as a poem.  If there is metadata in the image it tends to show up. It ended up being more an exploration of random than uncovering hidden data. It however was a lot of fun.
Command line code (it should work on any image): https://gist.github.com/josephwilk/ba1299cd9b3c1a3802828ad9386c573c

## Code:
```
    $2 = /usr/share/dict/words
    #Fetch binary data
    wget $1 -O data

    #convert into strings
    strings data | sed 's/\([A-Z]\)/ \1/g' | sed 's/[^a-zA-Z]//g'| tr '[:upper:]' '[:lower:]' | tr -s '[:blank:]' '\n'  > strings.txt

    #Find dictionary words in data
    awk 'length > 2' strings.txt > strings.big.txt
    awk 'FNR==NR{dict[$1]++;next} {for(i=1;i<=NF;i++)if(!($i in dict))next}1' /usr/share/dict/words       strings.big.txt  | uniq > words.txt
    awk 'FNR==NR{dict[$1]++;next} {for(i=1;i<=NF;i++)if(!($i in dict))next}1' /usr/share/dict/connectives strings.txt  | uniq > connect.txt

    #join connectives and words
    paste -d '\n' connect.txt words.txt | tr \\n ' '
```

Binary image (it knows nothing of the text in the process):

![](https://paper-attachments.dropbox.com/s_E6FFE5B9575B776EB1E8573293D7DCC5A5A19326139E5B4341057D14F19F0048_1553727704614_image.png)

## Poem discovered:
```
    be vum
    a lag
    i yap
    a awn
    it fly
    i yow
    up mae
    so yin
    a goi
    i ova of
```

Poem discovered
```
    mr text
    a bet
    i run
    he rame
    a ach
    i feu
    a dry
    or rab
    be cro
```
