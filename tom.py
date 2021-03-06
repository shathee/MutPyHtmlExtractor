import sys, getopt
from csv_reader import generate_tom_run_vs_tc
from csv_reader import generate_tom_mutators_vs_run
from csv_reader import generate_tom_run_tc_op
from csv_reader import generate_tom_run_tc_op_ld
from csv_reader import collect_csv_files_from_directory
from csv_reader import pit_csv_cleaner
from csv_reader import clean_tom_run_tc_op
import time
from datetime import timedelta



def main(argv):
	
	inputfile = ''
	outputfile = ''
	directory = False
	if len(argv) <=0:
		print("please provide valude arguments")
	try:
		opts, args = getopt.getopt(argv,"hf:d:c:k:m:r:",["file=","dir=","cleanPIT=","cleanTOM=","tomMutator=","tomRun="])
	except getopt.GetoptError:
		print ('please put right aruguments, try tom.py -h for details')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print ('tom.py -f <file> -d <directory>')
			sys.exit()
		elif opt in ("-f", "--file"):
			inputfile = arg
			directory = False
			generate_tom_run_tc_op_ld(inputfile)
		elif opt in ("-d", "--dir"):
			inputdir = arg
			# directory = True
			files = collect_csv_files_from_directory(inputdir)
			for f in files:
				generate_tom_run_tc_op_ld(f)
		elif opt in ("-c", "--cleanPIT"):
			pit_csv_cleaner(arg)
		elif opt in ("-k", "--cleanTOM"):
			clean_tom_run_tc_op(arg)
		elif opt in ("-m"):
			generate_tom_mutators_vs_run(arg)
		elif opt in ("-r"):
			generate_tom_run_vs_tc(arg)
			





if __name__ == "__main__":
	start_time = time.time()
	main(sys.argv[1:])
	# print(time.time() - start_time)
	print(str(timedelta(seconds=time.time() - start_time)))