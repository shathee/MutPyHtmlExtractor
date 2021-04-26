import os, glob, sys, re, fileinput, argparse
import csv
import yaml

from collections import OrderedDict
'''
finds all html files in the folder and subfolders 
'''
def collect_files_from_directory(pathToDirectory):
    # return glob.glob(pathToDirectory +r"/**/*.html", recursive=True)
    return glob.glob(pathToDirectory +r"/**/*", recursive=True)

def collect_all_files_from_directory_by_ext(path_to_directory, ext):
    return glob.glob(path_to_directory +r"/**/*"+ext, recursive=True)

def get_all_test_case_names(path_to_directory):
	files = collect_all_files_from_directory_by_ext(path_to_directory, '.java')
	print(files)

def parse_ld_file():
	files = collect_all_files_from_directory_by_ext('LDFiles','.txt')
	
	mutation_data_list = []
	for f in files:
		mutation_entity = {}
		directory = '\\'.join(f.split('\\')[0:-1])
		mutation_entity['operator'] = get_mutant_operator(directory+'\\'+f.split('\\')[-1].split('.')[0] +'.java')
		mutation_entity['mutation_node'] = get_mutantion_node(directory+'\\'+f.split('\\')[-1].split('.')[0] +'.java')
		print(get_failed_test(f))
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


def get_tests(file):
	with open(file) as f:
		for line in f:
			failed_test = re.search(r"Failed tests:", line) 
			errored_test = re.search(r"Tests in error:", line) 
			skipped_test = re.search(r"Tests in error:", line) 
			 
			if failed_test != None:
				ft = failed_test.group(0)
			if errored_test!=None: 
				et = errored_test.group(0)
	return ft

	


# parse_ld_file()
get_all_test_case_names()