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



ina = None


def cmd():
	argz = input(ina + "@overlord $ ")
	os.system(argz)
while select != 1:
	if select == 2:
		if ina == None:
			ina = input("What do you want your hostname to be?: ")
			os.system('clear')
			cmd()

		else:
			cmd()
