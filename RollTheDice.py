import random

def main():
	dice1 = 0
	dice2 = 0

	while (True):
		choice = input('Roll the dice? Y/N')
		if (choice == 'Y'):
			dice1 = random.randint(1,6)
			dice2 = random.randint(1,6)
			print('The rolls were ', dice1, ' ', dice2)
		else:
			break

if __name__ == "__main__":
	main()

