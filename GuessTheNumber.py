import random

def main():
	randNumber = random.randint(1, 100)
	numNotGuessed = True
	while(numNotGuessed):
		guess = input("Guess the number(1-100): ")
		try:
			guess = int(guess)
		except ValueError as ex:
			print('Enter a number please')
			continue
		##if number is not in bounds then tell the user to try again
		if(guess < 1 or guess > 100):
			print('Please stay within the bounds of the prompt')
			continue
		##if they guess the number the game ends
		if(randNumber == guess):
			print('You guess the number correctly')
			break
		##if they guess higher than the number, tell them. Same for if they guess lower
		elif(randNumber <= guess):
			print('You guessed too high')
		elif(randNumber >= guess):
			print('You guessed too low')

if __name__ == "__main__":
	main()
