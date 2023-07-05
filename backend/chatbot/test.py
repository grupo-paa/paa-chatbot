import nltk

from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree

text = '''
Cars best characters of the star wars universe is One, like Alex and without a doubt
'''

nltk_results = ne_chunk(pos_tag(word_tokenize(text)))
for nltk_result in nltk_results:
    if type(nltk_result) == Tree:
        name = ''
        for nltk_result_leaf in nltk_result.leaves():
            name += nltk_result_leaf[0] + ' '
        print ('Type: ', nltk_result.label(), 'Name: ', name)