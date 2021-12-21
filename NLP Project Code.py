# Round 1
"""

import nltk
import re

"""<br>

# Task-1: Import Two Books T1 and T2

Here we have imported two books from (https://www.gutenberg.org/ebooks/11) and  (https://www.gutenberg.org/ebooks/46) as opened as T1 and T2 using the open function of the OS library.

<br>
"""

filename="/content/Alice.txt"
f = open(str(filename), 'r', encoding="utf8")

T1 = f.read()
f.close()

"""<br>"""

filename="/content/Carol.txt"
f = open(str(filename), 'r', encoding="utf8")

T2 = f.read()
f.close()

"""<br>

# Task-2 : Text pre-processing and Tokenization

Text preprocessing:
First of all, we have cleaned the chapters name and all the other stuff which is not required for further processing.
Here, we have seen a pattern that after every 4 new empty lines we see chapter number and in the next line we see chapter name and two more new empty lines, which we removed using the REGEX, for both books T1 and T2 and called the now obtained books as T1_Clean and T2_clean.

<br>
"""

T1 = T1[T1.find("CHAPTER XII.")+len("CHAPTER XII.   Alice’s Evidence"):T1.find("*** END OF THE PROJECT GUTENBERG EBOOK")]
T1_clean = re.sub(r'\n{4}.*\n.*\n\n\n+', '\n\n', T1)
# print(T1_clean)

"""<br>"""

T2 = T2[T2.find("Stave   V")+len("Stave   V: The End of It"):T2.find("*** END OF THE PROJECT GUTENBERG EBOOK")]
T2_clean = re.sub(r'\n{3}.*\n\n+', '\n\n', T2)
print(T2_clean)

"""<br>

Tokenization: Then the next step was to tokenize both the books, for that we have imported word_tokenizer from nltk.tokenize. Then we one by one we have tokenized both the cleaned books and stored the resultant (tokenized) list in Token_T1 and Token_T2 for book T1 and T2 respectively.

<br>
"""

import nltk
nltk.download('punkt')

from nltk.tokenize import word_tokenize

Token_T1=word_tokenize(T1_clean)
Token_T1

"""<br>"""

from nltk.tokenize import word_tokenize

Token_T2=word_tokenize(T2_clean)
# Token_T2

"""<br>

# Task-3 : Freq Distribution Of T1 and T2

Here in this step before finding the distribution, we have removed all the punctuation and the numerical values, i.e. everything except the alphabetical words, so that they don’t pop in the frequency table/curve, and make our findings wrong.

<br>
"""

import re
punctuation = re.compile(r"[^a-zA-Z]+")
T1_only_words = []
for words in Token_T1:
  words = punctuation.sub("", words)
  if len(words) > 0:
    T1_only_words.append(words.lower())
# print(T1_only_words)
Token_T1 = T1_only_words

"""<br>"""

import re
punctuation = re.compile(r"[^a-zA-Z]+")
T2_only_words = []
for words in Token_T2:
  words = punctuation.sub("", words)
  if len(words) > 0:
    T2_only_words.append(words.lower())
# print(T2_only_words)
Token_T2 = T2_only_words

"""<br>

Then we have imported the FreqDist function. And took the count for frequency for each word. We did so for both Token_T1 and Token_T2. Then we took the 20 most common words for both books, using most_common() available in FreqDist through nltk.probability.

<br>
"""

from nltk.probability import FreqDist

"""<br>"""

fdist_T1=FreqDist()
for word in Token_T1:
    fdist_T1[word]+=1
fdist_T1

"""<br>"""

fdist_T2=FreqDist()
for word in Token_T2:
    fdist_T2[word]+=1
fdist_T2

"""<br>"""

fdist_T1_top20 = fdist_T1.most_common(20)
fdist_T1_top20

"""<br>"""

fdist_T2_top20 = fdist_T2.most_common(20)
fdist_T2_top20

"""<br>

Here we have plotted for the 20 most common words for both the books, and clearly word ‘the’ is the most common word in both the books, but that’s could be deceptive as `the` is a stopword, which will be taken care in next steps, and then we’ll plot again and will see how the plot changes.

<br>
"""

fdist_T1.plot(20, cumulative=False)

"""<br>"""

fdist_T2.plot(20, cumulative=False)

"""<br>

# Task-4: Word Cloud Of T1 and T2

Now to show the wordcloud from frequency distribution we have used the wordcloud library along with the Matplotlib library.
As we can see here word `the`, which is most frequent so far is plotted the largest and other were also being plotted according to their frequency (before removing the stopwords).

<br>
"""

from wordcloud import WordCloud
import matplotlib.pyplot as plt

"""<br>"""

word_cloud_dict1 = fdist_T1
wordcloud1 = WordCloud(width = 500, height = 300).generate_from_frequencies(word_cloud_dict1)
plt.figure(figsize=(15,8))
plt.imshow(wordcloud1)
plt.axis("off")
plt.show()

"""<br>
<br>
<br>
"""

word_cloud_dict2 = fdist_T2
wordcloud2 = WordCloud(width = 500, height = 300).generate_from_frequencies(word_cloud_dict2)
plt.figure(figsize=(15,8))
plt.imshow(wordcloud2)
plt.axis("off")
plt.show()

"""<br>
<br>
<br>

# Task-5: Removal of Stop Words And Creating Word Cloud

Now, this is the time when we are separating stopwords from our list of tokens for both books. Here firstly we have found the stopwords for the English language. Then one by one, we examined all the tokens and if that token is not a stopword, we considered it for further processing and will store them in a new list, and the words left will be of no use and hence won’t include them in the new list. This way we have removed the stopwords from Token_T1 and Token_T2. Then we have again found the frequency distribution for the cleaned set of tokens and plotted the new word graphs. As we can see stopwords like ‘a’, ‘i’, ‘the’ are no more appear in the frequency distribution as well as in the word cloud. And thus the most frequent word for Book1 i.e. Alice’s adventures in Wonderland is ‘said’ and for Book2 i.e.  A Christmas Carol in Prose; Being a Ghost Story of Christmas is ‘scrooge’.

<br>
"""

import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
sr= stopwords.words('english')
clean_tokens_T1 = []

for token in Token_T1:
    if token not in stopwords.words('english'):
        clean_tokens_T1.append(token)

freq_T1 = nltk.FreqDist(clean_tokens_T1)

#for key,val in freq_T1.items():
   # print(str(key) + ':' + str(val))

"""<br>"""

from nltk.corpus import stopwords
sr= stopwords.words('english')
clean_tokens_T2 = []

for token in Token_T2:
    if token not in stopwords.words('english'):
        clean_tokens_T2.append(token)

freq_T2 = nltk.FreqDist(clean_tokens_T2)
# for key,val in freq_T2.items():
   # print(str(key) + ':' + str(val))

word_cloud_dict3 = freq_T1
wordcloud3 = WordCloud(width = 500, height = 300).generate_from_frequencies(word_cloud_dict3)
plt.figure(figsize=(15,8))
plt.imshow(wordcloud3)
plt.axis("off")
plt.show()

word_cloud_dict4 = freq_T2
wordcloud4 = WordCloud(width = 1000, height = 500).generate_from_frequencies(word_cloud_dict4)
plt.figure(figsize=(15,8))
plt.imshow(wordcloud4)
plt.axis("off")
plt.show()

"""<br>
<br>
<br>

# Task-6: Relationship Between Word Length And Frequency

Next, we are going to find the frequency distribution with the count. For that first, we have found various lengths of words for each cleaned set of words of each book. Then for each possible word size, we found the number of words with that size and then stored all the pair of word length and number of such length words and then converted it to the data frame, which we further plotted using the matplotlib library, and visualized the relationship between length and frequency for both cleaned token set of book T1 and T2.

<br>
"""

import pandas as pd

data = []

fdist_len_T1 = FreqDist()
for word in clean_tokens_T1:
    fdist_len_T1[len(word)] += 1

for key in sorted(fdist_len_T1):
    temp = []
    temp.append(key)
    temp.append(fdist_len_T1[key])
    data.append(temp)
    
df_T1 = pd.DataFrame(data, columns = ['Length', 'Count'])
print(df_T1)

"""<br>"""

import pandas as pd

data = []

fdist_len_T2 = FreqDist()
for word in clean_tokens_T2:
    fdist_len_T2[len(word)] += 1

for key in sorted(fdist_len_T2):
    temp = []
    temp.append(key)
    temp.append(fdist_len_T2[key])
    data.append(temp)

df_T2 = pd.DataFrame(data, columns = ['Length', 'Count'])
print(df_T2)

"""<br>"""

import matplotlib.pyplot as plt
plt.plot(df_T1['Length'],df_T1['Count'])
plt.plot(df_T2['Length'],df_T2['Count'])
plt.xlabel('Length of word')
# naming the y axis
plt.ylabel('Number of Word')
 
# giving a title to My graph
plt.title('Word Length and Frequency Comaprison for Both Garphs')
plt.show()
# Here Blue denotes Book T1 and orange denotes book2

"""<br>
<br>

# Task-7 : POS Tagging For T1 and T2

In this step, we have done the part of speech tagging for the words of each book. For this, we have used the nltk.pos_tag function which uses the Penn Treebank tags. Then to get the distribution of various tags we have used the Counter function and then and then printed the tag wise distribution in descending order, for both the token sets T1 and T2.

<br>
"""

import nltk
nltk.download('averaged_perceptron_tagger')

Token1_pos = nltk.pos_tag(clean_tokens_T1)
# Token1_pos

"""<br>"""

Token1_pos = list(map(list, Token1_pos))
# Token1_pos

"""<br>"""

Token2_pos = nltk.pos_tag(clean_tokens_T2)
# Token2_pos

"""<br>"""

Token2_pos = list(map(list, Token2_pos))
# Token2_pos

"""<br>"""

from collections import Counter
pos_tag_T1 = Counter(tag for _, tag in Token1_pos)

"""<br>"""

for k, v in sorted(pos_tag_T1.items(), key=lambda kv: kv[1], reverse=True):
    print(f"{k}: {v}")

"""<br>"""

from collections import Counter
pos_tag_T2 = Counter(tag for _, tag in Token2_pos)

"""<br>"""

for k, v in sorted(pos_tag_T2.items(), key=lambda kv: kv[1], reverse=True):
    print(f"{k}: {v}")

"""# Round 2

### Part 1

First we have imported wordnet (An NLTK corpus reader) from nltk.corpus. And then defined an lambda funtion to find which words are `NN` (nouns), and stored nouns of book1 as `nounsBook1`. 
"""

from nltk.corpus import wordnet
is_noun = lambda pos: pos[:2] == 'NN'
nounsBook1 = [word for (word, pos) in Token1_pos if is_noun(pos)] 
nounsBook1

"""Here we have found the nouns from Book2, using same method as earlier and stored the nouns of book2 in `nounsBook2`."""

from nltk.corpus import wordnet
is_noun = lambda pos: pos[:2] == 'NN'
nounsBook2 = [word for (word, pos) in Token2_pos if is_noun(pos)] 
nounsBook2

"""Here we have seperated the Verbs from book1 using lambda funtion `is_verb` for finding `VBG` and then stored the verbs in form of list in `verbsBook1`."""

is_verb = lambda pos: pos[:3] == 'VBG'
verbsBook1 = [word for (word, pos) in Token1_pos if is_verb(pos)] 
verbsBook1

"""In this block we have found the verbs in book2 in similar way and stored the result into `verbsBook2`."""

is_verb = lambda pos: pos[:3] == 'VBG'
verbsBook2 = [word for (word, pos) in Token2_pos if is_verb(pos)] 
verbsBook2

"""In this step we are finding the immediate categories i.e. parent of word. For this we are using the `hypernym()` and for each noun word in `nounsBook1` we are finding the Hypernym and then adding it to a list for parent of nouns in Book1 i.e. `parentBook1_noun`.  """

nltk.download('wordnet')  
from nltk.corpus import wordnet
parentBook1_noun = []
for noun in nounsBook1:
    if len(wordnet.synsets(noun)) > 0:
        x = wordnet.synsets(noun)[0] 
        if len(x.hypernyms()) > 0:
            y = [noun, x.hypernyms()[0]]
            parentBook1_noun.append(y)
        print(f'{noun} -> {x.hypernyms()}')

"""Similar to previous step we are finding the immediate categories i.e. parents of verbs in book1 and storing the result in `parentBook1_verb`."""

parentBook1_verb = []
for verb in verbsBook1:
    if len(wordnet.synsets(verb)) > 0:
        x = wordnet.synsets(verb)[0] 
        if len(x.hypernyms()) > 0:
            y = [verb, x.hypernyms()[0]]
            parentBook1_verb.append(y)
        print(f'{verb} -> {x.hypernyms()}')

"""Here we are fingind the parent of nouns in book2 and storing the parents in `parentBook2_noun`."""

parentBook2_noun = []
for noun in nounsBook2:
    if len(wordnet.synsets(noun)) > 0:
        x = wordnet.synsets(noun)[0] 
        if len(x.hypernyms()) > 0:
            y = [noun, x.hypernyms()[0]]
            parentBook2_noun.append(y)
        print(f'{noun} -> {x.hypernyms()}')

"""Here we are finding the parent of verbs in book2 and storing in the list `parentBook2_verb`."""

parentBook2_verb = []
for noun in verbsBook2:
    if len(wordnet.synsets(noun)) > 0:
        x = wordnet.synsets(noun)[0] 
        if len(x.hypernyms()) > 0:
            y = [noun, x.hypernyms()[0]]
            parentBook2_verb.append(y)
        print(f'{noun} -> {x.hypernyms()}')

"""### Part 1.2

In this step we have found the frequency of immediate categoty of each noun in Book1. We have used `Counter()`, as Counter is a container that will hold the count of each of the elements present in the container. Then we have created two list storing the count of parent of noun and that parent of noun itself called as `val` and `par` respectively. To obtain the string from Synset we have used `k.lemmas()[0].name`.
"""

freqBook1_noun = Counter(parent for word, parent in parentBook1_noun)
val = []
par = []
for k, v in sorted(freqBook1_noun.items(), key=lambda kv: kv[1], reverse=True):
    val.append(v)
    par.append(k.lemmas()[0].name())

"""Here we have plotted two types of charts, one is histogram which is showing frquency wise representation of immediate category for nouns in book1. From this we can see that most of categories of nouns occurs 0-10 times only and there are very few categories of nouns which occurs more often. 

Then we have plotted bar chart showing the frequency of each category of noun. Using the 2 bar charts we have shown for 200 categories (100 categories each).

<br>
"""

plt.hist(val)
plt.show()

plt.figure(figsize = (20,8))
plt.bar(par[:100], val[:100])
plt.xticks(rotation=90)
plt.show()

"""<br>"""

plt.figure(figsize = (20,8))
plt.bar(par[100:200], val[100:200])
plt.xticks(rotation=90)
plt.show()

"""<br>

<br>

Similarly we have plotted 1 histogram and 2 bar charts for the categories of varbs in book1 as follows.
"""

freqBook1_verb = Counter(parent for word, parent in parentBook1_verb)
val = []
par = []
for k, v in sorted(freqBook1_verb.items(), key=lambda kv: kv[1], reverse=True):
    val.append(v)
    par.append(k.lemmas()[0].name())

plt.hist(val)
plt.show()

plt.figure(figsize = (20,8))
plt.bar(par[:100], val[:100])
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize = (20,8))
plt.bar(par[100:200], val[100:200])
plt.xticks(rotation=90)
plt.show()

"""Here we have found the frequency and plotted a histogram and two bar charts for categories of nouns for book2."""

freqBook2_noun = Counter(parent for word, parent in parentBook2_noun)
val = []
par = []
for k, v in sorted(freqBook2_noun.items(), key=lambda kv: kv[1], reverse=True):
    val.append(v)
    par.append(k.lemmas()[0].name())

plt.hist(val)
plt.show()

plt.figure(figsize = (20,8))
plt.bar(par[:100], val[:100])
plt.xticks(rotation=90)
plt.show()

"""<br>

<br>
"""

plt.figure(figsize = (20,8))
plt.bar(par[100:200], val[100:200])
plt.xticks(rotation=90)
plt.show()

"""<br>

<br>

Similarly here we have found the frequency and plotted a histogram and two bar charts for categories of verbs for book2.
"""

freqBook2_verb = Counter(parent for word, parent in parentBook2_verb)
val = []
par = []
for k, v in sorted(freqBook2_verb.items(), key=lambda kv: kv[1], reverse=True):
    val.append(v)
    par.append(k.lemmas()[0].name())

"""<br>

<br>
"""

plt.hist(val)
plt.show()

plt.figure(figsize = (20,8))
plt.bar(par[:100], val[:100])
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize = (20,8))
plt.bar(par[100:200], val[100:200])
plt.xticks(rotation=90)
plt.show()

"""<br>

<br>

<br>

<br>

### Part2

In part two, we have to recognise all Persons, Location(GPE) and Organisation. In order to complete this NER task we are using two step procedure:
1. First recognise all the entity
2. Recognise all entity types

For this purpose we are using sentence tokenizer from NLTK library. Then we are using `ne_chunk()` which is a NLTK's currently recommended named entity chunker to chunk the given list of tagged tokens We are passing POS-tagged data to this funtion. Then based on the recognized entities we add them to a list, which we have called `NER_book1` for book1 and `NER_book2` for book2. Then we have put them in set to prevent the duplicates.
"""

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

NER_Book1 = set()
for sent in nltk.sent_tokenize(T1_clean):
  for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
     if hasattr(chunk, 'label'):
       NER_Book1.add((' '.join(c[0] for c in chunk), chunk.label()))
NER_Book1

NER_Book2 = set()
for sent in nltk.sent_tokenize(T2_clean):
  for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
     if hasattr(chunk, 'label'):
       NER_Book2.add((' '.join(c[0] for c in chunk), chunk.label()))
NER_Book2

"""Here we are going to test the accuracy and F1 score for our NER method. First of all we have defined `passage` which is our sample text taken out from book T2. Then we have put the model's NER and our hand picked NER into two different dictionaries and based on presence of actual entity type if it is present is model's entity types, we have found out the True Positives (`tp`), True Negative (`tn`), False Positive (`fp`) and False Negative (`fn`). Then we have calculated the `Accuracy` and `F1-Score` which we have got `0.87` and `0.80` respectively."""

passage="""MARLEY was dead: to begin with. There is no doubt
whatever about that. The register of his burial was
signed by the clergyman, the clerk, the undertaker,
and the chief mourner. Scrooge signed it: and
Scrooge's name was good upon 'Change, for anything he
chose to put his hand to. Old Marley was as dead as a
door-nail.

Mind! I don't mean to say that I know, of my
own knowledge, what there is particularly dead about
a door-nail. I might have been inclined, myself, to
regard a coffin-nail as the deadest piece of ironmongery
in the trade. But the wisdom of our ancestors
is in the simile; and my unhallowed hands
shall not disturb it, or the Country's done for. You
will therefore permit me to repeat, emphatically, that
Marley was as dead as a door-nail.

Scrooge knew he was dead? Of course he did.
How could it be otherwise? Scrooge and he were
partners for I don't know how many years. Scrooge
was his sole executor, his sole administrator, his sole
assign, his sole residuary legatee, his sole friend, and
sole mourner. And even Scrooge was not so dreadfully
cut up by the sad event, but that he was an excellent
man of business on the very day of the funeral,
and solemnised it with an undoubted bargain.

The mention of Marley's funeral brings me back to
the point I started from. There is no doubt that Marley
was dead. This must be distinctly understood, or
nothing wonderful can come of the story I am going
to relate. If we were not perfectly convinced that
Hamlet's Father died before the play began, there
would be nothing more remarkable in his taking a
stroll at night, in an easterly wind, upon his own ramparts,
than there would be in any other middle-aged
gentleman rashly turning out after dark in a breezy
spot--say Saint Paul's Churchyard for instance--
literally to astonish his son's weak mind.

Scrooge never painted out Old Marley's name.
There it stood, years afterwards, above the warehouse
door: Scrooge and Marley. The firm was known as
Scrooge and Marley. Sometimes people new to the
business called Scrooge Scrooge, and sometimes Marley,
but he answered to both names. It was all the
same to him.

Oh! But he was a tight-fisted hand at the grind-stone,
Scrooge! a squeezing, wrenching, grasping, scraping,
clutching, covetous, old sinner! Hard and sharp as flint,
from which no steel had ever struck out generous fire;
secret, and self-contained, and solitary as an oyster. The
cold within him froze his old features, nipped his pointed
nose, shrivelled his cheek, stiffened his gait; made his
eyes red, his thin lips blue; and spoke out shrewdly in his
grating voice. A frosty rime was on his head, and on his
eyebrows, and his wiry chin. He carried his own low
temperature always about with him; he iced his office in
the dog-days; and didn't thaw it one degree at Christmas.

External heat and cold had little influence on
Scrooge. No warmth could warm, no wintry weather
chill him. No wind that blew was bitterer than he,
no falling snow was more intent upon its purpose, no
pelting rain less open to entreaty. Foul weather didn't
know where to have him. The heaviest rain, and
snow, and hail, and sleet, could boast of the advantage
over him in only one respect. They often "came down"
handsomely, and Scrooge never did.

Nobody ever stopped him in the street to say, with
gladsome looks, "My dear Scrooge, how are you?
When will you come to see me?" No beggars implored
him to bestow a trifle, no children asked him
what it was o'clock, no man or woman ever once in all
his life inquired the way to such and such a place, of
Scrooge. Even the blind men's dogs appeared to
know him; and when they saw him coming on, would
tug their owners into doorways and up courts; and
then would wag their tails as though they said, "No
eye at all is better than an evil eye, dark master!"

But what did Scrooge care! It was the very thing
he liked. To edge his way along the crowded paths
of life, warning all human sympathy to keep its distance,
was what the knowing ones call "nuts" to Scrooge.

Once upon a time--of all the good days in the year,
on Christmas Eve--old Scrooge sat busy in his
counting-house. It was cold, bleak, biting weather: foggy
withal: and he could hear the people in the court outside,
go wheezing up and down, beating their hands
upon their breasts, and stamping their feet upon the
pavement stones to warm them. The city clocks had
only just gone three, but it was quite dark already--
it had not been light all day--and candles were flaring
in the windows of the neighbouring offices, like
ruddy smears upon the palpable brown air. The fog
came pouring in at every chink and keyhole, and was
so dense without, that although the court was of the
narrowest, the houses opposite were mere phantoms.
To see the dingy cloud come drooping down, obscuring
everything, one might have thought that Nature
lived hard by, and was brewing on a large scale.

The door of Scrooge's counting-house was open
that he might keep his eye upon his clerk, who in a
dismal little cell beyond, a sort of tank, was copying
letters. Scrooge had a very small fire, but the clerk's
fire was so very much smaller that it looked like one
coal. But he couldn't replenish it, for Scrooge kept
the coal-box in his own room; and so surely as the
clerk came in with the shovel, the master predicted
that it would be necessary for them to part. Wherefore
the clerk put on his white comforter, and tried to
warm himself at the candle; in which effort, not being
a man of a strong imagination, he failed.

"A merry Christmas, uncle! God save you!" cried
a cheerful voice. It was the voice of Scrooge's
nephew, who came upon him so quickly that this was
the first intimation he had of his approach.

"Bah!" said Scrooge, "Humbug!"

He had so heated himself with rapid walking in the
fog and frost, this nephew of Scrooge's, that he was
all in a glow; his face was ruddy and handsome; his
eyes sparkled, and his breath smoked again.

"Christmas a humbug, uncle!" said Scrooge's
nephew. "You don't mean that, I am sure?"

"I do," said Scrooge. "Merry Christmas! What
right have you to be merry? What reason have you
to be merry? You're poor enough."

"Come, then," returned the nephew gaily. "What
right have you to be dismal? What reason have you
to be morose? You're rich enough."

Scrooge having no better answer ready on the spur
of the moment, said, "Bah!" again; and followed it up
with "Humbug."

"Don't be cross, uncle!" said the nephew.

"What else can I be," returned the uncle, "when I
live in such a world of fools as this? Merry Christmas!
Out upon merry Christmas! What's Christmas
time to you but a time for paying bills without
money; a time for finding yourself a year older, but
not an hour richer; a time for balancing your books
and having every item in 'em through a round dozen
of months presented dead against you? If I could
work my will," said Scrooge indignantly, "every idiot
who goes about with 'Merry Christmas' on his lips,
should be boiled with his own pudding, and buried
with a stake of holly through his heart. He should!"

"Uncle!" pleaded the nephew.

"Nephew!" returned the uncle sternly, "keep Christmas
in your own way, and let me keep it in mine."

"Keep it!" repeated Scrooge's nephew. "But you
don't keep it."

"Let me leave it alone, then," said Scrooge. "Much
good may it do you! Much good it has ever done
you!"

"There are many things from which I might have
derived good, by which I have not profited, I dare
say," returned the nephew. "Christmas among the
rest. But I am sure I have always thought of Christmas
time, when it has come round--apart from the
veneration due to its sacred name and origin, if anything
belonging to it can be apart from that--as a
good time; a kind, forgiving, charitable, pleasant
time; the only time I know of, in the long calendar
of the year, when men and women seem by one consent
to open their shut-up hearts freely, and to think
of people below them as if they really were
fellow-passengers to the grave, and not another race
of creatures bound on other journeys. And therefore,
uncle, though it has never put a scrap of gold or
silver in my pocket, I believe that it has done me
good, and will do me good; and I say, God bless it!"

The clerk in the Tank involuntarily applauded.
Becoming immediately sensible of the impropriety,
he poked the fire, and extinguished the last frail spark
for ever.

"Let me hear another sound from you," said
Scrooge, "and you'll keep your Christmas by losing
your situation! You're quite a powerful speaker,
sir," he added, turning to his nephew. "I wonder you
don't go into Parliament."

"Don't be angry, uncle. Come! Dine with us to-morrow."

Scrooge said that he would see him--yes, indeed he
did. He went the whole length of the expression,
and said that he would see him in that extremity first.

"But why?" cried Scrooge's nephew. "Why?"

"Why did you get married?" said Scrooge.

"Because I fell in love."

"Because you fell in love!" growled Scrooge, as if
that were the only one thing in the world more ridiculous
than a merry Christmas. "Good afternoon!"

"Nay, uncle, but you never came to see me before
that happened. Why give it as a reason for not
coming now?"

"Good afternoon," said Scrooge.

"I want nothing from you; I ask nothing of you;
why cannot we be friends?"

"Good afternoon," said Scrooge.

"I am sorry, with all my heart, to find you so
resolute. We have never had any quarrel, to which I
have been a party. But I have made the trial in
homage to Christmas, and I'll keep my Christmas
humour to the last. So A Merry Christmas, uncle!"

"Good afternoon!" said Scrooge.

"And A Happy New Year!"

"Good afternoon!" said Scrooge.

His nephew left the room without an angry word,
notwithstanding. He stopped at the outer door to
bestow the greetings of the season on the clerk, who,
cold as he was, was warmer than Scrooge; for he returned
them cordially.

"There's another fellow," muttered Scrooge; who
overheard him: "my clerk, with fifteen shillings a
week, and a wife and family, talking about a merry
Christmas. I'll retire to Bedlam."

This lunatic, in letting Scrooge's nephew out, had
let two other people in. They were portly gentlemen,
pleasant to behold, and now stood, with their hats off,
in Scrooge's office. They had books and papers in
their hands, and bowed to him.

"Scrooge and Marley's, I believe," said one of the
gentlemen, referring to his list. "Have I the pleasure
of addressing Mr. Scrooge, or Mr. Marley?"

"Mr. Marley has been dead these seven years,"
Scrooge replied. "He died seven years ago, this very
night."

"We have no doubt his liberality is well represented
by his surviving partner," said the gentleman, presenting
his credentials.

It certainly was; for they had been two kindred
spirits. At the ominous word "liberality," Scrooge
frowned, and shook his head, and handed the credentials
back.

"At this festive season of the year, Mr. Scrooge,"
said the gentleman, taking up a pen, "it is more than
usually desirable that we should make some slight
provision for the Poor and destitute, who suffer
greatly at the present time. Many thousands are in
want of common necessaries; hundreds of thousands
are in want of common comforts, sir."

"Are there no prisons?" asked Scrooge.

"Plenty of prisons," said the gentleman, laying down
the pen again.

"And the Union workhouses?" demanded Scrooge.
"Are they still in operation?"

"They are. Still," returned the gentleman, "I wish
I could say they were not."

"The Treadmill and the Poor Law are in full vigour,
then?" said Scrooge.

"Both very busy, sir."

"Oh! I was afraid, from what you said at first,
that something had occurred to stop them in their
useful course," said Scrooge. "I'm very glad to
hear it."

"Under the impression that they scarcely furnish
Christian cheer of mind or body to the multitude,"
returned the gentleman, "a few of us are endeavouring
to raise a fund to buy the Poor some meat and drink,
and means of warmth. We choose this time, because
it is a time, of all others, when Want is keenly felt,
and Abundance rejoices. What shall I put you down
for?"

"Nothing!" Scrooge replied.

"You wish to be anonymous?"
"""

passageNER = set()
for sent in nltk.sent_tokenize(passage):
  for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
     if hasattr(chunk, 'label'):
       passageNER.add((' '.join(c[0] for c in chunk), chunk.label()))
passageNER

tp,tn,fp,fn=0,0,0,0
 
prediction=dict()
for x in passageNER:
  prediction.setdefault(x[0],[]).append(x[1])
# print(prediction)

HandMarked= {
  ('Bedlam', 'GPE'),
  ('Christian', 'PERSON'),
  ('Churchyard', 'ORGANIZATION'),
  ('Country', 'GPE’'),
  ('Father', 'PERSON'),
  ('God', 'PERSON'),
  ('Happy New Year', 'ORGANIZATION'),
  ('Marley', 'PERSON'),
  ('Merry', 'PERSON'),
  ('Mr. Marley', 'PERSON'),
  ('Mr. Scrooge', 'PERSON'),
  ('Old Marley', 'ORGANIZATION'),
  ('Parliament', 'ORGANIZATION'),
  ('Saint Paul', 'GPE'),
  ('Scrooge', 'PERSON'),
  ('Treadmill', 'ORGANIZATION'),
  ('Union', 'ORGANIZATION')}


actual=dict()
for x in HandMarked:
  actual.setdefault(x[0],x[1])
# print(actual)


for entity, type_ in actual.items():
    # print(entity, ":", type_)
    if type_ in prediction[entity]:
      tp+=1
      fp+=len(prediction[entity])-1
    else:
      fp+=len(prediction[entity])
    if type_ not in prediction[entity]:
        fn+=1
    for x in ['GPE','ORGANIZATION','PERSON']:
      if x != type_ and x not in prediction[entity]:
        tn+=1

print("TP: ",tp," TN: ",tn," FP: ",fp," FN: ",fn) 
F1_score=(2*tp)/((2*tp)+fp+fn)
accuracy=(tp+tn)/(tp+tn+fn+fp)
print("Accuracy: {0:.2f}".format(accuracy))
print("F1 Score: {0:.2f}".format(F1_score))

"""### Part 3

In this part we will create TF-IDF vectors for all books and find the cosine similarity between each of them and find which two books are more similar.

Here we have impprted the third book called `Pride and Prejudice` and called it `T3`. Then we have cleaned it and removed the headings and other un-neccessary text.
"""

filename="/content/Pride.txt"
f = open(str(filename), 'r', encoding="utf8")

T3 = f.read()
f.close()

T3_clean = T3[T3.find("Chapter 61")+len("Chapter 61"):T3.find("*** END OF THE PROJECT GUTENBERG EBOOK")]
T3_clean = re.sub(r'\n{4}Chapter.*\n\n+', '\n\n', T3_clean)
# print(T3_clean)

"""Here we have tokenized each word and saved the list of Token in `T3_Words`. Then we have further filtered the Tokens by removing the numerals and other characters, and saved the resutant list as `T3_Token`."""

from nltk.tokenize import sent_tokenize, word_tokenize

T3_Words = word_tokenize(T3_clean)

punctuation = re.compile(r"[^a-zA-Z]+")
T3_Token = []
for words in T3_Words:
  words = punctuation.sub("", words)
  if len(words) > 0:
    T3_Token.append(words.lower())
print(T3_Token)

"""Here we have removed the stopwords and stored the result into `T3_Clean_Token`."""

T3_Clean_Token = []
for token in T3_Token:
    if token not in stopwords.words('english'):
        T3_Clean_Token.append(token)

"""Now it's the time we create the corpus, which have three documents namely `T1_clean`, `T2_clean` and `T3_clean`. Then using the `TfidfVectorizer()` available in `sklearn.feature_extraction.text` library, we have vectorized out documents and found the TF-IDF vectors for all the books. Then we have found the cosine similarity between each pair of book and found the similarity as follows:

Douments | T1 | T2 | T3
--- | --- | --- | ---
T1 | 1.0 | 0.86462291 | 0.84356338
T2 | 86462291 | 1.0 | 0.86722304
T3 | 84356338 | 0.86722304 | 1.0

So clearly T2 and T3 are more similar.
"""

corpus = [T1_clean, T2_clean, T3_clean]
print(corpus)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

tfidf = TfidfVectorizer().fit_transform(corpus)
print(tfidf)

print("cosine scores ==> ")
cosine_similarity(tfidf[0:1], tfidf)

corpus = [T2_clean, T1_clean, T3_clean]
tfidf = TfidfVectorizer().fit_transform(corpus)
print("cosine scores ==> ")
cosine_similarity(tfidf[0:1], tfidf)

"""### Without Stopwords
Here we are again finding the cosine similarity of the given three documents but this time we are not not using stopwords. SO first we are constructing the documents from the individual cleaned token lists and then we are vectorizing them and then finding the cosine similarity between each pair of documents.

We have obtained the following cosine similarity:

Douments | T1 | T2 | T3
--- | --- | --- | ---
T1 | 1.0 | 0.29815264 | 0.27590156
T2 | 0.29815264 | 1.0 | 0.29103395
T3 | 0.27590156 | 0.29103395 | 1.0


From this we can see that T1 and T2 are more similar than any other pair.
"""

T1_withoutSW = ''
for word in clean_tokens_T1:
    T1_withoutSW = T1_withoutSW + ' ' + word

T2_withoutSW = ''
for word in clean_tokens_T2:
    T2_withoutSW = T2_withoutSW + ' ' + word

T3_withoutSW = ''
for word in T3_Clean_Token:
    T3_withoutSW = T3_withoutSW + ' ' + word

corpus = [T1_withoutSW, T2_withoutSW, T3_withoutSW]
tfidf = TfidfVectorizer().fit_transform(corpus)
print("cosine scores ==> ")
cosine_similarity(tfidf[0:1], tfidf)

corpus = [T2_withoutSW, T1_withoutSW, T3_withoutSW]
tfidf = TfidfVectorizer().fit_transform(corpus)
print("cosine scores ==> ")
cosine_similarity(tfidf[0:1], tfidf)

"""### Part 3.2

### Lemmatization
In this part we are again going to vectorize the documents and then finding the cosine similarity between them but this time we are first lemmatizing the tokens of each documets using `WordNetLemmatizer()` and then forming the documents from the lemmatized tokens of each document and calling the document as `strT1`, `strT2` and `strT3`. Then again using the `TfidfVectorizer()` we are vectorizing each document and the finding the cosine similarity between each pair of documents. The result thus obtained is as follows:

Douments | T1 | T2 | T3
--- | --- | --- | ---
T1 | 1.0 | 0.86217166 | 0.8374938
T2 | 0.86217166 | 1.0 | 0.85994249
T3 | 0.8374938 | 0.85994249 | 1.0

Through this analysis we have found that T1 and T2 are more similar than any other pair of documents.
"""

from nltk.stem import WordNetLemmatizer
 
lemmatizer = WordNetLemmatizer()

lem1 = []
lem2 = []
lem3 = []
for token in Token_T1:
    lem1.append(lemmatizer.lemmatize(token))
    
for token in Token_T2:
    lem2.append(lemmatizer.lemmatize(token))

for token in T3_Token:
    lem3.append(lemmatizer.lemmatize(token))

strT1 = ''
for word in lem1:
    strT1 = strT1 + ' ' + word

strT2 = ''
for word in lem2:
    strT2 = strT2 + ' ' + word

strT3 = ''
for word in lem3:
    strT3 = strT3 + ' ' + word

corpus = [strT1, strT2, strT3]
tfidf = TfidfVectorizer().fit_transform(corpus)
from sklearn.metrics.pairwise import cosine_similarity
print("cosine scores ==> ")
cosine_similarity(tfidf[0:1], tfidf)

corpus = [strT2, strT1, strT3]
tfidf = TfidfVectorizer().fit_transform(corpus)
print("cosine scores ==> ")
cosine_similarity(tfidf[0:1], tfidf)

"""### Without Stopwords

Once again we are finding the similarity between each pair of documents but this time we are using combination of removing stop word technique and lemmatization. So firstly we will lemmatize tokens of each book which do not contains any stopword. After lemmatization we are appending tokens so as to make a documents in which each word is lemmatized ans is not a stopword. Then we have again prepared a corpus and vectorized each of the three documents using `TfidfVectorizer()`, and then using `cosine_similarity()` we have found the similarity between each pair of documents and found the following result:

Douments | T1 | T2 | T3
--- | --- | --- | ---
T1 | 1.0 | 0.3054361 | 0.26813356
T2 | 0.3054361 | 1.0 | 0.30240701
T3 | 0.26813356 | 0.30240701 | 1.0

From the above table we can say that T1 and T2 are more similar than (T1,T3) and (T2,T3).
"""

lem1_withoutSW = []
lem2_withoutSW = []
lem3_withoutSW = []
for token in clean_tokens_T1:
    lem1_withoutSW.append(lemmatizer.lemmatize(token))
    
for token in clean_tokens_T2:
    lem2_withoutSW.append(lemmatizer.lemmatize(token))

for token in T3_Clean_Token:
    lem3_withoutSW.append(lemmatizer.lemmatize(token))

strT1_withoutSW = ''
for word in lem1_withoutSW:
    strT1_withoutSW = strT1_withoutSW + ' ' + word

strT2_withoutSW = ''
for word in lem2_withoutSW:
    strT2_withoutSW = strT2_withoutSW + ' ' + word

strT3_withoutSW = ''
for word in lem3_withoutSW:
    strT3_withoutSW = strT3_withoutSW + ' ' + word

corpus = [strT1_withoutSW, strT2_withoutSW, strT3_withoutSW]
tfidf = TfidfVectorizer().fit_transform(corpus)
print("cosine scores ==> ")
cosine_similarity(tfidf[0:1], tfidf)

corpus = [strT2_withoutSW, strT1_withoutSW, strT3_withoutSW]
tfidf = TfidfVectorizer().fit_transform(corpus)
print("cosine scores ==> ")
cosine_similarity(tfidf[0:1], tfidf)

"""# Inferences

1. We can see that most of the words in both the books is some stopwords only.
2. After removing the stopwords we found that, most frequent words for book 1 i.e. Alice’s adventures in Wonderland is 'said' and 'Alice', so Alice must have been main character in this book, similarly in book 2 i.e. A Christmas Carol in Prose; Being a Ghost Story of Christmas by Charles Dickens most frequent words are 'Scrooge' and 'said', which can be interpreted as Scrooge being main charachter on that story.
3. Most of words in both the books are either Nouns or Adjective.
4. Most of the words in book 1 and book 2 have lenght between 2 to 10 characters, while books 1 has more variability as minimum word length for book1 words is 1 and maximum is 40, while for book 2 minimum is 2 and maximum is 21.
5. For book 1, Most categories of nouns occurs 0-10 times only and there are very few categories of nouns which occurs more often.
6. For book 1, the most used noun is “external_body_part”  and the most used verb is “act”.
7. For book 2, Most categories of nouns occurs 0-25 times only and there are very few categories of nouns which occurs more often.
8. For book 2, the most used noun is “hoarder”  and the most used verb is “sensing”.
9. Book T1 and Book T2 are more similar than any other pair.

"""
