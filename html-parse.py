import os, glob, sys, re, fileinput, argparse

from bs4 import BeautifulSoup
import csv


'''
finds all html files in the folder and subfolders 
'''
def collect_files_from_directory(pathToDirectory):
    return glob.glob(pathToDirectory +r"/**/*.html", recursive=True)

'''
parse the file given as parameter and saves the information in csv format
'''
def parse_index_html(pathToDirectory):
	soup = BeautifulSoup (open(pathToDirectory), features="lxml")

	f = csv.writer(open("index.csv", "w"))
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


file_list = collect_files_from_directory('html_report')

for f in file_list:
	if(re.search(r"(index)(\.html)$",f)):
		parse_index_html(f)
	elif(re.search(r"([0-9])(\.html)$",f)):
		print('2nd typ', f)
	else:
		print("no Html file found")


# soup = BeautifulSoup(html_text, 'html.parser')
# 	with open(f, 'r', encoding='utf-8') as infile:
# 		for line in infile:
# 			print(line)





# mutatant_total = mutation_time_tag.parent.parent
# print(mutatant_total)
# \<\/(strong)\>(.)
# print(mutation_score.find_previous_siblings("strong"))

# for link in links:
	# print(link)
    # names = link.contents[0]
    # fullLink = link.get('class')

    # f.writerow([no_of_tests,mutation_score,successful_mutants,survived_mutants,incompetent_mutants,timeout_mutants])
# for span in soup.find_all('span'):
#     print(span.get('class'))