import os, glob, sys, re, fileinput, argparse
import csv
import yaml

from collections import Counter
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
	all_tests = []
	for f in files:
		with open(f) as of:
			for line in of:
				if "@Test" in line:
					nl = next(of, '').strip()
					all_tests.append(re.search(r'test[a-zA-Z_0-9]+', nl).group(0))
	return all_tests

def parse_ld_file():
	files = collect_all_files_from_directory_by_ext('LDFiles','.txt')
	all_tests = get_all_test_case_names('LDFiles\\test')
	# print(files)
	mutation_data_list = []
	
	for f in files:
		for tc in all_tests:
			mutation_entity = {}
			directory = '\\'.join(f.split('\\')[0:-1])
			mutation_entity['test_case'] = tc
			mutation_entity['status'] = get_failed_status(f, tc)
			mutation_entity['operator'] = get_mutant_operator(directory+'\\'+f.split('\\')[-1].split('.')[0] +'.java')
			mutation_entity['mutation_node'] = get_mutantion_node(directory+'\\'+f.split('\\')[-1].split('.')[0] +'.java')
			# print(mutation_entity)
			mutation_data_list.append(mutation_entity)
	# print(len(mutation_data_list))
	write_to_csv(mutation_data_list)
	c = Counter()
	for item in mutation_data_list:
	    c[item["status"]] += 1
	print(c)



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


def get_failed_status(file, tc):
	textfile = open(file, 'r')
	f = textfile.read()
	r1 = re.search(r"(?s)(?<=Results :).*?(?=Tests run:)", f)
	if r1 != None:
		if tc in r1.group(0):
			status = 'killed'
		else:
			status = 'survived'
	else:
		status = 'survived'
	return status

def write_to_csv(list_of_dict):
	for d in list_of_dict:
		with open('data.csv', 'a+', newline='', encoding="Latin-1") as myfile:
			wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
			wr.writerow([d['test_case'],d['operator'],d['mutation_node'],d['status']])


parse_ld_file()