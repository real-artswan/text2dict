# Extracts dictionary from text
It coverts a text file to a CSV dictionary table

Requirements: nltk package, to install do `pip install nltk`

# Usage
Run `python text2dict.py <path to text file>`
Also there is an utility script `./extras/dumpfb2.py` that can dump fb2 file to a plain text file

# Output
CSV columns are:

*STEM* is a stem key (https://en.wikipedia.org/wiki/Stemming)

*LEMMA* is a general form of a word chosen by word form (https://en.wikipedia.org/wiki/Lemmatisation)
*(v)* stands for verb and *(n)* stands for noun, other values mean that lemma was not found and original word was used instead

*FORMS...* this column and all next columns contain forms of words exist in the text and keyed by STEM
