#!/usr/bin/env python3
# Aris Adamantiadis 2022
# MIT Licensed

import os
import sys
import glob

def cleanup(a, b):
	files = a + b
	for f in files:
		os.unlink(f)

def main(args):
	if len(args) != 2:
		print("Usage: twosided-scan.py front-side.pdf back-side.pdf")
		print("Back sided pdf is expected to be scanned reverse last to first page.")
		return
	rc = os.system("qpdf --version > /dev/null")
	if rc != 0:
		print("qpdf is needed for this script. Please install qpdf and try again.")
	recto = glob.glob('recto-*.pdf')
	verso = glob.glob('verso-*.pdf')
	if len(recto) != 0 or len(verso) != 0:
		print("Please remove any file recto-*.pdf or verso-*.pdf and try again")
		return
	rc = os.system("qpdf --split-pages %s recto.pdf"%(args[0],))
	if rc != 0:
		print("qpdf error")
		return
	rc = os.system("qpdf --split-pages %s verso.pdf"%(args[1],))
	if rc != 0:
		print("qpdf error")
		return
	recto = glob.glob('recto-*.pdf')
	verso = glob.glob('verso-*.pdf')
	if len(recto) != len(verso):
		print("Different number of pages")
		cleanup(recto, verso)
		return
	recto.sort()
	verso.sort()
	verso.reverse()
	pages = []
	for i in zip(recto, verso):
		pages += i
	print(pages)
	rc = os.system("qpdf --empty recto_verso.pdf --pages %s --"%(
		" ".join(pages),))
	if rc != 0:
		print("qpdf error")
	cleanup(recto, verso)

if __name__=="__main__":
	main(sys.argv[1:])