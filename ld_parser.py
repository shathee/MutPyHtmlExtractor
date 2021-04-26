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



def parse_ld_file():
	files = collect_files_from_directory('LDFiles')
	mutation_data_list = []
	for f in files:
		mutation_entity = {}
		dir_name = f.split("\\")[0:-2]
		file_name = f.split("\\")[-1]
		print(dir_name, file_name)
		file_ext = file_name.split(".")
		if(file_ext[-1] == 'txt'):
			mutation_entity['operator'] = get_mutant_operator(dir_name+'\\'+file_ext[0]+'.java')
			mutation_entity['mutation_no'] = file_ext[0]
		mutation_data_list.append(mutation_entity)
	# print(mutation_data_list)


def get_mutant_operator(path):
	with open(path) as f:
		for line in f:
			if line.startswith("mutant type:"):
				mo = line.split(' ')[-1]
	return mo.strip()


def get_failed_test(path):
	with open(path) as f:
		for line in f:
			if line.startswith("Failed tests:"):
				ft = line.split(' ')[-1]
	return ft.strip()

def get_files_to_parse(files):
	test = []
	for d in f:
		s = d.split('\\')
		test.append(s[-1].split('.')[0])

	return list(set(i for i in test if test.count(i) > 1))
	