import csv, re, glob
# import dataframe


def collect_csv_files_from_directory(pathToDirectory):
    return glob.glob(pathToDirectory +r"/**/*.csv", recursive=True)
    

def pit_csv_cleaner(pathToFile):
	file_split = pathToFile.split('\\')

	with open(pathToFile, newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

		refactored_list = []
		for row in spamreader:
			x = row[0].split(',')
			if 'KILLED' in x or 'SURVIVED' in x:
				refactored_list.append(x)
				
				
	for r in refactored_list:
		mutator = re.search(r"^[A-Za-z](.+?)Mutator",r[1].split('.')[-1]).group(0)
		mutator_number = re.search(r"\d+",r[1].split('.')[-1]).group(0)
		
		testCase = r[0].split('.')[-1]
		status = r[2]
		with open(file_split[0]+'\\new_'+ file_split[1], 'a+', newline='', encoding="Latin-1") as myfile:
			wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
			wr.writerow([testCase, mutator, mutator_number, status])


def generate_tom_mutators_vs_tc():
	row_collection = []
	mutators_list = []
	# with open('PITcsv/new_output.csv', mode='r') as infile:
	with open('PITcsv/new_jcsv_output.csv', mode='r') as infile:
		reader = csv.reader(infile)
		
		for line in csv.reader(infile):
			row_dict = {}
			row_dict['testCase'] = line[0]
			row_dict['mutator'] = line[1]
			row_dict['line-no'] = line[2]
			row_dict['status'] = line[3]
			# print (line)
			row_collection.append(row_dict)
			mutators_list.append(row_dict['mutator'])

	mutators_list.sort()
	unique_mutators = list(set(mutators_list))
	
	csv_data_to_write = []
	
	for da in row_collection:
		i=0
		tmpdict = []
		tmpdict.append(da['testCase'])
		for un in unique_mutators:
			if da['mutator'].strip() == un.strip() and da['testCase'] != 'none':
				tmpdict.append(1)
				# tmpdict.append(da['status'])
			else:
				tmpdict.append(0)
		csv_data_to_write.append(tmpdict)


	header_list = ['']
	for u in unique_mutators:
		header_list.append(u)
	f = csv.writer(open("tom.csv", "a", newline='',  encoding="Latin-1"))
	f.writerow(header_list)
	for d in csv_data_to_write:
		f.writerow(d)


def generate_tom_run_vs_tc(inputFileName):
	row_collection = []
	mutators_list = []
	number_of_run_list = []
	with open('inputFileName', mode='r') as infile:
	# with open('PITcsv/new_jcsv_output.csv', mode='r') as infile:
		reader = csv.reader(infile)
		for line in csv.reader(infile):
			row_dict = {}
			row_dict['testCase'] = line[0]
			row_dict['mutator'] = line[1]
			row_dict['line-no'] = line[2]
			row_dict['status'] = line[3]
			# print (line)
			row_collection.append(row_dict)
			mutators_list.append(row_dict['mutator'])
			number_of_run_list.append(row_dict['line-no'])

	number_of_run_list.sort()
	unique_run_list = list(set(number_of_run_list))
	
	csv_data_to_write = []
	test_list = []
	for da in row_collection:
		i=0
		tmpdict = []
		tmpdict.append(da['testCase'])
		for un in unique_run_list:
			if da['line-no'].strip() == un.strip() and da['testCase'] != 'none':
				tmpdict.append(1)
			else:
				tmpdict.append(0)
		test_list.append(da['mutator'])
		csv_data_to_write.append(tmpdict)


	header_list = ['']
	header_2_list = ['']
	for ur in unique_run_list:
		header_list.append(ur)
	for tl in test_list:
		header_2_list.append(tl)

	f = csv.writer(open("tom_run_vs_tc.csv", "a", newline='',  encoding="Latin-1"))
	f.writerow(header_list)
	f = csv.writer(open("tom_run_vs_tc.csv", "a", newline='',  encoding="Latin-1"))
	f.writerow(header_2_list)
	for d in csv_data_to_write:
		f.writerow(d)




def generate_tom_run_vs_tc_2(inputFileName):
	row_collection = []
	mutators_list = []
	number_of_run_list = []
	with open(inputFileName, mode='r') as infile:
		reader = csv.reader(infile)
		for line in csv.reader(infile):
			row_dict = {}
			row_dict['testCase'] = line[0]
			row_dict['mutator'] = line[1]
			row_dict['line-no'] = line[2]
			row_dict['status'] = line[3]
			row_collection.append(row_dict)
			mutators_list.append(row_dict['mutator'])
			number_of_run_list.append(row_dict['line-no'])

	number_of_run_list.sort()
	unique_run_list = list(set(number_of_run_list))
	
	csv_data_to_write = []
	test_list = []
	for da in row_collection:
		i=0
		tmpdict = []
		tmpdict.append(da['testCase'])
		for un in unique_run_list:
			if da['line-no'].strip() == un.strip() and da['testCase'] != 'none':
				tmpdict.append(1)
			else:
				tmpdict.append(0)
		test_list.append([da['line-no'], da['mutator']])
		csv_data_to_write.append(tmpdict)


	header_list = ['']
	for ur in unique_run_list:
		header_list.append(ur)
	

	f = csv.writer(open(inputFileName+'_tom_1.csv', "a", newline='',  encoding="Latin-1"))
	f.writerow(header_list)
	for d in csv_data_to_write:
		f.writerow(d)
	f = csv.writer(open(inputFileName+'_tom_2.csv', "a", newline='',  encoding="Latin-1"))
	for t in test_list:
		f.writerow(t)


# files = collect_csv_files_from_directory("PITcsv")

# for f in files:
	# pit_csv_cleaner(f)

# generate_tom_run_vs_tc_2()