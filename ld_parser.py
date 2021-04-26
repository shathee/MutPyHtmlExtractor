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

def collect_all_text_files(pathToDirectory):
    return glob.glob(pathToDirectory +r"/**/*.txt", recursive=True)


def parse_ld_file():
	files = collect_all_text_files('LDFiles')
	
	mutation_data_list = []
	for f in files:
		mutation_entity = {}
		directory = '\\'.join(f.split('\\')[0:-1])
		mutation_entity['operator'] = get_mutant_operator(directory+'\\'+f.split('\\')[-1].split('.')[0] +'.java')
		mutation_entity['mutation_node'] = get_mutantion_node(directory+'\\'+f.split('\\')[-1].split('.')[0] +'.java')
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

	


parse_ld_file()