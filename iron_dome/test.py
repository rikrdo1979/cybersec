import time, datetime, os, sys, re
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

current_datetime = datetime.datetime.now().strftime("%d-%m-%Y | %H:%M:%S.%f")[:-3]

def write_log(log_line):
	log_path = "/var/log/irondome/"
	log_file = "irondome.log"
	os.makedirs(log_path, exist_ok=True)
	with open(log_path+log_file,'a+') as file:
		file.write(f"{log_line}\n")
		file.close()
	return(True)

def on_created(event):
	log_line = (f"{current_datetime} | {event.src_path} [{event.src_path.split('/')[-1]}] - CREATED")
	print(log_line)
	write_log(log_line)
	
def on_deleted(event):
	log_line = (f"{current_datetime} | {event.src_path} [{event.src_path.split('/')[-1]}] - DELETED")
	print(log_line)
	write_log(log_line)


def on_modified(event):
	log_line = (f"{current_datetime} | {event.src_path} [{event.src_path.split('/')[-1]}] - MODIFIED")
	print(log_line)
	write_log(log_line)


def on_moved(event):
	log_line = (f"{current_datetime} | {event.src_path} [{event.src_path.split('/')[-1]}] - MOVED TO - {event.dest_path}")
	print(log_line)
	write_log(log_line)

def monitor(path, patterns):
	ignore_patterns = None
	ignore_directories = False
	case_sensitive = True
	event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
	event_handler.on_created = on_created
	event_handler.on_deleted = on_deleted
	event_handler.on_modified = on_modified
	event_handler.on_moved = on_moved
	go_recursively = True
	observer = Observer()
	observer.schedule(event_handler, path, recursive=go_recursively)
	observer.start()
	log_line = (f"Start watching [ {path} ] ON {current_datetime}")
	write_log(log_line)
	print(f'\nStart watching [ {path} ]\n')
	
	try:
		while True:
			time.sleep(1)
	except KeyboardInterrupt:
		observer.stop()
		observer.join()

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
							ext = '.'+ext.lower()
						to_set.add('*'+ext)
						to_watch = list(to_set)
				if (len(to_watch) == 0):
					to_watch = ['*']
				print(" \n\033[1mPath to follow:\n\n*** \033[0m \033[95m" + path + "\033[0m ***")
				print(" \n\033[1mExtension(s) to follow:\n\n*** \033[0m \033[95m" + str(to_watch) + "\033[0m ***")
				monitor(path, to_watch)
	else:
		print("\nAdd at least 1 argument! Try again!.\n")

if __name__=="__main__":
	try:
		main()
	except KeyboardInterrupt:
		exit_gracefully()
	finally:
		pass