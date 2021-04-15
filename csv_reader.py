import csv, re, glob
# import dataframe
import calendar
import time
import itertools

def collect_csv_files_from_directory(pathToDirectory):
    return glob.glob(pathToDirectory +r"/**/*.csv", recursive=True)
    

def pit_csv_cleaner(pathToFile):
	file_split = pathToFile.split('\\')

	with open(pathToFile, newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

		refactored_list = []
		for row in spamreader:
			x = row[0].split(',')
			# if 'KILLED' in x or 'SURVIVED' in x:
			if 'KILLED' in x:
				refactored_list.append(x)
				
				
	for r in refactored_list:
		mutator = re.search(r"^[A-Za-z](.+?)Mutator",r[1].split('.')[-1]).group(0)
		mutator_number = re.search(r"\d+",r[1].split('.')[-1]).group(0)
		
		testCase = r[0].split('.')[-1]
		status = r[2]
		with open('cleaned_'+ file_split[-1], 'a+', newline='', encoding="Latin-1") as myfile:
			wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
			wr.writerow([testCase, mutator, mutator_number, status])


def generate_tom_mutators_vs_run(inputFileName):
	row_collection = []
	mutators_list = []
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

	csv_data_to_write = []

	for row in row_collection:
		tmp_arr = []
		tmp_arr.append(row['mutator'])
		tmp_arr.append(row['line-no'])
		csv_data_to_write.append(tmp_arr)

	
	
	f = csv.writer(open("mutators_vs_run_"+inputFileName, "a", newline='',  encoding="Latin-1"))
	for d in csv_data_to_write:
		f.writerow(d)


def generate_tom_run_vs_tc(inputFileName):
	row_collection = []
	mutators_list = []
	number_of_run_list = []
	testcase_list = []
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
			testcase_list.append(row_dict['testCase'])

	
	csv_data_to_write = []
	
	# distinct_runs = list(set(number_of_run_list))
	# print(number_of_run_list)

	for tc in list(set(testcase_list)):
		test_list = []
		test_list.append(tc)
		for row in row_collection:
			if tc == row['testCase']:
				test_list.append(1)
			else:
				test_list.append(0)
		# print(test_list)
		csv_data_to_write.append(test_list)

	# print(csv_data_to_write)

	header_list = number_of_run_list
	header_list.insert(0, ' ')
	# print(header_list)

	f = csv.writer(open("tom_run_vs_tc_"+inputFileName, "a", newline='',  encoding="Latin-1"))
	f.writerow(header_list)
	for d in csv_data_to_write:
		f.writerow(d)




# def generate_tom_run_vs_tc_2(inputFileName):
# 	row_collection = []
# 	mutators_list = []
# 	number_of_run_list = []
# 	with open(inputFileName, mode='r') as infile:
# 		reader = csv.reader(infile)
# 		for line in csv.reader(infile):
# 			row_dict = {}
# 			row_dict['testCase'] = line[0]
# 			row_dict['mutator'] = line[1]
# 			row_dict['line-no'] = line[2]
# 			row_dict['status'] = line[3]
# 			row_collection.append(row_dict)
# 			mutators_list.append(row_dict['mutator'])
# 			number_of_run_list.append(row_dict['line-no'])

# 	number_of_run_list.sort()
# 	unique_run_list = list(set(number_of_run_list))
# 	new_row_collection = [i for n, i in enumerate(row_collection) if i not in row_collection[n + 1:]]

# 	csv_data_to_write = []
# 	test_list = []
# 	for da in new_row_collection:
# 		i=0
# 		tmpdict = []
# 		tmpdict.append(da['testCase'])
# 		for un in unique_run_list:
# 			if da['line-no'].strip() == un.strip() and da['testCase'] != 'none':
# 				tmpdict.append(1)
# 			else:
# 				tmpdict.append(0)
# 		test_list.append([da['line-no'], da['mutator']])
# 		csv_data_to_write.append(tmpdict)


# 	header_list = ['']
# 	for ur in unique_run_list:
# 		header_list.append(ur)
	

# 	f = csv.writer(open(inputFileName+'_tom_1.csv', "a", newline='',  encoding="Latin-1"))
# 	f.writerow(header_list)
# 	for d in csv_data_to_write:
# 		f.writerow(d)
# 	f = csv.writer(open(inputFileName+'_tom_2.csv', "a", newline='',  encoding="Latin-1"))
# 	for t in test_list:
# 		f.writerow(t)


# def generate_tom_run_tc_op(inputFileName):
# 	row_collection = []
# 	mutators_list = []
# 	number_of_run_list = []
# 	with open(inputFileName, mode='r') as infile:
# 		reader = csv.reader(infile)
# 		for line in csv.reader(infile):
# 			row_dict = {}
# 			row_dict['testCase'] = line[0]
# 			row_dict['mutator'] = line[1]
# 			row_dict['line-no'] = line[2]
# 			row_dict['status'] = line[3]
# 			row_collection.append(row_dict)
# 			mutators_list.append(row_dict['mutator'])
# 			number_of_run_list.append(row_dict['line-no'])

# 	csv_data_to_write = []
# 	res = {}
# 	for d in row_collection:
# 		tmpdict = {}
# 		tmpdict['testCase'] = d['testCase']
# 		tmpdict['mutator'] = d['mutator']
# 		tmpdict['status'] = d['status']
		
# 		res.setdefault(d['line-no'], []).append(tmpdict)
		
	
# 	k_arr = []
# 	m_arr = []
# 	data_arr = []
# 	for k,v in res.items():
# 		td = []
# 		for vv in v:
# 			k_arr.append(k)
# 			m_arr.append(vv['mutator'])
		
# 	for da in row_collection:
# 		tmpdict = []
# 		print(da['testCase'], '----')
# 		if da['testCase'] != 'none':
# 			tmpdict.append(da['testCase'])
# 			for f, b in zip(k_arr, m_arr):
# 				if da['line-no'].strip() == f.strip() and da['mutator'] == b and da['status'].lower() =='killed' and da['testCase'] != 'none':
# 					tmpdict.append(1)
# 				else:
# 					tmpdict.append(0)
# 			csv_data_to_write.append(tmpdict)

		
# 	new_k = []
# 	for elem in csv_data_to_write:
# 	    if elem not in new_k:
# 	        new_k.append(elem)
# 	csv_data_to_write = new_k

# 	k_arr.insert(0, '')
# 	m_arr.insert(0, '')

# 	ts = calendar.timegm(time.gmtime())
# 	f = csv.writer(open(str(ts)+'_tom.csv', "a", newline='',  encoding="Latin-1"))
# 	f.writerow(k_arr)
# 	f.writerow(m_arr)
# 	for c in csv_data_to_write:
# 		f.writerow(c)

def generate_tom_run_tc_op(inputFileName):
	row_collection = []
	mutators_list = []
	number_of_run_list = []
	with open(inputFileName, mode='r') as infile:
		reader = csv.reader(infile)
		i = 1
		for line in csv.reader(infile):
			row_dict = {}
			row_dict['testCase'] = line[0]
			row_dict['mutator'] = line[1]
			row_dict['line-no'] = line[2]
			row_dict['status'] = line[3]
			row_dict['item-no'] = i 
			row_collection.append(row_dict)
			mutators_list.append(row_dict['mutator'])
			number_of_run_list.append(row_dict['line-no'])
			i +=1

	csv_data_to_write = []
	res = {}
	for d in row_collection:
		tmpdict = {}
		tmpdict['testCase'] = d['testCase']
		tmpdict['mutator'] = d['mutator']
		tmpdict['status'] = d['status']
		tmpdict['item-no'] = d['item-no']
		
		res.setdefault(d['line-no'], []).append(tmpdict)
		
	
	# print(res)
	k_arr = []
	m_arr = []
	item_arr = []
	for k,v in res.items():
		for vv in v:
			k_arr.append(k)
			m_arr.append(vv['mutator'])
			# item_arr.append(vv['item-no'])


	for da in row_collection:
		tmpdict = []
	
		tmpdict.append(da['testCase'])
		for f, b in zip(k_arr, m_arr):
			if da['line-no'].strip() == f.strip() and da['mutator'] == b:
				tmpdict.append(1)
			else:
				tmpdict.append(0)
		csv_data_to_write.append(tmpdict)
	# print(csv_data_to_write)
	new_k = []
	for elem in csv_data_to_write:
	    if elem not in new_k:
	        new_k.append(elem)
	csv_data_to_write = new_k

	k_arr.insert(0, '')
	m_arr.insert(0, '')
	file_split = inputFileName.split('\\')[-1].split('.')[-2]
	# print(file_split[-2])
	ts = calendar.timegm(time.gmtime())
	f = csv.writer(open(str(ts)+'_'+file_split+'_tom.csv', "a", newline='',  encoding="Latin-1"))
	f.writerow(k_arr)
	f.writerow(m_arr)
	for c in csv_data_to_write:
		f.writerow(c)


def clean_tom_run_tc_op(inputFileName):
	csv_data_to_write = []
	lines_arr = []
	mutators_arr = []
	d_lst = []
	csv_data_to_write = []
	with open(inputFileName, mode='r') as infile:
	    r = csv.reader(infile)
	    lines_arr = next(r)
	    mutators_arr = next(r)
	    for line in csv.reader(infile):
	    	d_lst.append(line)
	
	temp_tc_arr = []
	temp_csv_arr = []
	temp_dict = {}
	f_dict = {}


	for d in d_lst:
		temp_tc_arr.append(d[0])

	for tc in temp_tc_arr:
		for d in d_lst:
			if tc == d[0] and d[0] not in f_dict:
				f_dict[tc]= d[1:]
			elif tc == d[0] and d[0] in f_dict:
				arr1 = f_dict[tc]
				arr2 = d[1:]
				x = list(zip(arr1, arr2))
				for i in range(len(x)):
					if x[i][0] == '1' or x[i][1] == '1':
						f_dict[tc][i] = '1'
					
	# for d in d_lst:
	# 	print(temp_tc_arr)
	# 	if(d[0] not in temp_tc_arr):
	# 		f_dict[d[0]] = d[1:]
	# 		temp_dict[d[0]] = d[1:]
	# 		temp_tc_arr.append(d[0])
	# 	else:
	# 		dd = d[1:]
	# 		ind = f_dict[d[0]]
	# 		i = 0
	# 		for i in range(len(dd)):
	# 			if dd[i] == '1' or ind[i] == '1':
	# 				temp_dict[d[0]][i] = '1'

	temp_dict = f_dict			

	for k, v in temp_dict.items():
		v.insert(0, k)
		temp_csv_arr.append(v)
	f = csv.writer(open('final_'+inputFileName, "a", newline='',  encoding="Latin-1"))
	f.writerow(lines_arr)
	f.writerow(mutators_arr)
	for c in temp_csv_arr:
		f.writerow(c)
			
	
	
## calling functions


# files = collect_csv_files_from_directory("PITcsv")

# for f in files:
# 	pit_csv_cleaner(f)

# generate_tom_run_vs_tc_2()

#generate_tom_mutators_vs_tc()

# generate_tom_run_tc_op('PITcsv/cleaned_csv_output.csv')

# clean_tom_run_tc_op('1617187551_tom.csv')