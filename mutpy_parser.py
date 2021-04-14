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
def parse_index_html(pathToDirectory):
	soup = BeautifulSoup (open(pathToDirectory), features="lxml")

	f = csv.writer(open("index.csv", "w",  encoding="Latin-1"))
	f.writerow(["No of Tests", "Mutation Score", "successful", "survived", "incompetent", "timeout"])    # Write column headers as the first line
	no_of_tests_text = soup.find('h4', string=re.compile(r'^(Tests)[\s\Sa-zA-Z0-9\[\]]*$')).getText()
	no_of_tests = re.findall(r"([0-9]*)", no_of_tests_text)
	no_of_tests = [element for element in no_of_tests if element]
	print(no_of_tests)
	mutation_score_tag = soup.find('span', class_=re.compile("glyphicon-signal"))
	mutation_score_text = mutation_score_tag.parent.parent.getText()
	mutation_score = re.findall(r"([0-9\.]*\%$)", mutation_score_text)
	print(mutation_score)
	mutation_time_tag = soup.span

	successful_mutants_text = soup.find('span', class_=re.compile("label label-success")).parent.getText()
	successful_mutants = re.findall(r"[0-9]*$", successful_mutants_text)
	print(successful_mutants)

	survived_mutants_text = soup.find('span', class_=re.compile("label label-danger")).parent.getText()
	survived_mutants = re.findall(r"[0-9]*$", survived_mutants_text)
	print(survived_mutants)

	incompetent_mutants_text = soup.find('span', class_=re.compile("label label-warning")).parent.getText()
	incompetent_mutants = re.findall(r"[0-9]*$", incompetent_mutants_text)
	print(incompetent_mutants)

	timeout_mutants_text = soup.find('span', class_=re.compile("label label-info")).parent.getText()
	timeout_mutants = re.findall(r"[0-9]*$", timeout_mutants_text)
	print(timeout_mutants)
	
	f.writerow([no_of_tests[0],mutation_score[0],successful_mutants[0],survived_mutants[0],incompetent_mutants[0],timeout_mutants[0]])


def parse_mutpy_yaml(pathToDirectory):
	
	data_all = []
	with open(pathToDirectory) as file:
		data_list = yaml.load(file, Loader=yaml.BaseLoader)
		
		for key, value in data_list.items():
			if(type(data_list['mutations']) != "null"):
				new_data = data_list['mutations']
		for d in new_data:
			data = {}
			# data['killer'] = 'none' if (d['killer'] == 'null') else d['killer']
			# data['lineno'] = d['mutations'][0]['lineno']
			# data['operator'] = d['mutations'][0]['operator']
			# data['status'] = d['status']
			if d['killer'] != 'null' :
				data['killer'] = d['killer']
				data['lineno'] = d['mutations'][0]['lineno']
				data['operator'] = d['mutations'][0]['operator']
				data['status'] = d['status']
				data_all.append(data)
			
	# print(data_all)
	f = csv.writer(open("data2.csv", "a", newline='',  encoding="Latin-1"))
	for d in data_all:
		f.writerow([d['killer'],d['operator'],d['lineno'],d['status']])

def num_operator_vs_tc(pathToDirectory):
	
	data_all = []
	with open(pathToDirectory) as file:
		data_list = yaml.load(file, Loader=yaml.BaseLoader)
		
		for key, value in data_list.items():
			if(type(data_list['mutations']) != "null"):
				new_data = data_list['mutations']
		for d in new_data:
			data = {}
			data['killer'] = d['killer']
			data['lineno'] = d['mutations'][0]['lineno']
			data['operator'] = d['mutations'][0]['operator']
			data['status'] = d['status']
			data_all.append(data)
			
	# print(data_all)




# file_list = collect_files_from_directory('yml_report')
# for f in file_list:
# 	parse_operator_html(f)


parse_mutpy_yaml('yml_report/forex_py_full')