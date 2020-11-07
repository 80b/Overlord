import os

#by raz, dont skid
def OverlordMenu():
	print("""

   ___                          __                        __  
 .'   `.                       [  |                      |  ] 
/  .-.  \ _   __  .---.  _ .--. | |  .--.   _ .--.   .--.| |  
| |   | |[ \ [  ]/ /__\\[ `/'`\]| |/ .'`\ \[ `/'`\]/ /'`\' |  
\  `-'  / \ \/ / | \__., | |    | || \__. | | |    | \__/  |  
 `.___.'   \__/   '.__.'[___]  [___]'.__.' [___]    '.__.;__] 
                                                              
By: Raz

[1] Exit
[2] Select the hostname for Overlord
	""")
OverlordMenu()
select = int(input("Which option?: "))


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
ina = None


def cmd():
	argz = input(bcolors.OKCYAN + ina + "@overlord $ " + bcolors.ENDC)
	os.system(argz)
while select != 1:
	if select == 2:
		if ina == None:
			ina = input("What do you want your hostname to be?: ")
			os.system('clear')
			cmd()

		else:
			cmd()
