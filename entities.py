import nltk

#5/1/16
#TOO SLOW. won't work on novel.

def extract_entity_names(t):
    entity_names = []
    if hasattr(t, 'label') and t.label:
        if t.label() == 'NE':
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))
    return entity_names


def getEntities(filename):
    with open('harry.txt', 'r') as f:
        sample = f.read()
    sample = sample.decode('unicode_escape').encode('ascii','ignore')
    print "sentence tokenize..."
    sentences = nltk.sent_tokenize(sample)
    print len(sentences)
    sentences = sentences[:len(sentences)/30]
    print len(sentences)
    print "word tokenize..."
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    print "POS tagging..."
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
    print "Chunking..."
    chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)
    entity_names = []
    print "getting entities..."
    print "total sentences = ", len(chunked_sentences)
    for i, tree in enumerate(chunked_sentences):
        if i%100==0:
            print "on sentence", i
        entity_names.extend(extract_entity_names(tree))
    uniques = list(set(entity_names))
    #only returned named entities that are 2 words or more
    output = [u for u in unique if len(u.split(" ")) >= 2]

print getEntities("harry.txt")
