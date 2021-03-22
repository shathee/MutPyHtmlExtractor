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
		opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print ('distance.py -i <file> -o <file>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print ('tom.py -i <file> -o <file>')
			sys.exit()
		elif opt in ("-i", "--ifile"):
			print('infile')
		elif opt in ("-o", "--ofile"):
			print('onfile')
			


if __name__ == "__main__":
	main(sys.argv[1:])