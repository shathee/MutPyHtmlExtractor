import os, glob, sys, re, fileinput, argparse

from bs4 import BeautifulSoup
import csv
import yaml

from collections import OrderedDict
'''
finds all html files in the folder and subfolders 
'''
def collect_files_from_directory(pathToDirectory):
    # return glob.glob(pathToDirectory +r"/**/*.html", recursive=True)
    return glob.glob(pathToDirectory +r"/**/*", recursive=True)

'''
parse the file given as parameter and saves the information in csv format
'''

def parse_ld_file():
	files = collect_files_from_directory('LDFiles')
	for f in files:
		dir_name = f.split("\\")[0]
		file_name = f.split("\\")[-1]
		file_ext = file_name.split(".")
		if(file_ext[-1] == 'txt'):
			print(file_ext[0])
			print(get_mutant_operator(dir_name+'\\'+file_ext[0]+'.java'))
			# get_mutant_operator()


def get_mutant_operator(path):
	with open(path) as f:
		for line in f:
			if line.startswith("mutant type:"):
				mo = line.split(' ')[-1]
	return mo.strip()


parse_ld_file()