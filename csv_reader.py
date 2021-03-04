import csv, re


def pit_csv_cleaner(pathToFile):
	with open('output.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

		refactored_list = []
		for row in spamreader:
			x = row[0].split(',')
			if 'KILLED' in x:
				refactored_list.append(x)
				
				
	for r in refactored_list:
		mutator = re.search(r"^[A-Za-z](.+?)Mutator",r[1].split('.')[-1]).group(0)
		testCase = r[0]
		status = r[2]
		with open('new_output.csv', 'a+', newline='', encoding="Latin-1") as myfile:
			wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
			wr.writerow([mutator, testCase, status])