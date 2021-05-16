import sys, getopt

from distance_calculator import calculate_distances, calculate_distances_manual


def main(argv):
	
	inputfile = ''
	outputfile = ''
	directory = False
	if len(argv) <=0:
		print("please provide valude arguments")
	try:
		opts, args = getopt.getopt(argv,"hf:m:",["file="])
	except getopt.GetoptError:
		print ('distance.py -f <file>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print ('distance.py -f <file>')
			sys.exit()
		elif opt in ("-f"):
			calculate_distances(arg)
		elif opt in ("-m"):
			calculate_distances_manual(arg)
			


if __name__ == "__main__":
	main(sys.argv[1:])