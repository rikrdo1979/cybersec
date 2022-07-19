import sys
import getopt

def arguments():
    url_input = None
    level = None
    path = "./data/"
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, "r:l:p:")
    except:
        print("Error")
    for opt, arg in opts:
        if opt in ['-r']:
            url_input = arg
        elif opt in ['-l']:
            level = arg
        elif opt in ['-p']:
            path = arg
	
	print(type(url_input))
    print(url_input)

arguments()