# -*- coding: utf-8 -*-

from nltk.corpus import wordnet as wn
import collections, sys
#from nltk.stem.wordnet import WordNetLemmatizer
from nltk import word_tokenize, PorterStemmer

stop_words = set()
with open('stop_words.txt', 'r') as f:    
    for line in f:
        word = line.strip()
        if word:
            stop_words.add(word)
#wnl = WordNetLemmatizer()
porter = PorterStemmer()

def lesk(target, sentence):
    print(target)
    best_sense = ''
    max_overlap = 0
    #context_words = [wnl.lemmatize(word) for word in sentence.split()]
    context_words = [porter.stem(word) for word in sentence] 
    new_context_words = []
    for w in context_words:
        if w not in stop_words:
            new_context_words.append(w)   
    context = collections.Counter(new_context_words)    
    senses = wn.synsets(target)   
    for sense in senses:
        definition = sense.definition()
        definition = word_tokenize(definition)
        #definition = [wnl.lemmatize(word) for word in definition]
        definition = [porter.stem(word) for word in definition]
        definition_dict = collections.Counter(definition)        
        overlap = computer_overlap(definition_dict, context)
        if overlap > max_overlap:
            #print(overlap)
            max_overlap = overlap
            best_sense = sense.definition()
    return best_sense

def computer_overlap(definition, context):
    count = 0
    for w, _ in definition.items():
        if w in context:
            count += 1
    return count

def main():
    #sentence = u'the bank can guarantee deposits will eventually cover future tuition costs because it invests in adjustable-rate mortgage securities'
    #sentence = sentence.split()
    #target = u'bank'
    target = sys.argv[1]
    sentence = sys.argv[2:]
    return lesk(target, sentence)

if __name__ == "__main__":
    res = main()
    print(res)