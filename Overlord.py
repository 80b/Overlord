import os


# Define colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def Info():
    print("This is a python command line tool created by Raz!")
    

#by raz, dont skid
def OverlordMenu():
	print(bcolors.FAIL + """

   ___                          __                        __  
 .'   `.                       [  |                      |  ] 
/  .-.  \ _   __  .---.  _ .--. | |  .--.   _ .--.   .--.| |  
| |   | |[ \ [  ]/ /__\\[ `/'`\]| |/ .'`\ \[ `/'`\]/ /'`\' |  
\  `-'  / \ \/ / | \__., | |    | || \__. | | |    | \__/  |  
 `.___.'   \__/   '.__.'[___]  [___]'.__.' [___]    '.__.;__] 
                                                              
By: Raz

[1] Exit
[2] Select the hostname for Overlord
[3] Info
	""" + bcolors.ENDC)
OverlordMenu()
select = int(input("Which option?: "))

# Declare ina as none so it can define
ina = None

#Make command input
def cmd():
	argz = input(bcolors.OKCYAN + ina + "@overlord $ " + bcolors.ENDC)
	os.system(argz)

# While loop for the command input
# TODO: add more options
while select != 1:
	if select == 2:
		if ina == None:
			ina = input("What do you want your hostname to be?: ")
			os.system('clear')
			cmd()

		else:
			cmd()
	if select == 3:
		Info()
		OverlordMenu()
		select = int(input("Which option?: "))
