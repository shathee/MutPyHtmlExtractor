import os, glob, sys, re, fileinput, argparse
import csv
import yaml
import xml.etree.ElementTree as ET

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
	files = collect_all_files_from_directory_by_ext(path_to_directory, '.xml')
	all_tests = []
	for f in files:
		tree = ET.parse(f)
		root = tree.getroot()
		for x in root.iter('testcase'):
			all_tests.append(x.attrib['name'])

	print('total tests', len(all_tests))
	return all_tests
			# all_tests = []
	# for f in files:
	# 	print(f)
	# 	textfile = open(f, 'r', encoding="utf8")
	# 	fr = textfile.read()
	# 	r1 = re.search(r"(?s)(?<=@Test).*?(?=\(\))", fr)
	# 	if r1 != None:
	# 		all_tests.append(re.search(r"(?<=public void).*", r1.group(0)).group(0))

	# 	# with open(f) as of:
	# 	# 	for line in of:
	# 	# 		if "@Test" in line:
	# 	# 			nl = next(of, '').strip()
	# 	# 			print(nl)
	# 	# 			all_tests.append(re.search(r'test[a-zA-Z_0-9]+', nl).group(0))
	# print('total tests', len(all_tests))
	# # return all_tests

def parse_ld_file():
	files = collect_all_files_from_directory_by_ext('LDFiles\\java','.txt')
	all_tests = get_all_test_case_names('LDFiles\\surefire-reports')
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
			mutation_data_list.append(mutation_entity)
	
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
	flist = open(file, encoding='utf8').readlines()
	parsing = False
	data = []
	for line in flist:
		if line.startswith("[INFO] Results:") or line.startswith("Results:"):
			parsing = True
		if parsing:
			data.append(line)
		if line.startswith("\t**** [ERROR] Tests run:") or line.startswith("\t**** [ERROR] Tests run:"):
			parsing = False
	status = 'survived'
	for d in data:
		if tc in d:
			status = 'killed'
			break;
		else:
			status = 'survived'
	# textfile = open(file, 'r', encoding="utf8")
	# f = textfile.read()
	# r1 = re.search(r"(?s)(?<=Results :).*?(?=Tests run:)", f)
	# r1 = re.search(r"(?s)(?<=Results :).*?(?=Tests run:)", f)
	# if r1 != None:
	# 	if tc in r1.group(0):
	# 		status = 'killed'
	# 	else:
	# 		status = 'survived'
	# else:
	# 	status = 'survived'
	return status
	# print(data)

def write_to_csv(list_of_dict):
	for d in list_of_dict:
		with open('data.csv', 'a+', newline='', encoding="Latin-1") as myfile:
			wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
			wr.writerow([d['test_case'],d['operator'],d['mutation_node'],d['status']])


parse_ld_file()