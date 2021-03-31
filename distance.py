import sys, getopt

# from csv_reader import collect_csv_files_from_directory


def main(argv):
	
	inputfile = ''
	outputfile = ''
	directory = False
	if len(argv) <=0:
		print("please provide valude arguments")
	try:
		opts, args = getopt.getopt(argv,"hf:",["file="])
	except getopt.GetoptError:
		print ('distance.py -f <file>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print ('distance.py -f <file>')
			sys.exit()
		elif opt in ("-f"):
			print('infile')
			


if __name__ == "__main__":
	main(sys.argv[1:])