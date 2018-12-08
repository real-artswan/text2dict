# Extracts dictionary from a text
It coverts a text file to a CSV dictionary table

Requirements: nltk package, to install do `pip install nltk`

# Usage
Run `python text2dict.py <path to text file>`. It will output the "unique_words.csv" file.

Run `python text2dict.py --help` to see what abbreviations in the output CSV file mean.

Also there is an utility script `./extras/dumpfb2.py` that dumps fb2 file to a plain text file. Output file will have a ".txt" extension.

# Output
CSV columns are:

*STEM* is a stem key (https://en.wikipedia.org/wiki/Stemming)

*LEMMA* is a general form of a word chosen by word form (https://en.wikipedia.org/wiki/Lemmatisation)

*(v)* stands for a verb and *(n)* stands for a noun, other values mean that lemma was not found and original word was used instead.

*FORMS...* this column and all next columns contain forms of the word exists in the text and keyed by STEM.
