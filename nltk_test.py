import nltk
from nltk.corpus import words,stopwords

nltk.download('punkt')
nltk.download('names')
nltk.download('city_database')
nltk.download('book')
nltk.download('stopwords')
nltk.download('words')

sentence ="""
Marcus (Male, 48 years old, age=49 ) had a sever headache that lasted 10 days starting on 10OCT2018 NNP.
This stopped two days later. Dr.Smith prescribed a paracetamol 10 mg dose.
"""
stop_words=set(stopwords.words("english"))

#WORD IN THE ENGLISH LANGUAGE?
print("fine" in words.words())
print("headache" in words.words())


#BREAK INTO SENTENCES
sent_tokens = nltk.sent_tokenize(sentence)
sent_tokens
#BREAK INTO WORDS
word_tokens = nltk.word_tokenize(sentence)
word_tokens

#PRINT OUT THE WORDS IN A LIST
for i in word_tokens:
    print(i)

#TAG THE WORDS
tagged = nltk.pos_tag(word_tokens)
tagged[0:]

#NOW REDACT THE TEXT BASED OFF THE CODE - NOT WORKING - NEED TO FIX
#PRINT OUT THE WORDS IN A LIST
for i in tagged:
    print(i)
tag2=([[i if i != 'CD' else '[DATE REDACTED]' for i in x] for x in tagged])
print(tag2)
#PUT THE SENTENCE BACK TOGETHER
new_sent=' '.join(tag2)
print(new_sent)




#SUMMARIZES THE TAGS AND COUNT
def findtags(tag_prefix, tagged_text):
    cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text
                                  if tag.startswith(tag_prefix))
    return dict((tag, cfd[tag].most_common(5)) for tag in cfd.conditions())

#NO DUPLICATES
def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

#LOOP THROUGH THE TAGS
x=[item[1] for item in tagged]
tag_list=f7(x)

for i in tag_list:
    findtags(i,tagged)



#FILTER THE SENTENCE FOR STOP WORDS
filter_word_tokens=[]
for w in word_tokens:
    if w not in stop_words:
        filter_word_tokens.append(w)
    else:
        print('Removed: '+w)

print(filter_word_tokens)

#PUT THE SENTENCE BACK TOGETHER
new_sent=' '.join(filter_word_tokens)
print(new_sent)






for x in tagged:
    print(x)

#REPLACE THE NNP
tag1=([[i if i != 'NNP' else '*' for i in x] for x in tagged])
tag2=([[i if i != 'CD' else '[DATE REDACTED]' for i in x] for x in tag1])


print(tag2)


for x in tagged:
    for i in x:
        print(x)


fdist = nltk.FreqDist(tagged)
print(fdist)

for word, frequency in fdist.most_common(10):
 print(u'{} - {}'.format(word, frequency))

from nltk.corpus import treebank
t = treebank.parsed_sents('wsj_0001.mrg')[0]
t.draw()


