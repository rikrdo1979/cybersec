from time import sleep

#animation = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
#animation = ['|', '/', '-', '\\']
animation = ["■         ","■■        ", "■■■       ", "■■■■      ", "■■■■■     ", "■■■■■■    ", "■■■■■■■   ", "■■■■■■■■  ", "■■■■■■■■■ ", "■■■■■■■■■■"]

# replace while True: for your loop

while True:                 
	for a in range(1, len(animation)):
		print('Searching... \033[1m\033[1;32m'+animation[a]+'\033[0m\033[0m', end='\r')
		sleep(0.01)
