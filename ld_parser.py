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
	all_files = collect_files_from_directory('LDFiles')
	files, dirs = get_files_to_parse(all_files)
	directory = '\\'.join(dirs)
	# print(directory)
	mutation_data_list = []
	for f in files:
		mutation_entity = {}
		mutation_entity['operator'] = get_mutant_operator(directory+'\\'+f +'.java')
		mutation_entity['mutation_node'] = get_mutantion_node(directory+'\\'+f +'.java')
		mutation_entity['mutation_no_in_file'] = f
		mutation_data_list.append(mutation_entity)
	print(mutation_data_list)


def get_mutant_operator(file):
	with open(file) as f:
		for line in f:
			if line.startswith("mutant type:"):
				mo = line.split(' ')[-1]
	return mo.strip()

def get_mutantion_node(file):
	with open(file) as f:
		for line in f:
			if line.startswith("----> mutated node:"):
				mn = line.split(' ')[-1]
	return mn.strip()


def get_failed_test(file):
	with open(file) as f:
		for line in f:
			if line.startswith("Failed tests:"):
				ft = line.split(' ')[-1]
	return ft.strip()

def get_files_to_parse(files):
	test = []
	for f in files:
		r = f.split('\\')
		test.append(r[-1].split('.')[0])
	return list(set(i for i in test if test.count(i) > 1)), r[0:-1]
	


parse_ld_file()