import sys,os,re

def exit_gracefully():
	print('\033[91m  ------------------------	 @@@ Bye Bye!!! @@@  ------------------------\033[0m')

def help():
	print("\nHelp Menu:\n\n- You have to indicate as first argument the path [ ex. /var/log/irondome/ ]\n")
	print("- Second and next arguments indicate the extensions you want to follow [ ex. .txt .pdf ... ]\n")
	print("- Example:\n\n./irondome  /var/log/irondome/ .txt .pdf .key\n\n")
	exit_gracefully()

def main():
	arg = sys.argv
	to_set = set()
	to_watch = []
	if len(arg) > 1:
		if (arg[1][0] == '-'):
			if (arg[1] == '--help') or (arg[1] == '-h'):
				help()
			else:
				print("\nThis argument is not alowed\n")
		else:
			path = arg[1]
			if os.path.exists(path) == False:
				print(f"\nPath {path} not exist!Try again!\n")
			else:
				if path[-1] != '/':
					path = arg[1]+'/'
				for argument in range(2,len(arg)):
					ext = arg[argument]
					ext = re.sub(r'[^a-zA-Z0-9.]+','', ext)
					if ext != '':
						if ext[0] != '.':
							ext = '.'+ext
						to_set.add('*'+ext)
						to_watch = list(to_set)
				print(" \n\033[1mPath to follow:\n\n*** \033[0m \033[95m" + path + "\033[0m ***")
				print(" \n\033[1mExtension(s) to follow:\n\n*** \033[0m \033[95m" + str(to_watch) + "\033[0m ***")
	else:
		print("\nAdd at least 1 argument! Try again!.\n")

if __name__=="__main__":
	main()