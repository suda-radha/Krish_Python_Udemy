## Speech Of DR APJ Abdul Kalam
apj_paragraph = """I have three visions for India. In 3000 years of our history, people from all over 
               the world have come and invaded us, captured our lands, conquered our minds. 
               From Alexander onwards, the Greeks, the Turks, the Moguls, the Portuguese, the British,
               the French, the Dutch, all of them came and looted us, took over what was ours. 
               Yet we have not done this to any other nation. We have not conquered anyone. 
               We have not grabbed their land, their culture, 
               their history and tried to enforce our way of life on them. 
               Why? Because we respect the freedom of others.That is why my 
               first vision is that of freedom. I believe that India got its first vision of 
               this in 1857, when we started the War of Independence. It is this freedom that
               we must protect and nurture and build on. If we are not free, no one will respect us.
               My second vision for India’s development. For fifty years we have been a developing nation.
               It is time we see ourselves as a developed nation. We are among the top 5 nations of the world
               in terms of GDP. We have a 10 percent growth rate in most areas. Our poverty levels are falling.
               Our achievements are being globally recognised today. Yet we lack the self-confidence to
               see ourselves as a developed nation, self-reliant and self-assured. Isn’t this incorrect?
               I have a third vision. India must stand up to the world. Because I believe that unless India 
               stands up to the world, no one will respect us. Only strength respects strength. We must be 
               strong not only as a military power but also as an economic power. Both must go hand-in-hand. 
               My good fortune was to have worked with three great minds. Dr. Vikram Sarabhai of the Dept. of 
               space, Professor Satish Dhawan, who succeeded him and Dr. Brahm Prakash, father of nuclear material.
               I was lucky to have worked with all three of them closely and consider this the great opportunity of my life. 
               I see four milestones in my career"""

## Stop words -- words that make no much sense like of, the,
## note: we can also apply stopwords and stemming


from nltk.stem import PorterStemmer
from nltk.corpus import stopwords


## you need to download the dataset for stopwords (note u have diff stopwords for diff language )
import nltk
nltk.download('stopwords')

# display all stopwords downloaded
print(stopwords.words('english')) # u see a huge list as op: a, about, above, after, am ....

# note: u can also create your own stopwords list (if u feel teh words in the default list is needed and should not be ignored)

# Step1: Apply stemming/tokenizing ->  apply sentence_tokenizer - so you get sentences
# Step2 : apply stopwords to eliminate stopwords

# Apply stemming on apj paragraph text
from nltk.stem import PorterStemmer
stemmer=PorterStemmer()
sent_tokenized_para=nltk.sent_tokenize(apj_paragraph)
print(sent_tokenized_para)

