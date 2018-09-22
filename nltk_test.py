import nltk

nltk.download('punkt')
nltk.download('names')
nltk.download('city_database')
nltk.download('book')


sentence = """Marcus (Male, 48 years old, age=49 ) had a sever headache that lasted 10 days starting on 10OCT2018 NNP"""


tokens = nltk.word_tokenize(sentence)
tokens


tagged = nltk.pos_tag(tokens)
tagged[0:]

print(tagged[0])

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


#SUMMARIZES THE TAGS AND COUNT
def findtags(tag_prefix, tagged_text):
    cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text
                                  if tag.startswith(tag_prefix))
    return dict((tag, cfd[tag].most_common(5)) for tag in cfd.conditions())

def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

#LOOP THROUGH THE TAGS
x=[item[1] for item in tagged]
tag_list=f7(x)

for i in tag_list:
    findtags(i,tagged)