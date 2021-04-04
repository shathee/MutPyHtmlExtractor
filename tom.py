import sys, getopt
from csv_reader import generate_tom_run_vs_tc_2
from csv_reader import generate_tom_run_vs_tc
from csv_reader import generate_tom_run_tc_op
from csv_reader import collect_csv_files_from_directory
from csv_reader import pit_csv_cleaner


def main(argv):
	
	inputfile = ''
	outputfile = ''
	directory = False
	if len(argv) <=0:
		print("please provide valude arguments")
	try:
		opts, args = getopt.getopt(argv,"hf:d:cp:",["file=","dir=","cleanPIT="])
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
			generate_tom_run_tc_op(inputfile)
		elif opt in ("-d", "--dir"):
			inputdir = arg
			# directory = True
			files = collect_csv_files_from_directory(inputdir)
			for f in files:
				generate_tom_run_tc_op(f)
		elif opt in ("-cp", "--cleanPIT"):
			pit_csv_cleaner(arg)


	# if(directory):
	# 	files = collect_csv_files_from_directory(inputdir)
	# 	for f in files:
	# 		# generate_tom_run_vs_tc(f)
	# 		# generate_tom_run_vs_tc_2(f)
	# 		generate_tom_run_tc_op(f)
	# else:
	# 	# generate_tom_run_vs_tc(inputfile)	
	# 	# generate_tom_run_vs_tc_2(inputfile)
	# 	generate_tom_run_tc_op(inputfile)



if __name__ == "__main__":
	main(sys.argv[1:])