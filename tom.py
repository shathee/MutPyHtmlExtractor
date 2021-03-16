import sys, getopt
from csv_reader import generate_tom_run_vs_tc_2
from csv_reader import collect_csv_files_from_directory


def main(argv):
	
	inputfile = ''
	outputfile = ''
	directory = False
	if len(argv) <=0:
		print("please provide valude arguments")
	try:
		opts, args = getopt.getopt(argv,"hf:d:",["file=","dir="])
	except getopt.GetoptError:
		print ('tom.py -f <file> -d <directory>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print ('tom.py -f <file> -d <directory>')
			sys.exit()
		elif opt in ("-f", "--file"):
			inputfile = arg
			directory = False
		elif opt in ("-d", "--dir"):
			inputdir = arg
			directory = True


	if(directory):
		files = collect_csv_files_from_directory(inputdir)
		for f in files:
			generate_tom_run_vs_tc_2(f)
	else:
		generate_tom_run_vs_tc_2(inputfile)



if __name__ == "__main__":
	main(sys.argv[1:])