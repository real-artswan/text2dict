#!/usr/bin/env python3

import sys

OUTFILE = 'unique_words.csv'

def main():
	if len(sys.argv) < 2:
		print('Specify an input plain text file!')

	from nltk import download
	inputFile = sys.argv[1]
	if inputFile == '--help':
		download('tagsets')
		from nltk.help import upenn_tagset
		print(upenn_tagset())
		return

	with open(inputFile, 'r') as f:
		texts = f.read()

	texts = texts.split('\n')
	# Process texts
	print('Got texts:', len(texts))


	# Tokenize texts
	print('Tokenizing texts...')
	download('punkt')
	from nltk.tokenize import word_tokenize
	words = set()

	for text in texts:
		text_words = word_tokenize(text)
		words.update(text_words)

	print('Normalization...')
	import re
	# Normalize words (remove punctuation etc)
	words = map(lambda w: re.sub(r'[^a-zA-Z\-\'\`\"]', '', w), words)

	# Filter out unnecessary stuff
	words = filter(lambda w: len(w) > 2 and len(w) <= 45, words)
	words = set(words)
	print('All filtered words:', len(words))

	# # Filter out names words
	# from nltk.tag import StanfordNERTagger
	# st = StanfordNERTagger('stanford-ner-2018-10-16/classifiers/english.all.3class.distsim.crf.ser.gz', 'stanford-ner-2018-10-16/stanford-ner.jar')
	# tagged = st.tag(words)
	# tagged_words_common = filter(lambda tag: tag[1] == 'O', tagged)
	# words = map(lambda tag: tag[0].lower(), tagged_words_common)
	# words = set(words)
	# print('Filtered common words:', len(words))
	#
	# Print names words (just for info)
	# tagged_names = list(filter(lambda tag: tag[1] != 'O', tagged))
	# print('Names words:', len(tagged_names))
	# print(tagged_names)

	# cast to lowercase
	words = set(map(str.lower, words))

	print('Processing words...')
	# Stemming to use stems as key
	download('stopwords')
	from nltk.stem import SnowballStemmer
	snowball_stemmer = SnowballStemmer('english', ignore_stopwords=True)
	# Lemmatize to use lemmas as base word
	download('wordnet')
	from nltk.corpus.reader import wordnet as wnr
	from nltk.corpus import wordnet

	# POS tagger
	download('averaged_perceptron_tagger')
	from nltk import pos_tag

	# Process words
	keyed_words = {}
	tagged_words = pos_tag(words)

	def tagged2str(word, tag): return '{} ({})'.format(word, tag)

	for word, tag in tagged_words:
		stem = snowball_stemmer.stem(word)
		str_word = tagged2str(word, tag)
		if stem in keyed_words:
			keyed_words[stem] += (str_word,)
		else:
			pos = wnr.VERB if tag in {'VB', 'VBP', 'VBZ', 'VBN', 'VBG', 'VBD', 'VERB'} else wnr.NOUN
			lemmas = wordnet._morphy(word, pos=pos)
			lemma = tagged2str(min(lemmas, key=len), pos) if lemmas else str_word
			keyed_words[stem] = (lemma, str_word)

	print('Keys count:', len(keyed_words))

	print('Writing file ', OUTFILE)

	def mapToCSVLine(item): return ','.join(
		map(str, (item[0],) + item[1])) + '\n'

	# Output to file
	with open(OUTFILE, 'w') as f:
		f.write(mapToCSVLine(('STEM', ('LEMMA', 'FORMS...'))))  # Header
		for key in sorted(keyed_words):
			f.write(mapToCSVLine((key, keyed_words[key])))

	print('Done! Use "{} --help" To know what abbreviations mean.'.format(sys.argv[0]))


if __name__ == "__main__":
	main()
