import re

#res = re.match('abc', 'abcde')
#print(res)

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize


sentences = sent_tokenize(scene_one)

tokenized_sent = word_tokenize(sentences[3])

unique_tokens = set(word_tokenize(scene_one))
print(unique_tokens)
