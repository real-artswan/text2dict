#!/usr/bin/env python3

import os
import sys


def xml2text(file):
	import xml.etree.ElementTree as ET

	def parse(elem, texts):
		if (elem.text):
			texts.append(elem.text)
		for child in elem.findall('*'):
			parse(child, texts)

	tree = ET.parse(file)
	root = tree.getroot()
	texts = []
	parse(root, texts)
	return texts


def main():
	if len(sys.argv) < 2:
		raise Exception('Specify an input file!')
	inputFile = sys.argv[1]
	outputFile = inputFile + '.txt'
	path_pair = os.path.splitext(inputFile)
	ext = path_pair[1]
	if ext.lower() == '.fb2':  # it is a raw XML file
		texts = xml2text(inputFile)
	else:
		if ext.lower() == '.zip':  # it must be a zipped FB2
			# try to pull xml from archive
			import zipfile
			zip = zipfile.ZipFile(inputFile, 'r')
			# seek for an fb2 file in the archive
			fb2file = next((f for f in zip.namelist()
							if f.lower().endswith('.fb2')), None)
			if fb2file == None:
				raise Exception('This ZIP archive is not an FB2 archive!')
			texts = xml2text(zip.open(fb2file, 'r'))

	# dump text to a file
	with open(outputFile, 'w') as f:
		for t in texts:
			f.write(t + '\n')


if __name__ == "__main__":
	main()