# Apply stopwords and Filter and apply stemming (3step process)
for i in range(len(sent_tokenized_para)):
    words = nltk.word_tokenize(sent_tokenized_para[i]) # get list of words in sentence-tokenized apj para
    # take each word and apply stemming only if that word is not present in stopwords list
    # (basically u are applying stemming for all words (but should not be part of stopwords)
    words=[stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
    # Then join these words together
    sent_tokenized_para[i]=' '.join(words) # converts all words to sentences

# now look at the stemmed text para (youll have minumum words)
print("\n\nSentTokenized Para==> Stemming applied on non stopwords ==> result words joined as sentences: ")
for w in sent_tokenized_para:
    print(w)

"""Output:
SentTokenized Para==> Stemming applied on non stopwords ==> result words joined as sentences: 
i three vision india .
in 3000 year histori , peopl world come invad us , captur land , conquer mind .
from alexand onward , greek , turk , mogul , portugues , british , french , dutch , came loot us , took .
yet done nation .
we conquer anyon .
we grab land , cultur , histori tri enforc way life .
whi ?
becaus respect freedom others.that first vision freedom .
i believ india got first vision 1857 , start war independ .
it freedom must protect nurtur build .
if free , one respect us .
my second vision india ’ develop .
for fifti year develop nation .
it time see develop nation .
we among top 5 nation world term gdp .
we 10 percent growth rate area .
our poverti level fall .
our achiev global recognis today .
yet lack self-confid see develop nation , self-reli self-assur .
isn ’ incorrect ?
i third vision .
india must stand world .
becaus i believ unless india stand world , one respect us .
onli strength respect strength .
we must strong militari power also econom power .
both must go hand-in-hand .
my good fortun work three great mind .
dr. vikram sarabhai dept .
space , professor satish dhawan , succeed dr. brahm prakash , father nuclear materi .
i lucki work three close consid great opportun life .
i see four mileston career
"""

# lets apply snowball stemmer and see
from nltk.stem import SnowballStemmer
snowballstemmer = SnowballStemmer('english')

# Apply stopwords and Filter and apply stemming (3step process)
for i in range(len(sent_tokenized_para)):
    words = nltk.word_tokenize(sent_tokenized_para[i]) # get list of words in sentence-tokenized apj para
    # take each word and apply stemming only if that word is not present in stopwords list
    # (basically u are applying stemming for all words (but should not be part of stopwords)
    words=[snowballstemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
    # Then join these words together
    sent_tokenized_para[i]=' '.join(words) # converts all words to sentences

# now look at the stemmed text para (youll have minumum words)
print("\n\nSentTokenized Para==> SNOWBALL Stemming applied on non stopwords ==> result words joined as sentences: ")
for w in sent_tokenized_para:
    print(w)

"""Output: looks better more unnecessary stopwords like i is removed here:
SentTokenized Para==> SNOWBALL Stemming applied on non stopwords ==> result words joined as sentences: 
three vision india .
3000 year histori , peopl world come invad us , captur land , conquer mind .
alexand onward , greek , turk , mogul , portugu , british , french , dutch , came loot us , took .
yet done nation .
conquer anyon .
grab land , cultur , histori tri enforc way life .
whi ?
becaus respect freedom others.that first vision freedom .
believ india got first vision 1857 , start war independ .
freedom must protect nurtur build .
free , one respect us .
second vision india ’ develop .
fifti year develop nation .
time see develop nation .
among top 5 nation world term gdp .
10 percent growth rate area .
poverti level fall .
achiev global recogni today .
yet lack self-confid see develop nation , self-r self-assur .
’ incorrect ?
third vision .
india must stand world .
becaus believ unless india stand world , one respect us .
on strength respect strength .
must strong militari power also econom power .
must go hand-in-hand .
good fortun work three great mind .
dr. vikram sarabhai dept .
space , professor satish dhawan , succeed dr. brahm prakash , father nuclear materi .
lucki work three close consid great opportun life .
see four mileston career
"""

## Now lets apply Lemmatization instead of Stemming
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

# Apply stopwords and Filter and apply Lemmatization (3step process)
for i in range(len(sent_tokenized_para)):
    words = nltk.word_tokenize(sent_tokenized_para[i]) # get list of words in sentence-tokenized apj para
    # take each word and apply lemmatization only if that word is not present in stopwords list
    # (basically u are applying lemmatization for all words (but should not be part of stopwords)
    words=[lemmatizer.lemmatize(word) for word in words if word not in set(stopwords.words('english'))]
    # Then join these words together
    sent_tokenized_para[i]=' '.join(words) # converts all words to sentences

# now look at the Lemmatized text para (youll have minumum words)
print("\n\nSentTokenized Para==> LEMMATIZATION applied on non stopwords ==> result words joined as sentences: ")
for w in sent_tokenized_para:
    print(w)

"""output: looks better with Lemmatization instead of Stemming:
SentTokenized Para==> LEMMATIZATION applied on non stopwords ==> result words joined as sentences: 
three vision india .
3000 year histori , peopl world come invad u , captur land , conquer mind .
alexand onward , greek , turk , mogul , portugu , british , french , dutch , came loot u , took .
yet done nation .
conquer anyon .
grab land , cultur , histori tri enforc way life .
whi ?
becaus respect freedom others.that first vision freedom .
believ india got first vision 1857 , start war independ .
freedom must protect nurtur build .
free , one respect u .
second vision india ’ develop .
fifti year develop nation .
time see develop nation .
among top 5 nation world term gdp .
10 percent growth rate area .
poverti level fall .
achiev global recogni today .
yet lack self-confid see develop nation , self-r self-assur .
’ incorrect ?
third vision .
india must stand world .
becaus believ unless india stand world , one respect u .
strength respect strength .
must strong militari power also econom power .
must go hand-in-hand .
good fortun work three great mind .
dr. vikram sarabhai dept .
space , professor satish dhawan , succeed dr. brahm prakash , father nuclear materi .
lucki work three close consid great opportun life .
see four mileston career
"""